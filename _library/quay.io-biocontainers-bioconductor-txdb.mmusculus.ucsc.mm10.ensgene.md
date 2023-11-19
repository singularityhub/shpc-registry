---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/container.yaml"
updated_at: "2023-11-19 02:52:49.300254"
latest: "3.4.0--r43hdfd78af_16"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
aliases:
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.0--r40_9"
 - "3.4.0--r42hdfd78af_15"
 - "3.4.0--r43hdfd78af_16"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "latest": {"3.4.0--r43hdfd78af_16": "sha256:88a689bd3f6213fed957d2a6b1c5933d520c11f0c2c55f5d4d0b4be66329b5a0"}, "tags": {"3.4.0--r40_9": "sha256:b87d48cf341dba877002e1d819a519170e1e2163597a24fd8e380ee0035579e2", "3.4.0--r42hdfd78af_15": "sha256:e54522e15920c9a6740f3b89e1dd5c2154b12b0f6a194e29d510b08a7d87c252", "3.4.0--r43hdfd78af_16": "sha256:88a689bd3f6213fed957d2a6b1c5933d520c11f0c2c55f5d4d0b4be66329b5a0"}, "docker": "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene:3.4.0--r43hdfd78af_16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/3.4.0--r43hdfd78af_16
$ module help quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/3.4.0--r43hdfd78af_16
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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