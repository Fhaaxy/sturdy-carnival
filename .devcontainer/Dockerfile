FROM debian:stable

# Update & upgrade
RUN apt-get update && apt-get upgrade -y

# C++ toolchain
RUN apt-get install -y \
    build-essential \
    cmake \
    gdb

# Python environment (aggiunta la parte necessaria!)
RUN apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Utilities
RUN apt-get install -y \
    git \
    nano

WORKDIR /workspace