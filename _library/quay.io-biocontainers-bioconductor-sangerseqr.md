---
layout: container
name:  "quay.io/biocontainers/bioconductor-sangerseqr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sangerseqr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sangerseqr/container.yaml"
updated_at: "2025-08-27 03:28:20.449805"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sangerseqr"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sangerseqr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sangerseqr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sangerseqr", "latest": {"1.42.0--r44hdfd78af_0": "sha256:769a6a686a2b251cdfa0d0058ad418a074b1eabb17301794cae78d51ebd10c82"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:d7d4932edb46891beb08818f539725f8989f30dfcc757e0d48e35da03b17e975", "1.34.0--r42hdfd78af_0": "sha256:7f4b0936015e75b025873391a73b02f3a149d5c3826106d96713ad20fee3742a", "1.36.0--r43hdfd78af_0": "sha256:5c0f41ecba23e5e6caaf0e874b1eed678b0345ccc839a3e15e26f56514fc3c65", "1.38.0--r43hdfd78af_0": "sha256:4efee0e959f0dbd89ef5f36d9ca8ae029212b37edae05c2f4e497647b7e318fa", "1.42.0--r44hdfd78af_0": "sha256:769a6a686a2b251cdfa0d0058ad418a074b1eabb17301794cae78d51ebd10c82"}, "docker": "quay.io/biocontainers/bioconductor-sangerseqr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sangerseqr.
shpc-registry automated BioContainers addition for bioconductor-sangerseqr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sangerseqr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sangerseqr:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sangerseqr/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sangerseqr/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sangerseqr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sangerseqr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sangerseqr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sangerseqr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sangerseqr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sangerseqr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sangerseqr

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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