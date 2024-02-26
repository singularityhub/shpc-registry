---
layout: container
name:  "quay.io/biocontainers/bioconductor-alpine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alpine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alpine/container.yaml"
updated_at: "2024-02-26 04:06:09.065315"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-alpine"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-alpine"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alpine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-alpine", "latest": {"1.26.0--r43hdfd78af_0": "sha256:6cb365c9ec5b4e2dd8005a8b7e48aafab46ec21985d7b9a4b51082cf9053d427"}, "tags": {"1.8.0--r351_0": "sha256:9212aa3f4ae2bd4d0fed165be35f8f6b0e34342e292be37fac83ae3973754986", "1.20.0--r41hdfd78af_0": "sha256:cb95249b77099507bad72c451f1dccb2e3e8b482a8b5463fa6c9b286a58b2ec1", "1.18.0--r41hdfd78af_0": "sha256:8162f4ff472c5d8a6f8b11bf4b9e04fc82e358b5a1efba6db12230451880a03e", "1.16.0--r40hdfd78af_1": "sha256:b388fdea35b569ffd630e759689a73aa9f03c664da50396bfcf0d5936c397aa5", "1.14.0--r40_0": "sha256:6f15dace71200e034d0f8377a14946f727fbe149059a6d34d78f91588eab596f", "1.12.0--r36_0": "sha256:5d2fd30c2fa6d5b9a281774ce96474eab83a6173c70ee64e3e12c8d19fb9154e", "1.24.0--r42hdfd78af_0": "sha256:545798eaf816365e9bc4d5890ff98d9e566721a8d8049441de39c53ba08466ea", "1.26.0--r43hdfd78af_0": "sha256:6cb365c9ec5b4e2dd8005a8b7e48aafab46ec21985d7b9a4b51082cf9053d427"}, "docker": "quay.io/biocontainers/bioconductor-alpine", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alpine.
shpc-registry automated BioContainers addition for bioconductor-alpine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alpine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alpine:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alpine/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-alpine/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alpine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alpine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alpine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alpine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alpine-inspect-deffile:

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