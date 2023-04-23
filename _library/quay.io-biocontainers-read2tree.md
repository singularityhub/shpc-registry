---
layout: container
name:  "quay.io/biocontainers/read2tree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/read2tree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/read2tree/container.yaml"
updated_at: "2023-04-23 02:49:30.277782"
latest: "0.1.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/read2tree"
aliases:
 - "addr2line"
 - "ar"
 - "as"
 - "c++filt"
 - "dwp"
 - "elfedit"
 - "gold"
 - "gprof"
 - "ld"
 - "ld.bfd"
 - "ld.gold"
 - "ngm"
 - "ngm-core"
 - "ngm-core-debug"
 - "ngm-debug"
 - "ngm-log"
 - "ngm-utils"
 - "ngm-utils-debug"
 - "ngmlr"
 - "nm"
 - "objcopy"
 - "objdump"
 - "oclTool"
 - "ranlib"
 - "read2tree"
 - "readelf"
 - "size"
 - "strings"
 - "strip"
 - "iqtree2"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "orc-bugreport"
 - "orcc"
 - "out123"
 - "dumpsexp"
 - "gpg-error"
 - "gpgrt-config"
 - "hmac256"
 - "libgcrypt-config"
 - "mpicalc"
 - "yat2m"
 - "lame"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "iqtree"
 - "attr"
 - "balsam"
 - "getfattr"
versions:
 - "0.1.5--pyhdfd78af_0"
