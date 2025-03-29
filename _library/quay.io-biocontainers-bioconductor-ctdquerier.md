---
layout: container
name:  "quay.io/biocontainers/bioconductor-ctdquerier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ctdquerier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ctdquerier/container.yaml"
updated_at: "2025-03-29 03:37:34.820199"
latest: "2.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ctdquerier"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ctdquerier"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ctdquerier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ctdquerier", "latest": {"2.14.0--r44hdfd78af_0": "sha256:58616f3c1d647b31191ecb63ec064a48ec1202bc24f7f4645e13e4889cb890d5"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:c82030c544b75dfcf60e0cdd1e4e25d4a9e7df8f230338c44ebb70f07478ff3d", "2.6.0--r42hdfd78af_0": "sha256:401648dcc906e3fceb4cde2f731529ffffbbb0b542a61b4d1d5df54ae6c9e152", "2.8.0--r43hdfd78af_0": "sha256:0ffe468d6765763b1ce77978f59d65ee0b834d94edaafb92237ce8a66d0d56de", "2.10.0--r43hdfd78af_0": "sha256:43d1fcafd561f03c9de2d3357bf58c6b24cfce3eb15dc52934d5b67ff8e3b0fa", "2.14.0--r44hdfd78af_0": "sha256:58616f3c1d647b31191ecb63ec064a48ec1202bc24f7f4645e13e4889cb890d5"}, "docker": "quay.io/biocontainers/bioconductor-ctdquerier"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ctdquerier.
shpc-registry automated BioContainers addition for bioconductor-ctdquerier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ctdquerier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ctdquerier:2.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ctdquerier/2.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ctdquerier/2.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ctdquerier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctdquerier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ctdquerier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ctdquerier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ctdquerier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ctdquerier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ctdquerier

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