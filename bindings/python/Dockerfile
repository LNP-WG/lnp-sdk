FROM rust:1.47.0-slim-buster

RUN apt-get update -y \
    && apt-get install -y \
        cmake \
        g++ \
        git \
        libpcre3-dev \
        libpq-dev \
        libssl-dev \
        libzmq3-dev \
        make \
        perl \
        pkg-config \
        python3-pip \
        wget

RUN wget https://freefr.dl.sourceforge.net/project/swig/swig/swig-4.0.1/swig-4.0.1.tar.gz && \
    tar xf swig-*.tar.gz && \
    cd swig-* && \
    ./configure && make -j12 && \
    make install

COPY bindings/python /lnp-sdk/bindings/python
COPY rust-lib /lnp-sdk/rust-lib

WORKDIR /lnp-sdk/bindings/python

RUN python3 -m pip install --upgrade pip setuptools wheel \
    && python3 setup.py build_ext
