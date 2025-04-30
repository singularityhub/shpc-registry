---
layout: container
name:  "quay.io/biocontainers/bioconductor-quartpac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-quartpac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-quartpac/container.yaml"
updated_at: "2025-04-30 03:37:04.908699"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-quartpac"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-quartpac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-quartpac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-quartpac", "latest": {"1.34.0--r43hdfd78af_0": "sha256:32762813df96c42755b821ec13c1ef627c82c12245588f6c5cc6200c1e922d5b"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:fc5f85102f8a9bae6af403d0879410ae7ae426d9551304717918ecf453fc7b27", "1.30.0--r42hdfd78af_0": "sha256:6b1bcce8a513d07fb132a3d50b4f41d64c092b718d07a56a9abc41d2267e4afd", "1.32.0--r43hdfd78af_0": "sha256:349f4dfce8834fd8b2157b197670c333a2e94cd73986e461530cf602a1e56990", "1.34.0--r43hdfd78af_0": "sha256:32762813df96c42755b821ec13c1ef627c82c12245588f6c5cc6200c1e922d5b"}, "docker": "quay.io/biocontainers/bioconductor-quartpac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-quartpac.
shpc-registry automated BioContainers addition for bioconductor-quartpac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-quartpac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-quartpac:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-quartpac/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-quartpac/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-quartpac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quartpac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quartpac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-quartpac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-quartpac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-quartpac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-quartpac

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