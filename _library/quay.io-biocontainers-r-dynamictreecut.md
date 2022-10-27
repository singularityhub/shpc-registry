---
layout: container
name:  "quay.io/biocontainers/r-dynamictreecut"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dynamictreecut/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-dynamictreecut/container.yaml"
updated_at: "2022-10-27 00:53:03.890352"
latest: "1.63_1--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/r-dynamictreecut"

versions:
 - "1.63_1--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for r-dynamictreecut"
config: {"url": "https://biocontainers.pro/tools/r-dynamictreecut", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-dynamictreecut", "latest": {"1.63_1--r3.4.1_0": "sha256:351628b4196c0d1954f32924167b119464cd6aa8cc552607f00b9384c7652401"}, "tags": {"1.63_1--r3.4.1_0": "sha256:351628b4196c0d1954f32924167b119464cd6aa8cc552607f00b9384c7652401"}, "docker": "quay.io/biocontainers/r-dynamictreecut"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dynamictreecut.
shpc-registry automated BioContainers addition for r-dynamictreecut
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dynamictreecut
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dynamictreecut:1.63_1--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dynamictreecut/1.63_1--r3.4.1_0
$ module help quay.io/biocontainers/r-dynamictreecut/1.63_1--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dynamictreecut-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dynamictreecut-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dynamictreecut-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dynamictreecut-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dynamictreecut-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dynamictreecut-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-dynamictreecut

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