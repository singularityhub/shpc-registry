---
layout: container
name:  "quay.io/biocontainers/bioconductor-bionero"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bionero/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bionero/container.yaml"
updated_at: "2023-05-02 02:50:05.182943"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bionero"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bionero"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bionero", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bionero", "latest": {"1.6.0--r42hdfd78af_0": "sha256:c6f1d14f71fd591e0c8b2f96ce3bf2d57041979f922c4268170187250776e4c9"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:c13e1bc96702ac86307f9a7e1aea50d6d4f37d1b41e3d6ce83b8823b9b3bac20", "1.6.0--r42hdfd78af_0": "sha256:c6f1d14f71fd591e0c8b2f96ce3bf2d57041979f922c4268170187250776e4c9"}, "docker": "quay.io/biocontainers/bioconductor-bionero"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bionero.
shpc-registry automated BioContainers addition for bioconductor-bionero
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bionero
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bionero:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bionero/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bionero/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bionero-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bionero-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bionero-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bionero-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bionero-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bionero-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bionero

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