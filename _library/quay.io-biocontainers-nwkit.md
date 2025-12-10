---
layout: container
name:  "quay.io/biocontainers/nwkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nwkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nwkit/container.yaml"
updated_at: "2025-12-10 04:07:05.162857"
latest: "0.18.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nwkit"
aliases:
 - "nwkit"
 - "pax11publish"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "mpg123"
 - "mpg123-id3dump"
 - "mpg123-strip"
 - "out123"
 - "sip-build"
 - "sip-distinfo"
 - "sip-install"
 - "sip-module"
 - "sip-sdist"
 - "sip-wheel"
 - "balsam"
versions:
 - "0.17.2--pyhdfd78af_0"
 - "0.18.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for nwkit"
config: {"url": "https://biocontainers.pro/tools/nwkit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nwkit", "latest": {"0.18.2--pyhdfd78af_0": "sha256:3f8e848459ad6a8a362176b7cce2a4289a488d115cce0c559ce8dac9dff1494e"}, "tags": {"0.17.2--pyhdfd78af_0": "sha256:3422279958d34579db0306d8c4a7738234ad2bb802dc54ce8e71cad01dea7a45", "0.18.2--pyhdfd78af_0": "sha256:3f8e848459ad6a8a362176b7cce2a4289a488d115cce0c559ce8dac9dff1494e"}, "docker": "quay.io/biocontainers/nwkit", "aliases": {"nwkit": "/usr/local/bin/nwkit", "pax11publish": "/usr/local/bin/pax11publish", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump", "mpg123-strip": "/usr/local/bin/mpg123-strip", "out123": "/usr/local/bin/out123", "sip-build": "/usr/local/bin/sip-build", "sip-distinfo": "/usr/local/bin/sip-distinfo", "sip-install": "/usr/local/bin/sip-install", "sip-module": "/usr/local/bin/sip-module", "sip-sdist": "/usr/local/bin/sip-sdist", "sip-wheel": "/usr/local/bin/sip-wheel", "balsam": "/usr/local/bin/balsam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nwkit.
singularity registry hpc automated addition for nwkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nwkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nwkit:0.18.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nwkit/0.18.2--pyhdfd78af_0
$ module help quay.io/biocontainers/nwkit/0.18.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nwkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nwkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nwkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nwkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nwkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nwkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nwkit

```bash
$ singularity exec <container> /usr/local/bin/nwkit
$ podman run --it --rm --entrypoint /usr/local/bin/nwkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nwkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
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