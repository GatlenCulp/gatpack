#!/bin/bash

# Exit on error
set -e

echo "�� Installing GatPack..."

# Check if uv is installed, install if not
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Install GatPack using uv tool
echo "📚 Installing GatPack..."
uv tool install gatpack
uv tool update-shell

# Check if pdflatex is installed
if ! command -v pdflatex &> /dev/null; then
    echo "⚠️ LaTeX (pdflatex) is not installed."
    
    # Check if running on macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "🍺 Homebrew not found. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            
            # Add Homebrew to PATH based on chip architecture
            if [[ $(uname -m) == "arm64" ]]; then
                echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
                eval "$(/opt/homebrew/bin/brew shellenv)"
            else
                echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
                eval "$(/usr/local/bin/brew shellenv)"
            fi
        fi
        
        echo "🍺 Installing MacTeX using Homebrew..."
        brew install --cask mactex
    else
        echo "❌ Please install LaTeX (pdflatex) manually for your operating system."
        exit 1
    fi
fi

# Verify installation
echo "✅ Verifying installation..."
gatpack --help

# Ask user about project setup
read -p "Would you like to set up a GatPack project in your Documents folder? (y/N) " setup_project

if [[ "$setup_project" =~ ^[Yy]$ ]]; then
    echo "📁 Setting up project in ~/Documents..."
    cd ~/Documents \
    && gatpack init \
    && open .
fi

echo "
🎉 Installation complete! You can now use GatPack.

Quick start:
1. Create a new project:       gatpack init
2. Build example project:      gatpack compose reading-packet --overwrite

For more information, see the documentation at:
https://github.com/GatlenCulp/gatpack
"
