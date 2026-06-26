---
layout: container
name:  "quay.io/biocontainers/bubblotter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bubblotter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bubblotter/container.yaml"
updated_at: "2026-06-26 01:40:57.924476"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bubblotter"
aliases:
 - "Bandage"
 - "BubbleGun"
 - "bubblotter"
 - "fc-genconf"
 - "vg"
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
 - "hb-raster"
 - "hb-vector"
 - "balsam"
 - "lprodump"
 - "lrelease-pro"
 - "lupdate-pro"
 - "meshdebug"
 - "qmlformat"
 - "qmltime"
 - "qmltyperegistrar"
 - "tracegen"
 - "mpg123"
 - "mpg123-id3dump"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bubblotter"
config: {"url": "https://biocontainers.pro/tools/bubblotter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bubblotter", "latest": {"0.1.0--pyhdfd78af_0": "sha256:57f686ab71dd3796398c4fc8d39fc5f9bb382a9b0ad8965dd47b59684e6436d1"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:57f686ab71dd3796398c4fc8d39fc5f9bb382a9b0ad8965dd47b59684e6436d1"}, "docker": "quay.io/biocontainers/bubblotter", "aliases": {"Bandage": "/usr/local/bin/Bandage", "BubbleGun": "/usr/local/bin/BubbleGun", "bubblotter": "/usr/local/bin/bubblotter", "fc-genconf": "/usr/local/bin/fc-genconf", "vg": "/usr/local/bin/vg", "pax11publish": "/usr/local/bin/pax11publish", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "balsam": "/usr/local/bin/balsam", "lprodump": "/usr/local/bin/lprodump", "lrelease-pro": "/usr/local/bin/lrelease-pro", "lupdate-pro": "/usr/local/bin/lupdate-pro", "meshdebug": "/usr/local/bin/meshdebug", "qmlformat": "/usr/local/bin/qmlformat", "qmltime": "/usr/local/bin/qmltime", "qmltyperegistrar": "/usr/local/bin/qmltyperegistrar", "tracegen": "/usr/local/bin/tracegen", "mpg123": "/usr/local/bin/mpg123", "mpg123-id3dump": "/usr/local/bin/mpg123-id3dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bubblotter.
singularity registry hpc automated addition for bubblotter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bubblotter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bubblotter:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bubblotter/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/bubblotter/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bubblotter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bubblotter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bubblotter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bubblotter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bubblotter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bubblotter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Bandage

```bash
$ singularity exec <container> /usr/local/bin/Bandage
$ podman run --it --rm --entrypoint /usr/local/bin/Bandage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Bandage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BubbleGun

```bash
$ singularity exec <container> /usr/local/bin/BubbleGun
$ podman run --it --rm --entrypoint /usr/local/bin/BubbleGun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BubbleGun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bubblotter

```bash
$ singularity exec <container> /usr/local/bin/bubblotter
$ podman run --it --rm --entrypoint /usr/local/bin/bubblotter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bubblotter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vg

```bash
$ singularity exec <container> /usr/local/bin/vg
$ podman run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
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