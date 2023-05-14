---
layout: container
name:  "quay.io/biocontainers/bioconductor-organism.dplyr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-organism.dplyr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-organism.dplyr/container.yaml"
updated_at: "2023-05-14 02:42:28.406078"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-organism.dplyr"

versions:
 - "1.22.1--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-organism.dplyr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-organism.dplyr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-organism.dplyr", "latest": {"1.26.0--r42hdfd78af_0": "sha256:758dfbef9ef97cdc251dd4c1da56cd8016cffc6d9e6b333a4e37be2500b8692e"}, "tags": {"1.22.1--r41hdfd78af_0": "sha256:3bcf9341dfdab449e4b2b56d69248e069c9ddb0b03f96ad58738bc47a52a52d8", "1.26.0--r42hdfd78af_0": "sha256:758dfbef9ef97cdc251dd4c1da56cd8016cffc6d9e6b333a4e37be2500b8692e"}, "docker": "quay.io/biocontainers/bioconductor-organism.dplyr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-organism.dplyr.
shpc-registry automated BioContainers addition for bioconductor-organism.dplyr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-organism.dplyr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-organism.dplyr:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-organism.dplyr/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-organism.dplyr/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-organism.dplyr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-organism.dplyr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-organism.dplyr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-organism.dplyr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-organism.dplyr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-organism.dplyr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-organism.dplyr

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