---
layout: container
name:  "quay.io/biocontainers/submission-excel2xml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/submission-excel2xml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/submission-excel2xml/container.yaml"
updated_at: "2024-05-14 03:09:24.349679"
latest: "2.6--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/submission-excel2xml"
aliases:
 - "addr2line"
 - "ar"
 - "as"
 - "c++"
 - "c++filt"
 - "cc"
 - "cpp"
 - "dwp"
 - "elfedit"
 - "excel2xml_dra.rb"
 - "excel2xml_jga.rb"
 - "g++"
 - "gcc"
 - "gcc-ar"
 - "gcc-nm"
 - "gcc-ranlib"
 - "gcov"
 - "gcov-dump"
 - "gcov-tool"
 - "gfortran"
 - "gold"
 - "gprof"
 - "ld"
 - "ld.bfd"
 - "ld.gold"
 - "nm"
 - "objcopy"
 - "objdump"
 - "ranlib"
 - "rbs"
 - "rdbg"
 - "readelf"
 - "size"
 - "strings"
 - "strip"
 - "typeprof"
 - "validate_meta_dra.rb"
 - "validate_meta_jga.rb"
 - "racc"
 - "bundle"
 - "bundler"
 - "gdbm_dump"
 - "gdbm_load"
 - "gdbmtool"
 - "erb"
 - "gem"
 - "irb"
 - "rake"
 - "rdoc"
 - "ri"
 - "ruby"
versions:
 - "2.0.0--hf0b54c8_0"
 - "2.5--hdfd78af_0"
 - "2.6--hdfd78af_0"
