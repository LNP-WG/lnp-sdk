# Python bindings

## Build

In order to build Python bindings, first follow
[main README's instructions](/README.md) and then, from the project root,
follow the [Local](#local) or [In docker](#in-docker) instructions.

Both instructions will generate the files `liblnp.so` in
`rust-lib/target/release/` and a shared object file
(e.g. `_lnp_node.cpython-37m-x86_64-linux-gnu.so`)
and `lnp_node.py` in `bindings/python/`.

### Local

* Install dependencies: python3-dev, swig 4.0
* From the project root run:
```bash
cd bindings/python
python3 setup.py build_ext
```

### In docker

```bash
docker build -f bindings/python/Dockerfile -t lnp-sdk-python .
docker run --rm -v $(pwd):/opt/mount --entrypoint bash \
    lnp-sdk-python \
    -c 'mkdir -p /opt/mount/liblnp/target/release \
    && cp /lnp-sdk/liblnp/target/release/liblnp.so /opt/mount/liblnp/target/release/ \
    && cp /lnp-sdk/bindings/python/*.so /opt/mount/bindings/python/ \
    && cp /lnp-sdk/bindings/python/lnp.py /opt/mount/bindings/python/'
```

## Usage

To try the generated library, you can use:
- [python demo](/demo/python)
