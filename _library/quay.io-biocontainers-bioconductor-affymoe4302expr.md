---
layout: container
name:  "quay.io/biocontainers/bioconductor-affymoe4302expr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affymoe4302expr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affymoe4302expr/container.yaml"
updated_at: "2023-01-26 03:08:27.788232"
latest: "1.35.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affymoe4302expr"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affymoe4302expr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affymoe4302expr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affymoe4302expr", "latest": {"1.35.0--r42hdfd78af_0": "sha256:b2d6fe3d35e5065875003ba7f9549bbbdf01feda54eaa9c8300a8f4caff3389d"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:284f98c1ec3486b18351f6b44882519e491f54bed75dff57e57a78c24b2f4836", "1.35.0--r42hdfd78af_0": "sha256:b2d6fe3d35e5065875003ba7f9549bbbdf01feda54eaa9c8300a8f4caff3389d"}, "docker": "quay.io/biocontainers/bioconductor-affymoe4302expr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affymoe4302expr.
shpc-registry automated BioContainers addition for bioconductor-affymoe4302expr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affymoe4302expr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affymoe4302expr:1.35.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affymoe4302expr/1.35.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affymoe4302expr/1.35.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affymoe4302expr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affymoe4302expr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affymoe4302expr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affymoe4302expr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affymoe4302expr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affymoe4302expr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affymoe4302expr

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