description: "singularity registry hpc automated addition for submission-excel2xml"
config: {"url": "https://biocontainers.pro/tools/submission-excel2xml", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for submission-excel2xml", "latest": {"2.6--hdfd78af_0": "sha256:340df444ab3b004d61f568c6210f3636ce01c839da2abce91f6d0e185b8209fd"}, "tags": {"2.0.0--hf0b54c8_0": "sha256:8ffffb5c7df8e42f9b2ae583325e0e7619a7b8354f7434d4624560c10dd3bd07", "2.5--hdfd78af_0": "sha256:418c528cb8800476abc553ab808c8c424cb6df41fe6cce2cb30f033423f0d777", "2.6--hdfd78af_0": "sha256:340df444ab3b004d61f568c6210f3636ce01c839da2abce91f6d0e185b8209fd"}, "docker": "quay.io/biocontainers/submission-excel2xml", "aliases": {"addr2line": "/usr/local/bin/addr2line", "ar": "/usr/local/bin/ar", "as": "/usr/local/bin/as", "c++": "/usr/local/bin/c++", "c++filt": "/usr/local/bin/c++filt", "cc": "/usr/local/bin/cc", "cpp": "/usr/local/bin/cpp", "dwp": "/usr/local/bin/dwp", "elfedit": "/usr/local/bin/elfedit", "excel2xml_dra.rb": "/usr/local/bin/excel2xml_dra.rb", "excel2xml_jga.rb": "/usr/local/bin/excel2xml_jga.rb", "g++": "/usr/local/bin/g++", "gcc": "/usr/local/bin/gcc", "gcc-ar": "/usr/local/bin/gcc-ar", "gcc-nm": "/usr/local/bin/gcc-nm", "gcc-ranlib": "/usr/local/bin/gcc-ranlib", "gcov": "/usr/local/bin/gcov", "gcov-dump": "/usr/local/bin/gcov-dump", "gcov-tool": "/usr/local/bin/gcov-tool", "gfortran": "/usr/local/bin/gfortran", "gold": "/usr/local/bin/gold", "gprof": "/usr/local/bin/gprof", "ld": "/usr/local/bin/ld", "ld.bfd": "/usr/local/bin/ld.bfd", "ld.gold": "/usr/local/bin/ld.gold", "nm": "/usr/local/bin/nm", "objcopy": "/usr/local/bin/objcopy", "objdump": "/usr/local/bin/objdump", "ranlib": "/usr/local/bin/ranlib", "rbs": "/usr/local/bin/rbs", "rdbg": "/usr/local/bin/rdbg", "readelf": "/usr/local/bin/readelf", "size": "/usr/local/bin/size", "strings": "/usr/local/bin/strings", "strip": "/usr/local/bin/strip", "typeprof": "/usr/local/bin/typeprof", "validate_meta_dra.rb": "/usr/local/bin/validate_meta_dra.rb", "validate_meta_jga.rb": "/usr/local/bin/validate_meta_jga.rb", "racc": "/usr/local/bin/racc", "bundle": "/usr/local/bin/bundle", "bundler": "/usr/local/bin/bundler", "gdbm_dump": "/usr/local/bin/gdbm_dump", "gdbm_load": "/usr/local/bin/gdbm_load", "gdbmtool": "/usr/local/bin/gdbmtool", "erb": "/usr/local/bin/erb", "gem": "/usr/local/bin/gem", "irb": "/usr/local/bin/irb", "rake": "/usr/local/bin/rake", "rdoc": "/usr/local/bin/rdoc", "ri": "/usr/local/bin/ri", "ruby": "/usr/local/bin/ruby"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/submission-excel2xml.
singularity registry hpc automated addition for submission-excel2xml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/submission-excel2xml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/submission-excel2xml:2.6--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/submission-excel2xml/2.6--hdfd78af_0
$ module help quay.io/biocontainers/submission-excel2xml/2.6--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### submission-excel2xml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### submission-excel2xml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### submission-excel2xml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### submission-excel2xml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### submission-excel2xml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### submission-excel2xml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addr2line

```bash
$ singularity exec <container> /usr/local/bin/addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ar

```bash
$ singularity exec <container> /usr/local/bin/ar
$ podman run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### as

```bash
$ singularity exec <container> /usr/local/bin/as
$ podman run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++

```bash
$ singularity exec <container> /usr/local/bin/c++
$ podman run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++filt

```bash
$ singularity exec <container> /usr/local/bin/c++filt
$ podman run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cc

```bash
$ singularity exec <container> /usr/local/bin/cc
$ podman run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp

```bash
$ singularity exec <container> /usr/local/bin/cpp
$ podman run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwp

```bash
$ singularity exec <container> /usr/local/bin/dwp
$ podman run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elfedit

```bash
$ singularity exec <container> /usr/local/bin/elfedit
$ podman run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### excel2xml_dra.rb

```bash
$ singularity exec <container> /usr/local/bin/excel2xml_dra.rb
$ podman run --it --rm --entrypoint /usr/local/bin/excel2xml_dra.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/excel2xml_dra.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### excel2xml_jga.rb

```bash
$ singularity exec <container> /usr/local/bin/excel2xml_jga.rb
$ podman run --it --rm --entrypoint /usr/local/bin/excel2xml_jga.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/excel2xml_jga.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g++

```bash
$ singularity exec <container> /usr/local/bin/g++
$ podman run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc

```bash
$ singularity exec <container> /usr/local/bin/gcc
$ podman run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ar

```bash
$ singularity exec <container> /usr/local/bin/gcc-ar
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-nm

```bash
$ singularity exec <container> /usr/local/bin/gcc-nm
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ranlib

```bash
$ singularity exec <container> /usr/local/bin/gcc-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov

```bash
$ singularity exec <container> /usr/local/bin/gcov
$ podman run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-dump

```bash
$ singularity exec <container> /usr/local/bin/gcov-dump
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-tool

```bash
$ singularity exec <container> /usr/local/bin/gcov-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfortran

```bash
$ singularity exec <container> /usr/local/bin/gfortran
$ podman run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gold

```bash
$ singularity exec <container> /usr/local/bin/gold
$ podman run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gprof

```bash
$ singularity exec <container> /usr/local/bin/gprof
$ podman run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld

```bash
$ singularity exec <container> /usr/local/bin/ld
$ podman run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.bfd

```bash
$ singularity exec <container> /usr/local/bin/ld.bfd
$ podman run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.gold

```bash
$ singularity exec <container> /usr/local/bin/ld.gold
$ podman run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.gold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nm

```bash
$ singularity exec <container> /usr/local/bin/nm
$ podman run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objcopy

```bash
$ singularity exec <container> /usr/local/bin/objcopy
$ podman run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### objdump

```bash
$ singularity exec <container> /usr/local/bin/objdump
$ podman run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbs

```bash
$ singularity exec <container> /usr/local/bin/rbs
$ podman run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdbg

```bash
$ singularity exec <container> /usr/local/bin/rdbg
$ podman run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readelf

```bash
$ singularity exec <container> /usr/local/bin/readelf
$ podman run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readelf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### size

```bash
$ singularity exec <container> /usr/local/bin/size
$ podman run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strings

```bash
$ singularity exec <container> /usr/local/bin/strings
$ podman run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip

```bash
$ singularity exec <container> /usr/local/bin/strip
$ podman run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeprof

```bash
$ singularity exec <container> /usr/local/bin/typeprof
$ podman run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_meta_dra.rb

```bash
$ singularity exec <container> /usr/local/bin/validate_meta_dra.rb
$ podman run --it --rm --entrypoint /usr/local/bin/validate_meta_dra.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_meta_dra.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### validate_meta_jga.rb

```bash
$ singularity exec <container> /usr/local/bin/validate_meta_jga.rb
$ podman run --it --rm --entrypoint /usr/local/bin/validate_meta_jga.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/validate_meta_jga.rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle

```bash
$ singularity exec <container> /usr/local/bin/bundle
$ podman run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundler

```bash
$ singularity exec <container> /usr/local/bin/bundler
$ podman run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_dump

```bash
$ singularity exec <container> /usr/local/bin/gdbm_dump
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbm_load

```bash
$ singularity exec <container> /usr/local/bin/gdbm_load
$ podman run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbm_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdbmtool

```bash
$ singularity exec <container> /usr/local/bin/gdbmtool
$ podman run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdbmtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb

```bash
$ singularity exec <container> /usr/local/bin/erb
$ podman run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem

```bash
$ singularity exec <container> /usr/local/bin/gem
$ podman run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb

```bash
$ singularity exec <container> /usr/local/bin/irb
$ podman run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake

```bash
$ singularity exec <container> /usr/local/bin/rake
$ podman run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc

```bash
$ singularity exec <container> /usr/local/bin/rdoc
$ podman run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri

```bash
$ singularity exec <container> /usr/local/bin/ri
$ podman run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby

```bash
$ singularity exec <container> /usr/local/bin/ruby
$ podman run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)