description: "singularity registry hpc automated addition for read2tree"
config: {"url": "https://biocontainers.pro/tools/read2tree", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for read2tree", "latest": {"0.1.5--pyhdfd78af_0": "sha256:520ae6ed6afc8aed321810e0edfc3b15861584d41722bae9db2d1f5721088066"}, "tags": {"0.1.5--pyhdfd78af_0": "sha256:520ae6ed6afc8aed321810e0edfc3b15861584d41722bae9db2d1f5721088066"}, "docker": "quay.io/biocontainers/read2tree", "aliases": {"addr2line": "/usr/local/bin/addr2line", "ar": "/usr/local/bin/ar", "as": "/usr/local/bin/as", "c++filt": "/usr/local/bin/c++filt", "dwp": "/usr/local/bin/dwp", "elfedit": "/usr/local/bin/elfedit", "gold": "/usr/local/bin/gold", "gprof": "/usr/local/bin/gprof", "ld": "/usr/local/bin/ld", "ld.bfd": "/usr/local/bin/ld.bfd", "ld.gold": "/usr/local/bin/ld.gold", "ngm": "/usr/local/bin/ngm", "ngm-core": "/usr/local/bin/ngm-core", "ngm-core-debug": "/usr/local/bin/ngm-core-debug", "ngm-debug": "/usr/local/bin/ngm-debug", "ngm-log": "/usr/local/bin/ngm-log", "ngm-utils": "/usr/local/bin/ngm-utils", "ngm-utils-debug": "/usr/local/bin/ngm-utils-debug", "ngmlr": "/usr/local/bin/ngmlr", "nm": "/usr/local/bin/nm", "objcopy": "/usr/local/bin/objcopy", "objdump": "/usr/local/bin/objdump", "oclTool": "/usr/local/bin/oclTool", "ranlib": "/usr/local/bin/ranlib", "read2tree": "/usr/local/bin/read2tree", "readelf": "/usr/local/bin/readelf", "size": "/usr/local/bin/size", "strings": "/usr/local/bin/strings", "strip": "/usr/local/bin/strip", "iqtree2": "/usr/local/bin/iqtree2", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "orc-bugreport": "/usr/local/bin/orc-bugreport", "orcc": "/usr/local/bin/orcc", "out123": "/usr/local/bin/out123", "dumpsexp": "/usr/local/bin/dumpsexp", "gpg-error": "/usr/local/bin/gpg-error", "gpgrt-config": "/usr/local/bin/gpgrt-config", "hmac256": "/usr/local/bin/hmac256", "libgcrypt-config": "/usr/local/bin/libgcrypt-config", "mpicalc": "/usr/local/bin/mpicalc", "yat2m": "/usr/local/bin/yat2m", "lame": "/usr/local/bin/lame", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "iqtree": "/usr/local/bin/iqtree", "attr": "/usr/local/bin/attr", "balsam": "/usr/local/bin/balsam", "getfattr": "/usr/local/bin/getfattr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/read2tree.
singularity registry hpc automated addition for read2tree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/read2tree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/read2tree:0.1.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/read2tree/0.1.5--pyhdfd78af_0
$ module help quay.io/biocontainers/read2tree/0.1.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### read2tree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### read2tree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### read2tree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### read2tree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### read2tree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### read2tree-inspect-deffile:

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


#### c++filt

```bash
$ singularity exec <container> /usr/local/bin/c++filt
$ podman run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++filt   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ngm

```bash
$ singularity exec <container> /usr/local/bin/ngm
$ podman run --it --rm --entrypoint /usr/local/bin/ngm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-core

```bash
$ singularity exec <container> /usr/local/bin/ngm-core
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-core-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-core-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-core-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-core-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-log

```bash
$ singularity exec <container> /usr/local/bin/ngm-log
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-utils

```bash
$ singularity exec <container> /usr/local/bin/ngm-utils
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngm-utils-debug

```bash
$ singularity exec <container> /usr/local/bin/ngm-utils-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ngm-utils-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngm-utils-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngmlr

```bash
$ singularity exec <container> /usr/local/bin/ngmlr
$ podman run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngmlr   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### oclTool

```bash
$ singularity exec <container> /usr/local/bin/oclTool
$ podman run --it --rm --entrypoint /usr/local/bin/oclTool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oclTool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ranlib

```bash
$ singularity exec <container> /usr/local/bin/ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read2tree

```bash
$ singularity exec <container> /usr/local/bin/read2tree
$ podman run --it --rm --entrypoint /usr/local/bin/read2tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read2tree   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123

```bash
$ singularity exec <container> /usr/local/bin/mpg123
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-id3dump

```bash
$ singularity exec <container> /usr/local/bin/mpg123-id3dump
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-id3dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpg123-strip

```bash
$ singularity exec <container> /usr/local/bin/mpg123-strip
$ podman run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpg123-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-bugreport

```bash
$ singularity exec <container> /usr/local/bin/orc-bugreport
$ podman run --it --rm --entrypoint /usr/local/bin/orc-bugreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-bugreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orcc

```bash
$ singularity exec <container> /usr/local/bin/orcc
$ podman run --it --rm --entrypoint /usr/local/bin/orcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### out123

```bash
$ singularity exec <container> /usr/local/bin/out123
$ podman run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/out123   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsexp

```bash
$ singularity exec <container> /usr/local/bin/dumpsexp
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsexp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpg-error

```bash
$ singularity exec <container> /usr/local/bin/gpg-error
$ podman run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpg-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpgrt-config

```bash
$ singularity exec <container> /usr/local/bin/gpgrt-config
$ podman run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpgrt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmac256

```bash
$ singularity exec <container> /usr/local/bin/hmac256
$ podman run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmac256   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libgcrypt-config

```bash
$ singularity exec <container> /usr/local/bin/libgcrypt-config
$ podman run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libgcrypt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicalc

```bash
$ singularity exec <container> /usr/local/bin/mpicalc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicalc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yat2m

```bash
$ singularity exec <container> /usr/local/bin/yat2m
$ podman run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yat2m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-build

```bash
$ singularity exec <container> /usr/local/bin/sip-build
$ podman run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-distinfo

```bash
$ singularity exec <container> /usr/local/bin/sip-distinfo
$ podman run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-distinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-install

```bash
$ singularity exec <container> /usr/local/bin/sip-install
$ podman run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-module

```bash
$ singularity exec <container> /usr/local/bin/sip-module
$ podman run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-module   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-sdist

```bash
$ singularity exec <container> /usr/local/bin/sip-sdist
$ podman run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-sdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip-wheel

```bash
$ singularity exec <container> /usr/local/bin/sip-wheel
$ podman run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip-wheel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### balsam

```bash
$ singularity exec <container> /usr/local/bin/balsam
$ podman run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfattr

```bash
$ singularity exec <container> /usr/local/bin/getfattr
$ podman run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
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