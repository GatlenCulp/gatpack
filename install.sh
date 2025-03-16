#!/bin/sh

# Exit on error
set -e

# Check for -y flag for non-interactive mode
YES_MODE=false
if [ "$1" = "-y" ]; then
    YES_MODE=true
fi

# Check if running in a pipe (non-interactive)
if [ ! -t 0 ]; then
    echo "Detected non-interactive mode (piped input). Automatically answering yes to all prompts."
    YES_MODE=true
fi

# Check if running in Docker
IN_DOCKER=false
if [ -f /.dockerenv ] || grep -q docker /proc/1/cgroup 2>/dev/null; then
    IN_DOCKER=true
    echo "Detected Docker environment"
fi

# Function to handle prompts in yes mode
prompt() {
    local message="$1"
    local default="$2"
    
    if [ "$YES_MODE" = true ]; then
        echo "$message (Automatically answering: Yes)"
        return 0
    else
        printf "%s " "$message"
        read response
        if [ -z "$response" ]; then
            response="$default"
        fi
        case "$response" in
            [Yy]*)
                return 0
                ;;
            *)
                return 1
                ;;
        esac
    fi
}

# More thorough check if GatPack is already installed and working
GATPACK_INSTALLED=false
if command -v gatpack > /dev/null 2>&1; then
    # Try to run a simple command to verify it actually works
    if gatpack --version > /dev/null 2>&1; then
        GATPACK_INSTALLED=true
        GATPACK_VERSION=$(gatpack --version 2>/dev/null || echo "unknown")
        echo "
✅ GatPack is already installed and working!
Current version: $GATPACK_VERSION

Would you like to reinstall or update GatPack?
"
        if ! prompt "Reinstall/update GatPack? (y/N)" "N"; then
            echo "Installation cancelled. GatPack is already installed."
            exit 0
        fi
    fi
fi

# If we get here, either GatPack is not installed or user wants to reinstall

echo "
🚀 GatPack Installation Script 🚀
================================

This script will:
1. Install the uv package manager if not already installed
2. Install GatPack using uv
3. Check for and install LaTeX (pdflatex) if needed:
   - On macOS: Using Homebrew and MacTeX
   - On Linux: Using apt-get and texlive packages
4. Optionally set up a GatPack project in your Documents folder

Note: This may require sudo privileges for some installations.
"

# Ask for confirmation
if ! prompt "Would you like to proceed with the installation? (y/N)" "N"; then
    echo "Installation cancelled."
    exit 0
fi

echo "📦 Installing GatPack..."

# Check if uv is installed, install if not
if ! command -v uv > /dev/null 2>&1; then
    echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Source the environment file to update PATH
    if [ -f "$HOME/.local/bin/env" ]; then
        . "$HOME/.local/bin/env"
    elif [ -f "$HOME/.uv/env" ]; then
        . "$HOME/.uv/env"
    fi
    
    # Add to PATH directly if needed
    if ! command -v uv > /dev/null 2>&1; then
        echo "Adding uv to PATH for this session..."
        export PATH="$HOME/.local/bin:$PATH"
    fi
fi

# Install GatPack using uv tool
echo "📚 Installing GatPack..."
uv tool install gatpack

# Update shell configuration and current session PATH
uv tool update-shell

# Add uv tool bin to PATH for current session
UV_TOOL_PATH=$(uv tool path 2>/dev/null || echo "")
if [ -n "$UV_TOOL_PATH" ]; then
    export PATH="$UV_TOOL_PATH:$PATH"
fi

# Check if pdflatex is installed
if ! command -v pdflatex > /dev/null 2>&1; then
    echo "⚠️ LaTeX (pdflatex) is not installed."
    
    # Check if running on macOS
    if [ "$(uname)" = "Darwin" ]; then
        if ! command -v brew > /dev/null 2>&1; then
            echo "🍺 Homebrew not found. Installing Homebrew..."
            /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            
            # Add Homebrew to PATH based on chip architecture
            if [ "$(uname -m)" = "arm64" ]; then
                echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
                eval "$(/opt/homebrew/bin/brew shellenv)"
            else
                echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
                eval "$(/usr/local/bin/brew shellenv)"
            fi
        fi
        
        echo "🍺 Installing MacTeX using Homebrew..."
        brew install --cask mactex
    # Check if running on Linux with apt-get
    elif command -v apt-get > /dev/null 2>&1; then
        echo "📦 Installing LaTeX using apt-get..."
        # Use sudo only if not in Docker
        if [ "$IN_DOCKER" = true ]; then
            apt-get update
            apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-latex-extra
        else
            sudo apt-get update
            sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-latex-extra
        fi
    else
        echo "❌ Please install LaTeX (pdflatex) manually for your operating system."
        exit 1
    fi
fi

# Verify installation and provide fallback instructions if not found
echo "✅ Verifying installation..."
if command -v gatpack > /dev/null 2>&1; then
    gatpack --help
else
    echo "⚠️ gatpack command not found in current PATH."
    echo "This is likely because the shell needs to be restarted to apply PATH changes."
    echo ""
    echo "Please try one of the following:"
    echo "1. Run 'source ~/.bashrc' or 'source ~/.zshrc' (depending on your shell)"
    echo "2. Start a new terminal session"
    echo "3. Run the gatpack command directly from: $(uv tool path 2>/dev/null || echo "$HOME/.local/bin")/gatpack"
    
    # Try to find gatpack directly
    POSSIBLE_PATHS="$HOME/.local/bin $HOME/.uv/bin $(uv tool path 2>/dev/null)"
    for path in $POSSIBLE_PATHS; do
        if [ -f "$path/gatpack" ]; then
            echo ""
            echo "✅ Found gatpack at: $path/gatpack"
            echo "You can run it directly with: $path/gatpack"
            break
        fi
    done
fi

# Skip project setup in Docker
if [ "$IN_DOCKER" = false ]; then
    # Ask user about project setup
    if prompt "Would you like to set up a GatPack project in your Documents folder? (y/N)" "N"; then
        echo "📁 Setting up project in ~/Documents..."
        
        # Use full path to gatpack if needed
        GATPACK_CMD="gatpack"
        if ! command -v gatpack > /dev/null 2>&1; then
            for path in $POSSIBLE_PATHS; do
                if [ -f "$path/gatpack" ]; then
                    GATPACK_CMD="$path/gatpack"
                    break
                fi
            done
            if [ "$GATPACK_CMD" = "gatpack" ]; then
                GATPACK_CMD="$(uv tool path 2>/dev/null || echo "$HOME/.local/bin")/gatpack"
            fi
        fi
        
        cd ~/Documents \
        && $GATPACK_CMD init \
        && open .
    fi
else
    echo "Skipping project setup in Docker environment"
fi

echo "
🎉 Installation complete! You can now use GatPack.

Quick start:
1. Create a new project:       gatpack init
2. Build example project:      gatpack compose reading-packet --overwrite

For more information, see the documentation at:
https://github.com/GatlenCulp/gatpack
"
