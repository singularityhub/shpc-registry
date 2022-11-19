---
layout: container
name:  "quay.io/biocontainers/blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blast/container.yaml"
updated_at: "2022-11-19 02:10:31.064998"
latest: "2.13.0--hf3cf87c_0"
container_url: "https://biocontainers.pro/tools/blast"

versions:
 - "2.10.1--pl526he19e7b1_3"
 - "2.11.0--pl5262h3289130_1"
 - "2.12.0--pl5262h3289130_0"
 - "2.12.0--hf3cf87c_4"
 - "2.13.0--hf3cf87c_0"
description: "shpc-registry automated BioContainers addition for blast"
config: {"url": "https://biocontainers.pro/tools/blast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blast", "latest": {"2.13.0--hf3cf87c_0": "sha256:221b0ab5540cf7c4013b51b60b2c66113104a5b700611d411ae25eb5904f78d8"}, "tags": {"2.10.1--pl526he19e7b1_3": "sha256:f12a5a35a0e6645134fcfe8650b0d1b5ff1f486430828a4ec3c4c9bfe35a5d78", "2.11.0--pl5262h3289130_1": "sha256:52e8e0ed12a0fe8854681dadb600e1d5599e04b960b01034cb53812fad944c3d", "2.12.0--pl5262h3289130_0": "sha256:a7eb056f5ca6a32551bf9f87b6b15acc45598cfef39bffdd672f59da3847cd18", "2.12.0--hf3cf87c_4": "sha256:9df91dee10f97405384734f964021feae38fcf68a721315f706be99be9366d86", "2.13.0--hf3cf87c_0": "sha256:221b0ab5540cf7c4013b51b60b2c66113104a5b700611d411ae25eb5904f78d8"}, "docker": "quay.io/biocontainers/blast"}
---

This module is a singularity container wrapper for quay.io/biocontainers/blast.
shpc-registry automated BioContainers addition for blast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blast:2.13.0--hf3cf87c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blast/2.13.0--hf3cf87c_0
$ module help quay.io/biocontainers/blast/2.13.0--hf3cf87c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### blast

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