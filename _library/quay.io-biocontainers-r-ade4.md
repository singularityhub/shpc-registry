---
layout: container
name:  "quay.io/biocontainers/r-ade4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ade4/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-ade4/container.yaml"
updated_at: "2022-10-27 00:22:08.363862"
latest: "1.7_2--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-ade4"

versions:
 - "1.7_2--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-ade4"
config: {"url": "https://biocontainers.pro/tools/r-ade4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ade4", "latest": {"1.7_2--r3.2.2_0": "sha256:4fd856b7fa42fcd41639cbcb55567e38880cf49e12653c83dfe86a119206c295"}, "tags": {"1.7_2--r3.2.2_0": "sha256:4fd856b7fa42fcd41639cbcb55567e38880cf49e12653c83dfe86a119206c295"}, "docker": "quay.io/biocontainers/r-ade4"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ade4.
shpc-registry automated BioContainers addition for r-ade4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ade4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ade4:1.7_2--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ade4/1.7_2--r3.2.2_0
$ module help quay.io/biocontainers/r-ade4/1.7_2--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ade4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ade4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ade4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ade4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ade4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ade4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ade4

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