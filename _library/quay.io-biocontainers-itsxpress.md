---
layout: container
name:  "quay.io/biocontainers/itsxpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/itsxpress/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/itsxpress/container.yaml"
updated_at: "2022-10-29 05:54:51.358865"
latest: "1.8.0--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/itsxpress"
aliases:
 - "aclocal.bak"
 - "autoheader.bak"
 - "autom4te.bak"
 - "automake.bak"
 - "autoreconf.bak"
 - "autoscan.bak"
 - "autoupdate.bak"
 - "ifnames.bak"
 - "itsxpress"
 - "2to3-3.10"
 - "a_sample_mt.sh"
 - "ace2sam"
 - "addadapters.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "alimask"
 - "alltoall.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
versions:
 - "1.8.0--pyhdfd78af_2"
description: "shpc-registry automated BioContainers addition for itsxpress"
config: {"url": "https://biocontainers.pro/tools/itsxpress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for itsxpress", "latest": {"1.8.0--pyhdfd78af_2": "sha256:688a48b2d785bc59556d33d3520450fcd6b206d95a5034c7fb245c37d6f6838c"}, "tags": {"1.8.0--pyhdfd78af_2": "sha256:688a48b2d785bc59556d33d3520450fcd6b206d95a5034c7fb245c37d6f6838c"}, "docker": "quay.io/biocontainers/itsxpress", "aliases": {"aclocal.bak": "/usr/local/bin/aclocal.bak", "autoheader.bak": "/usr/local/bin/autoheader.bak", "autom4te.bak": "/usr/local/bin/autom4te.bak", "automake.bak": "/usr/local/bin/automake.bak", "autoreconf.bak": "/usr/local/bin/autoreconf.bak", "autoscan.bak": "/usr/local/bin/autoscan.bak", "autoupdate.bak": "/usr/local/bin/autoupdate.bak", "ifnames.bak": "/usr/local/bin/ifnames.bak", "itsxpress": "/usr/local/bin/itsxpress", "2to3-3.10": "/usr/local/bin/2to3-3.10", "a_sample_mt.sh": "/usr/local/bin/a_sample_mt.sh", "ace2sam": "/usr/local/bin/ace2sam", "addadapters.sh": "/usr/local/bin/addadapters.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "alimask": "/usr/local/bin/alimask", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/itsxpress.
shpc-registry automated BioContainers addition for itsxpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/itsxpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/itsxpress:1.8.0--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/itsxpress/1.8.0--pyhdfd78af_2
$ module help quay.io/biocontainers/itsxpress/1.8.0--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### itsxpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### itsxpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### itsxpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### itsxpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### itsxpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### itsxpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aclocal.bak

```bash
$ singularity exec <container> /usr/local/bin/aclocal.bak
$ podman run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoheader.bak

```bash
$ singularity exec <container> /usr/local/bin/autoheader.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autom4te.bak

```bash
$ singularity exec <container> /usr/local/bin/autom4te.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### automake.bak

```bash
$ singularity exec <container> /usr/local/bin/automake.bak
$ podman run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoreconf.bak

```bash
$ singularity exec <container> /usr/local/bin/autoreconf.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoreconf.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoscan.bak

```bash
$ singularity exec <container> /usr/local/bin/autoscan.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoscan.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoupdate.bak

```bash
$ singularity exec <container> /usr/local/bin/autoupdate.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoupdate.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifnames.bak

```bash
$ singularity exec <container> /usr/local/bin/ifnames.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifnames.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### itsxpress

```bash
$ singularity exec <container> /usr/local/bin/itsxpress
$ podman run --it --rm --entrypoint /usr/local/bin/itsxpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/itsxpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a_sample_mt.sh

```bash
$ singularity exec <container> /usr/local/bin/a_sample_mt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addadapters.sh

```bash
$ singularity exec <container> /usr/local/bin/addadapters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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