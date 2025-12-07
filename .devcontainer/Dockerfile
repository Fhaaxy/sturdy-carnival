FROM debian:stable

RUN apt-get update && apt-get upgrade -y

# C++ toolchain
RUN apt-get install -y \
    build-essential \
    cmake \
    gdb

# Python environment
RUN apt-get install -y \
    python3 \
    python3-pip

# Utilities
RUN apt-get install -y \
    git \
    nano

WORKDIR /workspace