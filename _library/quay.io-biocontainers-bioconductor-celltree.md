---
layout: container
name:  "quay.io/biocontainers/bioconductor-celltree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celltree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celltree/container.yaml"
updated_at: "2024-09-22 02:58:19.900425"
latest: "1.27.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-celltree"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.27.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-celltree"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celltree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celltree", "latest": {"1.27.0--r42hdfd78af_0": "sha256:c0eea47358204385e375a697f84b710e8bac68819a9272e41ddc10066ad4b521"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:21d453fb3e2a0d6ae475da095563a7054216865f9adc0d2ddd5a31814af313af", "1.27.0--r42hdfd78af_0": "sha256:c0eea47358204385e375a697f84b710e8bac68819a9272e41ddc10066ad4b521"}, "docker": "quay.io/biocontainers/bioconductor-celltree"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celltree.
shpc-registry automated BioContainers addition for bioconductor-celltree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celltree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celltree:1.27.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celltree/1.27.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-celltree/1.27.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celltree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celltree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celltree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celltree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celltree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celltree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-celltree

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