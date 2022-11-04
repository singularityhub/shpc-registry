---
layout: container
name:  "quay.io/biocontainers/bioconductor-preprocesscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-preprocesscore/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-preprocesscore/container.yaml"
updated_at: "2022-11-04 00:26:48.069631"
latest: "1.56.0--r41hc0cfd56_3"
container_url: "https://biocontainers.pro/tools/bioconductor-preprocesscore"

versions:
 - "1.56.0--r41hc0cfd56_3"
description: "shpc-registry automated BioContainers addition for bioconductor-preprocesscore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-preprocesscore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-preprocesscore", "latest": {"1.56.0--r41hc0cfd56_3": "sha256:04f16830ab80ff8d1b47df3698ff59af740b2e9da59e15cc4f910da054a7c7b7"}, "tags": {"1.56.0--r41hc0cfd56_3": "sha256:04f16830ab80ff8d1b47df3698ff59af740b2e9da59e15cc4f910da054a7c7b7"}, "docker": "quay.io/biocontainers/bioconductor-preprocesscore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-preprocesscore.
shpc-registry automated BioContainers addition for bioconductor-preprocesscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-preprocesscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-preprocesscore:1.56.0--r41hc0cfd56_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-preprocesscore/1.56.0--r41hc0cfd56_3
$ module help quay.io/biocontainers/bioconductor-preprocesscore/1.56.0--r41hc0cfd56_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-preprocesscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-preprocesscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-preprocesscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-preprocesscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-preprocesscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-preprocesscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-preprocesscore

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