---
layout: container
name:  "quay.io/biocontainers/treesimulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treesimulator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treesimulator/container.yaml"
updated_at: "2024-11-10 03:13:07.902328"
latest: "0.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/treesimulator"
aliases:
 - "generate_bd"
 - "generate_bdei"
 - "generate_bdss"
 - "generate_mtbd"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "numpy-config"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "dumpsexp"
 - "gpg-error"
 - "gpgrt-config"
 - "hmac256"
 - "mpicalc"
 - "yat2m"
 - "lame"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "balsam"
 - "lprodump"
 - "lrelease-pro"
 - "lupdate-pro"
versions:
 - "0.1.22--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for treesimulator"
config: {"url": "https://biocontainers.pro/tools/treesimulator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for treesimulator", "latest": {"0.2.0--pyhdfd78af_0": "sha256:48114eb2a2954aef5f2d3dbb61eea4d2339e85dea86ec7129f88b21764d1d000"}, "tags": {"0.1.22--pyhdfd78af_0": "sha256:43f049c1076003511d187cae582f0714791580276e17f026d82c22a70db85b55", "0.2.0--pyhdfd78af_0": "sha256:48114eb2a2954aef5f2d3dbb61eea4d2339e85dea86ec7129f88b21764d1d000"}, "docker": "quay.io/biocontainers/treesimulator", "aliases": {"generate_bd": "/usr/local/bin/generate_bd", "generate_bdei": "/usr/local/bin/generate_bdei", "generate_bdss": "/usr/local/bin/generate_bdss", "generate_mtbd": "/usr/local/bin/generate_mtbd", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "numpy-config": "/usr/local/bin/numpy-config", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "dumpsexp": "/usr/local/bin/dumpsexp", "gpg-error": "/usr/local/bin/gpg-error", "gpgrt-config": "/usr/local/bin/gpgrt-config", "hmac256": "/usr/local/bin/hmac256", "mpicalc": "/usr/local/bin/mpicalc", "yat2m": "/usr/local/bin/yat2m", "lame": "/usr/local/bin/lame", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "balsam": "/usr/local/bin/balsam", "lprodump": "/usr/local/bin/lprodump", "lrelease-pro": "/usr/local/bin/lrelease-pro", "lupdate-pro": "/usr/local/bin/lupdate-pro"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treesimulator.
singularity registry hpc automated addition for treesimulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treesimulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treesimulator:0.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treesimulator/0.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/treesimulator/0.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treesimulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treesimulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treesimulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treesimulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treesimulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treesimulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### generate_bd

```bash
$ singularity exec <container> /usr/local/bin/generate_bd
$ podman run --it --rm --entrypoint /usr/local/bin/generate_bd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_bd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_bdei

```bash
$ singularity exec <container> /usr/local/bin/generate_bdei
$ podman run --it --rm --entrypoint /usr/local/bin/generate_bdei   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_bdei   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_bdss

```bash
$ singularity exec <container> /usr/local/bin/generate_bdss
$ podman run --it --rm --entrypoint /usr/local/bin/generate_bdss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_bdss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_mtbd

```bash
$ singularity exec <container> /usr/local/bin/generate_mtbd
$ podman run --it --rm --entrypoint /usr/local/bin/generate_mtbd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_mtbd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### balsam

```bash
$ singularity exec <container> /usr/local/bin/balsam
$ podman run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lprodump

```bash
$ singularity exec <container> /usr/local/bin/lprodump
$ podman run --it --rm --entrypoint /usr/local/bin/lprodump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lprodump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-pro

```bash
$ singularity exec <container> /usr/local/bin/lrelease-pro
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-pro

```bash
$ singularity exec <container> /usr/local/bin/lupdate-pro
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-pro   -v ${PWD} -w ${PWD} <container> -c " $@"
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