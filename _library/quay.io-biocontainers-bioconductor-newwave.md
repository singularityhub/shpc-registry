---
layout: container
name:  "quay.io/biocontainers/bioconductor-newwave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-newwave/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-newwave/container.yaml"
updated_at: "2024-06-16 02:48:51.578557"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-newwave"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-newwave"
config: {"url": "https://biocontainers.pro/tools/bioconductor-newwave", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-newwave", "latest": {"1.12.0--r43hdfd78af_0": "sha256:82412784ab953a721cf30fd7cca0a50e1c4666f5fcbbd2aca818b20b0ac6a321"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:1814d07d9c6542df3b36da69bc8943cc2c87d8f3569dc15ffaf7212b3f16898a", "1.8.0--r42hdfd78af_0": "sha256:cc7a8d4e697560a3780c3417b6c66c5d1e95a6bd2bc91eb6c72a8e53efa2d321", "1.12.0--r43hdfd78af_0": "sha256:82412784ab953a721cf30fd7cca0a50e1c4666f5fcbbd2aca818b20b0ac6a321"}, "docker": "quay.io/biocontainers/bioconductor-newwave"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-newwave.
shpc-registry automated BioContainers addition for bioconductor-newwave
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-newwave
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-newwave:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-newwave/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-newwave/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-newwave-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-newwave-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-newwave-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-newwave-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-newwave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-newwave-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-newwave

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