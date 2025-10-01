---
layout: container
name:  "quay.io/biocontainers/bioconductor-moanin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moanin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moanin/container.yaml"
updated_at: "2025-10-01 03:45:47.015034"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-moanin"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-moanin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moanin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moanin", "latest": {"1.14.0--r44hdfd78af_0": "sha256:b61406fcf6d4c0449396137c9380349e432ddc5c0d669c741ce9443f4a7716b3"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ed68b2dee171c0000ebdfa672d2b57d6700e2a002801b2034fd738a79c3534e5", "1.6.0--r42hdfd78af_0": "sha256:a074f22bfb1fea4cb395a7fcdf4699306efa7e3c243c40606c78fde61a0bf6a2", "1.8.0--r43hdfd78af_0": "sha256:bc2709412de791961b751f873da2929b11ba183665703ab43d45bf805c95813e", "1.10.0--r43hdfd78af_0": "sha256:5699d5e2cf21f2fccfc9f5c80fd0ae4a1d6ef8cac5c6d6820f018f31b5c87088", "1.14.0--r44hdfd78af_0": "sha256:b61406fcf6d4c0449396137c9380349e432ddc5c0d669c741ce9443f4a7716b3"}, "docker": "quay.io/biocontainers/bioconductor-moanin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moanin.
shpc-registry automated BioContainers addition for bioconductor-moanin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moanin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moanin:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moanin/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-moanin/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moanin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moanin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moanin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moanin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moanin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moanin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moanin

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