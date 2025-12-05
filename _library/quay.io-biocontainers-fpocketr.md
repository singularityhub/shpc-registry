---
layout: container
name:  "quay.io/biocontainers/fpocketr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fpocketr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fpocketr/container.yaml"
updated_at: "2025-12-05 03:21:35.116941"
latest: "1.3.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fpocketr"
aliases:
 - "dpocket"
 - "evol"
 - "fpocket"
 - "glewinfo"
 - "mdpocket"
 - "prody"
 - "pymol"
 - "tpocket"
 - "visualinfo"
 - "pax11publish"
 - "h5fuse"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "balsam"
 - "lprodump"
 - "lrelease-pro"
 - "lupdate-pro"
 - "meshdebug"
 - "qmlformat"
 - "qmltime"
 - "qmltyperegistrar"
 - "tracegen"
 - "lame"
versions:
 - "1.3.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for fpocketr"
config: {"url": "https://biocontainers.pro/tools/fpocketr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fpocketr", "latest": {"1.3.4--pyhdfd78af_0": "sha256:503c2577e810c91c75f9a96cf50fe6dccb11b3dd0a058b4d2e4f1ab08b54c4c4"}, "tags": {"1.3.4--pyhdfd78af_0": "sha256:503c2577e810c91c75f9a96cf50fe6dccb11b3dd0a058b4d2e4f1ab08b54c4c4"}, "docker": "quay.io/biocontainers/fpocketr", "aliases": {"dpocket": "/usr/local/bin/dpocket", "evol": "/usr/local/bin/evol", "fpocket": "/usr/local/bin/fpocket", "glewinfo": "/usr/local/bin/glewinfo", "mdpocket": "/usr/local/bin/mdpocket", "prody": "/usr/local/bin/prody", "pymol": "/usr/local/bin/pymol", "tpocket": "/usr/local/bin/tpocket", "visualinfo": "/usr/local/bin/visualinfo", "pax11publish": "/usr/local/bin/pax11publish", "h5fuse": "/usr/local/bin/h5fuse", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "balsam": "/usr/local/bin/balsam", "lprodump": "/usr/local/bin/lprodump", "lrelease-pro": "/usr/local/bin/lrelease-pro", "lupdate-pro": "/usr/local/bin/lupdate-pro", "meshdebug": "/usr/local/bin/meshdebug", "qmlformat": "/usr/local/bin/qmlformat", "qmltime": "/usr/local/bin/qmltime", "qmltyperegistrar": "/usr/local/bin/qmltyperegistrar", "tracegen": "/usr/local/bin/tracegen", "lame": "/usr/local/bin/lame"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fpocketr.
singularity registry hpc automated addition for fpocketr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fpocketr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fpocketr:1.3.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fpocketr/1.3.4--pyhdfd78af_0
$ module help quay.io/biocontainers/fpocketr/1.3.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fpocketr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fpocketr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fpocketr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fpocketr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fpocketr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fpocketr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dpocket

```bash
$ singularity exec <container> /usr/local/bin/dpocket
$ podman run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evol

```bash
$ singularity exec <container> /usr/local/bin/evol
$ podman run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fpocket

```bash
$ singularity exec <container> /usr/local/bin/fpocket
$ podman run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glewinfo

```bash
$ singularity exec <container> /usr/local/bin/glewinfo
$ podman run --it --rm --entrypoint /usr/local/bin/glewinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glewinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mdpocket

```bash
$ singularity exec <container> /usr/local/bin/mdpocket
$ podman run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prody

```bash
$ singularity exec <container> /usr/local/bin/prody
$ podman run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pymol

```bash
$ singularity exec <container> /usr/local/bin/pymol
$ podman run --it --rm --entrypoint /usr/local/bin/pymol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pymol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpocket

```bash
$ singularity exec <container> /usr/local/bin/tpocket
$ podman run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpocket   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### visualinfo

```bash
$ singularity exec <container> /usr/local/bin/visualinfo
$ podman run --it --rm --entrypoint /usr/local/bin/visualinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/visualinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse

```bash
$ singularity exec <container> /usr/local/bin/h5fuse
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### meshdebug

```bash
$ singularity exec <container> /usr/local/bin/meshdebug
$ podman run --it --rm --entrypoint /usr/local/bin/meshdebug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meshdebug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlformat

```bash
$ singularity exec <container> /usr/local/bin/qmlformat
$ podman run --it --rm --entrypoint /usr/local/bin/qmlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmltime

```bash
$ singularity exec <container> /usr/local/bin/qmltime
$ podman run --it --rm --entrypoint /usr/local/bin/qmltime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmltime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmltyperegistrar

```bash
$ singularity exec <container> /usr/local/bin/qmltyperegistrar
$ podman run --it --rm --entrypoint /usr/local/bin/qmltyperegistrar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmltyperegistrar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tracegen

```bash
$ singularity exec <container> /usr/local/bin/tracegen
$ podman run --it --rm --entrypoint /usr/local/bin/tracegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lame

```bash
$ singularity exec <container> /usr/local/bin/lame
$ podman run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lame   -v ${PWD} -w ${PWD} <container> -c " $@"
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