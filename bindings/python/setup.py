#!/usr/bin/env python3

"""
Bundle LNP Python bindings with setuptools
"""

import sys
import platform

from setuptools.command.build_ext import build_ext
# keep Extension import after setuptools to avoid class replacement
# see https://github.com/pypa/setuptools/issues/309
from distutils.core import Extension, setup
from subprocess import Popen, TimeoutExpired

RUST_LIB = '../../liblnp'


def _die(message):
    """ Prints message to stderr with error code 1 """
    sys.stderr.write(message + '\n')
    sys.exit(1)


def build_rust():
    """ Build Rust library """
    cmd = ['cargo', 'build', '--release', '--manifest-path', RUST_LIB + '/Cargo.toml']
    proc = Popen(cmd)
    try:
        _, _ = proc.communicate(timeout=600)
    except TimeoutExpired:
        proc.kill()
        _die('Build of Rust library timed out')
    if proc.returncode:
        _die('Build of Rust library failed')


class BuildExt(build_ext):
    """ Build Python bindings """

    def initialize_options(self):
        """ Overrides default behavior """
        build_ext.initialize_options(self)
        self.inplace = 1

    def run(self):
        """ Build Rust library and Python extensions """
        build_rust()
        self.force = True
        build_ext.run(self)


if __name__ == "__main__":
    if platform.system() == "Darwin":
        ext = ".dylib" # macOS requires dynamic binding; otherwise it does not find system libs
    elif platform.system() == "Windows":
        ext = ".lib"
    else:
        ext = ".a"

    lnp_node_module = Extension(
        '_lnp',
        sources=['swig.i'],
        swig_opts=['-c++', '-py3'],
        extra_objects=[RUST_LIB + '/target/release/liblnp' + ext],
    )
    setup(
        name        = 'lnp',
        version     = '0.2.0',
        author      = "LNP/BP Standards Association",
        description = 'LNP Python bindings',
        ext_modules = [lnp_node_module],
        py_modules  = ["lnp"],
        cmdclass    = {
            'build_ext': BuildExt,
        },
    )
