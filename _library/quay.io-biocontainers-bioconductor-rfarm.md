---
layout: container
name:  "quay.io/biocontainers/bioconductor-rfarm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rfarm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rfarm/container.yaml"
updated_at: "2022-10-27 00:56:42.728051"
latest: "1.6.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rfarm"

versions:
 - "1.6.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rfarm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rfarm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rfarm", "latest": {"1.6.0--r41hdfd78af_0": "sha256:1e829fff8580c39c228a0fb8fada8f02b5adedf2405fc2c9b9aa823da1d2d50b"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:1e829fff8580c39c228a0fb8fada8f02b5adedf2405fc2c9b9aa823da1d2d50b"}, "docker": "quay.io/biocontainers/bioconductor-rfarm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rfarm.
shpc-registry automated BioContainers addition for bioconductor-rfarm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rfarm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rfarm:1.6.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rfarm/1.6.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rfarm/1.6.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rfarm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rfarm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rfarm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rfarm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rfarm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rfarm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rfarm

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