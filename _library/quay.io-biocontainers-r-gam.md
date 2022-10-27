---
layout: container
name:  "quay.io/biocontainers/r-gam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gam/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-gam/container.yaml"
updated_at: "2022-10-27 00:55:50.487025"
latest: "1.14_4--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/r-gam"

versions:
 - "1.14_4--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for r-gam"
config: {"url": "https://biocontainers.pro/tools/r-gam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gam", "latest": {"1.14_4--r3.4.1_0": "sha256:54828c4175cfcc3a4838eacb319d1e370329cf992eecbe8557e7071a22ab1bea"}, "tags": {"1.14_4--r3.4.1_0": "sha256:54828c4175cfcc3a4838eacb319d1e370329cf992eecbe8557e7071a22ab1bea"}, "docker": "quay.io/biocontainers/r-gam"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gam.
shpc-registry automated BioContainers addition for r-gam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gam:1.14_4--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gam/1.14_4--r3.4.1_0
$ module help quay.io/biocontainers/r-gam/1.14_4--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-gam

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