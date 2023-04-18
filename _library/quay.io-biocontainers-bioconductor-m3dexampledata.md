---
layout: container
name:  "quay.io/biocontainers/bioconductor-m3dexampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-m3dexampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-m3dexampledata/container.yaml"
updated_at: "2023-04-18 02:40:04.592036"
latest: "1.23.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-m3dexampledata"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.23.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.15.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-m3dexampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-m3dexampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-m3dexampledata", "latest": {"1.23.0--r42hdfd78af_0": "sha256:deb62c9096695b4da3a2f5e4058dc91afe974a6ec75d9279984cc17e5d6abc36"}, "tags": {"1.8.0--r351_0": "sha256:16ff7737d39ddf81fbc953466f1d89a6433da3c3612423cce714623081047c8c", "1.23.0--r42hdfd78af_0": "sha256:deb62c9096695b4da3a2f5e4058dc91afe974a6ec75d9279984cc17e5d6abc36", "1.20.0--r41hdfd78af_1": "sha256:07bff37a77e8ad69bb0b4b1c883bfb8e05128b559a7ecbabcc2b0b3646870971", "1.18.0--r41hdfd78af_0": "sha256:ab147bb68ac236ebb7df86855dab10ed1154bd0360ab674fd132466ef086655e", "1.16.0--r40hdfd78af_1": "sha256:5862906493beae10770b77ed7b7507f7c076e77937ec6c6a32246483579d48a1", "1.15.0--r40_0": "sha256:0a375fda4617cd016a9a81070c1df07e38a32c690798fad4fd3a408a19fd36a2"}, "docker": "quay.io/biocontainers/bioconductor-m3dexampledata", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-m3dexampledata.
shpc-registry automated BioContainers addition for bioconductor-m3dexampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-m3dexampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-m3dexampledata:1.23.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-m3dexampledata/1.23.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-m3dexampledata/1.23.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-m3dexampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m3dexampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m3dexampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-m3dexampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-m3dexampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-m3dexampledata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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