# Node.js bindings

## Build

In order to build Node.js bindings, from the project root follow the
[Local](#local) or [In docker](#in-docker) instructions.

Both instructions will generate the files `liblnp.so` in `rust-lib/target/release/`
and `lnp.node` in `bindings/nodejs/build/Release/`.

### Local

* Install dependencies: Node.js v10, node-gyp, swig 4.0
* From the project root run:
```bash
cd bindings/npm
npm install
```

### In docker

```bash
docker build -f bindings/npmnpm/Dockerfile -t lnp-sdk-npm .
docker run --rm -v $(pwd):/opt/mount --entrypoint bash \
    lnp-sdk-npm \
    -c 'mkdir -p /opt/mount/liblnp/target/release /opt/mount/bindings/npm/build/Release \
    && cp /lnp-sdk/target/release/liblnp.so /opt/mount/liblnp/target/release/liblnp.so \
    && cp /lnp-sdk/lnp.node /opt/mount/bindings/npm/build/Release/lnp.node'
```

## Usage

To try the generated library, you can use:
- [node.js demo](/demo/nodejs)
