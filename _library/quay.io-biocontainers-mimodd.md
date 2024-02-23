---
layout: container
name:  "quay.io/biocontainers/mimodd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimodd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mimodd/container.yaml"
updated_at: "2024-02-23 02:40:02.934329"
latest: "0.1.9--py36_0"
container_url: "https://biocontainers.pro/tools/mimodd"
aliases:
 - "BATCH"
 - "COMPILE"
 - "INSTALL"
 - "LINK"
 - "REMOVE"
 - "Rcmd"
 - "Rd2pdf"
 - "Rdconv"
 - "Rdiff"
 - "Rprof"
 - "SHLIB"
 - "Stangle"
 - "Sweave"
 - "ar"
 - "build"
 - "c++"
 - "cc"
 - "check"
 - "config"
 - "f77"
 - "f77_f2c"
 - "fc"
 - "g++"
 - "gcc"
 - "gfortran"
 - "javareconf"
 - "mimodd"
 - "mkinstalldirs"
 - "pager"
 - "ranlib"
 - "rtags"
 - "strip"
 - "libtool"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "ncurses5-config"
versions:
 - "0.1.9--py36_0"
description: "shpc-registry automated BioContainers addition for mimodd"
config: {"url": "https://biocontainers.pro/tools/mimodd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mimodd", "latest": {"0.1.9--py36_0": "sha256:891054c4a37eadca5433989561a2b31842e7e21f828d50a164afab4e1bd65804"}, "tags": {"0.1.9--py36_0": "sha256:891054c4a37eadca5433989561a2b31842e7e21f828d50a164afab4e1bd65804"}, "docker": "quay.io/biocontainers/mimodd", "aliases": {"BATCH": "/usr/local/bin/BATCH", "COMPILE": "/usr/local/bin/COMPILE", "INSTALL": "/usr/local/bin/INSTALL", "LINK": "/usr/local/bin/LINK", "REMOVE": "/usr/local/bin/REMOVE", "Rcmd": "/usr/local/bin/Rcmd", "Rd2pdf": "/usr/local/bin/Rd2pdf", "Rdconv": "/usr/local/bin/Rdconv", "Rdiff": "/usr/local/bin/Rdiff", "Rprof": "/usr/local/bin/Rprof", "SHLIB": "/usr/local/bin/SHLIB", "Stangle": "/usr/local/bin/Stangle", "Sweave": "/usr/local/bin/Sweave", "ar": "/usr/local/bin/ar", "build": "/usr/local/bin/build", "c++": "/usr/local/bin/c++", "cc": "/usr/local/bin/cc", "check": "/usr/local/bin/check", "config": "/usr/local/bin/config", "f77": "/usr/local/bin/f77", "f77_f2c": "/usr/local/bin/f77_f2c", "fc": "/usr/local/bin/fc", "g++": "/usr/local/bin/g++", "gcc": "/usr/local/bin/gcc", "gfortran": "/usr/local/bin/gfortran", "javareconf": "/usr/local/bin/javareconf", "mimodd": "/usr/local/bin/mimodd", "mkinstalldirs": "/usr/local/bin/mkinstalldirs", "pager": "/usr/local/bin/pager", "ranlib": "/usr/local/bin/ranlib", "rtags": "/usr/local/bin/rtags", "strip": "/usr/local/bin/strip", "libtool": "/usr/local/bin/libtool", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "ncurses5-config": "/usr/local/bin/ncurses5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimodd.
shpc-registry automated BioContainers addition for mimodd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimodd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimodd:0.1.9--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimodd/0.1.9--py36_0
$ module help quay.io/biocontainers/mimodd/0.1.9--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimodd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimodd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimodd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimodd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimodd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimodd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### BATCH

```bash
$ singularity exec <container> /usr/local/bin/BATCH
$ podman run --it --rm --entrypoint /usr/local/bin/BATCH   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BATCH   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COMPILE

```bash
$ singularity exec <container> /usr/local/bin/COMPILE
$ podman run --it --rm --entrypoint /usr/local/bin/COMPILE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COMPILE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### INSTALL

```bash
$ singularity exec <container> /usr/local/bin/INSTALL
$ podman run --it --rm --entrypoint /usr/local/bin/INSTALL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/INSTALL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LINK

```bash
$ singularity exec <container> /usr/local/bin/LINK
$ podman run --it --rm --entrypoint /usr/local/bin/LINK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### REMOVE

```bash
$ singularity exec <container> /usr/local/bin/REMOVE
$ podman run --it --rm --entrypoint /usr/local/bin/REMOVE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REMOVE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rcmd

```bash
$ singularity exec <container> /usr/local/bin/Rcmd
$ podman run --it --rm --entrypoint /usr/local/bin/Rcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rd2pdf

```bash
$ singularity exec <container> /usr/local/bin/Rd2pdf
$ podman run --it --rm --entrypoint /usr/local/bin/Rd2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rd2pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rdconv

```bash
$ singularity exec <container> /usr/local/bin/Rdconv
$ podman run --it --rm --entrypoint /usr/local/bin/Rdconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rdconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rdiff

```bash
$ singularity exec <container> /usr/local/bin/Rdiff
$ podman run --it --rm --entrypoint /usr/local/bin/Rdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rprof

```bash
$ singularity exec <container> /usr/local/bin/Rprof
$ podman run --it --rm --entrypoint /usr/local/bin/Rprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SHLIB

```bash
$ singularity exec <container> /usr/local/bin/SHLIB
$ podman run --it --rm --entrypoint /usr/local/bin/SHLIB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHLIB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Stangle

```bash
$ singularity exec <container> /usr/local/bin/Stangle
$ podman run --it --rm --entrypoint /usr/local/bin/Stangle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Stangle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Sweave

```bash
$ singularity exec <container> /usr/local/bin/Sweave
$ podman run --it --rm --entrypoint /usr/local/bin/Sweave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Sweave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ar

```bash
$ singularity exec <container> /usr/local/bin/ar
$ podman run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build

```bash
$ singularity exec <container> /usr/local/bin/build
$ podman run --it --rm --entrypoint /usr/local/bin/build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c++

```bash
$ singularity exec <container> /usr/local/bin/c++
$ podman run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cc

```bash
$ singularity exec <container> /usr/local/bin/cc
$ podman run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check

```bash
$ singularity exec <container> /usr/local/bin/check
$ podman run --it --rm --entrypoint /usr/local/bin/check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config

```bash
$ singularity exec <container> /usr/local/bin/config
$ podman run --it --rm --entrypoint /usr/local/bin/config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f77

```bash
$ singularity exec <container> /usr/local/bin/f77
$ podman run --it --rm --entrypoint /usr/local/bin/f77   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f77   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f77_f2c

```bash
$ singularity exec <container> /usr/local/bin/f77_f2c
$ podman run --it --rm --entrypoint /usr/local/bin/f77_f2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f77_f2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc

```bash
$ singularity exec <container> /usr/local/bin/fc
$ podman run --it --rm --entrypoint /usr/local/bin/fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gfortran

```bash
$ singularity exec <container> /usr/local/bin/gfortran
$ podman run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javareconf

```bash
$ singularity exec <container> /usr/local/bin/javareconf
$ podman run --it --rm --entrypoint /usr/local/bin/javareconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javareconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimodd

```bash
$ singularity exec <container> /usr/local/bin/mimodd
$ podman run --it --rm --entrypoint /usr/local/bin/mimodd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimodd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkinstalldirs

```bash
$ singularity exec <container> /usr/local/bin/mkinstalldirs
$ podman run --it --rm --entrypoint /usr/local/bin/mkinstalldirs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkinstalldirs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pager

```bash
$ singularity exec <container> /usr/local/bin/pager
$ podman run --it --rm --entrypoint /usr/local/bin/pager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rtags

```bash
$ singularity exec <container> /usr/local/bin/rtags
$ podman run --it --rm --entrypoint /usr/local/bin/rtags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rtags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip

```bash
$ singularity exec <container> /usr/local/bin/strip
$ podman run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libtool

```bash
$ singularity exec <container> /usr/local/bin/libtool
$ podman run --it --rm --entrypoint /usr/local/bin/libtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libtool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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