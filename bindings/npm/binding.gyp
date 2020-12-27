{
  "targets": [
    {
      "target_name": "lnplib",
      "sources": [ "swig_wrap.cxx" ],
      "libraries": [
           '-L<(module_root_dir)/../../liblnp/target/release',
           '-llnp',
       ],
      "include_dirs": [
           '../../liblnp',
       ],
      "ldflags": [
           '-Wl,-rpath,../../liblnp/target/release/'
       ],
      "cflags!": ["-std=c++11"],
    }
  ]
}
