# Use a standard Ubuntu base image
FROM ubuntu:22.04

# Set non-interactive installation mode
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install basic utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    wget \
    gnupg \
    lsb-release \
    vim \
    nano \
    git \
    bash \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# # Install LaTeX (pdflatex)
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     texlive-latex-base \
#     texlive-fonts-recommended \
#     texlive-latex-extra \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# # Install GatPack - explicitly use bash to run the script in non-interactive mode
# RUN curl -LsSf https://raw.githubusercontent.com/GatlenCulp/gatpack/refs/heads/main/install.sh -o /tmp/install.sh && \
#     chmod +x /tmp/install.sh && \
#     bash /tmp/install.sh -y

# Default command to keep container running
CMD ["bash"]