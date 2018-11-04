FROM debian:9-slim as base

FROM base as builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
      g++ \
      make \
      cmake \
      wget \
      git \
      build-essential \
      python3-dev \
      python3-pip \
      python3-setuptools 

FROM builder as deps
COPY Makefile requirements.txt /tmp/
WORKDIR /tmp
RUN make install-deps

FROM deps as install
COPY . /tmp/
WORKDIR /tmp
RUN make install

FROM base
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
      python3 \
      python3-pkg-resources
COPY --from=install /usr/local /usr/local
ENTRYPOINT ["lucia"]

