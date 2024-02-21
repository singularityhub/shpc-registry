---
layout: container
name:  "quay.io/biocontainers/bioconductor-peco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-peco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-peco/container.yaml"
updated_at: "2024-02-21 02:36:02.180587"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-peco"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-peco"
config: {"url": "https://biocontainers.pro/tools/bioconductor-peco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-peco", "latest": {"1.14.0--r43hdfd78af_0": "sha256:1094a9930d2d3ee906a8397c490e4c1ebd75c3f57cc89966518f021afb663edc"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:523cc450c5135d2cc361c92104818d8a9df868027da937c41292eb01db9971eb", "1.10.0--r42hdfd78af_0": "sha256:d0b78aff4e7c823e717a7178988c62290d59f653a2c64352687bcadf92751b6d", "1.12.0--r43hdfd78af_0": "sha256:6735bfe4ee12024bd188291423908251d73f8e8eaa61ef3624454c27dbab21cf", "1.14.0--r43hdfd78af_0": "sha256:1094a9930d2d3ee906a8397c490e4c1ebd75c3f57cc89966518f021afb663edc"}, "docker": "quay.io/biocontainers/bioconductor-peco"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-peco.
shpc-registry automated BioContainers addition for bioconductor-peco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-peco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-peco:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-peco/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-peco/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-peco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-peco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-peco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-peco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-peco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-peco

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