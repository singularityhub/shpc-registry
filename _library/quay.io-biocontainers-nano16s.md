---
layout: container
name:  "quay.io/biocontainers/nano16s"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nano16s/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nano16s/container.yaml"
updated_at: "2026-10-10 19:54:11.973827"
latest: "1.2.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/nano16s"
aliases:
 - "NanoStat"
 - "bioawk"
 - "chopper"
 - "clang++-23"
 - "clang-23"
 - "clang-cl-23"
 - "clang-cpp-23"
 - "emu"
 - "nano16s"
 - "porechop_abi"
 - "x86_64-conda-linux-gnu-clang"
 - "x86_64-conda-linux-gnu-clang-cpp"
 - "x86_64-conda-linux-gnu-clang-cpp.cfg"
 - "x86_64-conda-linux-gnu-clang.cfg"
 - "x86_64-conda-linux-gnu-flang.cfg"
 - "clang-cl"
 - "clang-cpp"
 - "addr2line"
 - "as"
 - "c++filt"
 - "clang"
 - "elfedit"
 - "gprof"
 - "ld.bfd"
 - "nm"
 - "objcopy"
 - "objdump"
 - "readelf"
 - "size"
 - "strings"
 - "ar"
 - "ld"
 - "ranlib"
 - "strip"
 - "seq_cache_populate.py"
 - "phc"
 - "eido"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
versions:
 - "1.2.2--hdfd78af_0"
description: "singularity registry hpc automated addition for nano16s"
config: {"url": "https://biocontainers.pro/tools/nano16s", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nano16s", "latest": {"1.2.2--hdfd78af_0": "sha256:f34f6d72f3314fcb66c9a3212f0d18ea0f2127a6ece0222bac17e872da9c7ede"}, "tags": {"1.2.2--hdfd78af_0": "sha256:f34f6d72f3314fcb66c9a3212f0d18ea0f2127a6ece0222bac17e872da9c7ede"}, "docker": "quay.io/biocontainers/nano16s", "aliases": {"NanoStat": "/usr/local/bin/NanoStat", "bioawk": "/usr/local/bin/bioawk", "chopper": "/usr/local/bin/chopper", "clang++-23": "/usr/local/bin/clang++-23", "clang-23": "/usr/local/bin/clang-23", "clang-cl-23": "/usr/local/bin/clang-cl-23", "clang-cpp-23": "/usr/local/bin/clang-cpp-23", "emu": "/usr/local/bin/emu", "nano16s": "/usr/local/bin/nano16s", "porechop_abi": "/usr/local/bin/porechop_abi", "x86_64-conda-linux-gnu-clang": "/usr/local/bin/x86_64-conda-linux-gnu-clang", "x86_64-conda-linux-gnu-clang-cpp": "/usr/local/bin/x86_64-conda-linux-gnu-clang-cpp", "x86_64-conda-linux-gnu-clang-cpp.cfg": "/usr/local/bin/x86_64-conda-linux-gnu-clang-cpp.cfg", "x86_64-conda-linux-gnu-clang.cfg": "/usr/local/bin/x86_64-conda-linux-gnu-clang.cfg", "x86_64-conda-linux-gnu-flang.cfg": "/usr/local/bin/x86_64-conda-linux-gnu-flang.cfg", "clang-cl": "/usr/local/bin/clang-cl", "clang-cpp": "/usr/local/bin/clang-cpp", "addr2line": "/usr/local/bin/addr2line", "as": "/usr/local/bin/as", "c++filt": "/usr/local/bin/c++filt", "clang": "/usr/local/bin/clang", "elfedit": "/usr/local/bin/elfedit", "gprof": "/usr/local/bin/gprof", "ld.bfd": "/usr/local/bin/ld.bfd", "nm": "/usr/local/bin/nm", "objcopy": "/usr/local/bin/objcopy", "objdump": "/usr/local/bin/objdump", "readelf": "/usr/local/bin/readelf", "size": "/usr/local/bin/size", "strings": "/usr/local/bin/strings", "ar": "/usr/local/bin/ar", "ld": "/usr/local/bin/ld", "ranlib": "/usr/local/bin/ranlib", "strip": "/usr/local/bin/strip", "seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "phc": "/usr/local/bin/phc", "eido": "/usr/local/bin/eido", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nano16s.
singularity registry hpc automated addition for nano16s
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nano16s
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nano16s:1.2.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nano16s/1.2.2--hdfd78af_0
$ module help quay.io/biocontainers/nano16s/1.2.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nano16s-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nano16s-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nano16s-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nano16s-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nano16s-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nano16s-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoStat

```bash
$ singularity exec <container> /usr/local/bin/NanoStat
$ podman run --it --rm --entrypoint /usr/local/bin/NanoStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioawk

```bash
$ singularity exec <container> /usr/local/bin/bioawk
$ podman run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chopper

```bash
$ singularity exec <container> /usr/local/bin/chopper
$ podman run --it --rm --entrypoint /usr/local/bin/chopper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chopper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang++-23

```bash
$ singularity exec <container> /usr/local/bin/clang++-23
$ podman run --it --rm --entrypoint /usr/local/bin/clang++-23   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang++-23   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-23

```bash
$ singularity exec <container> /usr/local/bin/clang-23
$ podman run --it --rm --entrypoint /usr/local/bin/clang-23   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-23   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cl-23

```bash
$ singularity exec <container> /usr/local/bin/clang-cl-23
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cl-23   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cl-23   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cpp-23

```bash
$ singularity exec <container> /usr/local/bin/clang-cpp-23
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cpp-23   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cpp-23   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emu

```bash
$ singularity exec <container> /usr/local/bin/emu
$ podman run --it --rm --entrypoint /usr/local/bin/emu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nano16s

```bash
$ singularity exec <container> /usr/local/bin/nano16s
$ podman run --it --rm --entrypoint /usr/local/bin/nano16s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nano16s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### porechop_abi

```bash
$ singularity exec <container> /usr/local/bin/porechop_abi
$ podman run --it --rm --entrypoint /usr/local/bin/porechop_abi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porechop_abi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-clang

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-clang
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-clang-cpp

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-clang-cpp.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang-cpp.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-clang.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-clang.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-clang.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-flang.cfg

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-flang.cfg
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-flang.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-flang.cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cl

```bash
$ singularity exec <container> /usr/local/bin/clang-cl
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang-cpp

```bash
$ singularity exec <container> /usr/local/bin/clang-cpp
$ podman run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang-cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addr2line

```bash
$ singularity exec <container> /usr/local/bin/addr2line
$ podman run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addr2line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### as

```bash
$ singularity exec <container> /usr/local/bin/as
$ podman run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++filt

```bash
$ singularity exec <container> /usr/local/bin/c++filt
$ podman run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clang

```bash
$ singularity exec <container> /usr/local/bin/clang
$ podman run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elfedit

```bash
$ singularity exec <container> /usr/local/bin/elfedit
$ podman run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elfedit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gprof

```bash
$ singularity exec <container> /usr/local/bin/gprof
$ podman run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld.bfd

```bash
$ singularity exec <container> /usr/local/bin/ld.bfd
$ podman run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld.bfd   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ar

```bash
$ singularity exec <container> /usr/local/bin/ar
$ podman run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ld

```bash
$ singularity exec <container> /usr/local/bin/ld
$ podman run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip

```bash
$ singularity exec <container> /usr/local/bin/strip
$ podman run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phc

```bash
$ singularity exec <container> /usr/local/bin/phc
$ podman run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eido

```bash
$ singularity exec <container> /usr/local/bin/eido
$ podman run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
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