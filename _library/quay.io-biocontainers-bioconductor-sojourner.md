---
layout: container
name:  "quay.io/biocontainers/bioconductor-sojourner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sojourner/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sojourner/container.yaml"
updated_at: "2022-10-27 00:59:30.809920"
latest: "1.8.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-sojourner"

versions:
 - "1.8.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-sojourner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sojourner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sojourner", "latest": {"1.8.0--r41hc247a5b_2": "sha256:8bcefa73ebdba30438d9e30eb0cebe5f0cafc5920e81eb27b10bbb72747f73cd"}, "tags": {"1.8.0--r41hc247a5b_2": "sha256:8bcefa73ebdba30438d9e30eb0cebe5f0cafc5920e81eb27b10bbb72747f73cd"}, "docker": "quay.io/biocontainers/bioconductor-sojourner"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sojourner.
shpc-registry automated BioContainers addition for bioconductor-sojourner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sojourner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sojourner:1.8.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sojourner/1.8.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-sojourner/1.8.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sojourner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sojourner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sojourner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sojourner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sojourner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sojourner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sojourner

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