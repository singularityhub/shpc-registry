---
layout: container
name:  "quay.io/biocontainers/bioconductor-lobstahs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lobstahs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lobstahs/container.yaml"
updated_at: "2022-10-27 01:02:08.269525"
latest: "1.8.1--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lobstahs"

versions:
 - "1.8.1--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lobstahs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lobstahs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lobstahs", "latest": {"1.8.1--r351_0": "sha256:6a51e5e30e29cd7343ba27f1e654ce50bcd5cff9ceab02dccbbe469ca782cd46"}, "tags": {"1.8.1--r351_0": "sha256:6a51e5e30e29cd7343ba27f1e654ce50bcd5cff9ceab02dccbbe469ca782cd46"}, "docker": "quay.io/biocontainers/bioconductor-lobstahs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lobstahs.
shpc-registry automated BioContainers addition for bioconductor-lobstahs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lobstahs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lobstahs:1.8.1--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lobstahs/1.8.1--r351_0
$ module help quay.io/biocontainers/bioconductor-lobstahs/1.8.1--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lobstahs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lobstahs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lobstahs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lobstahs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lobstahs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lobstahs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lobstahs

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