---
layout: container
name:  "quay.io/biocontainers/r-rcppparallel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rcppparallel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-rcppparallel/container.yaml"
updated_at: "2022-10-27 00:35:22.218216"
latest: "4.3.20--r3.3.1_1"
container_url: "https://biocontainers.pro/tools/r-rcppparallel"

versions:
 - "4.3.20--r3.3.1_1"
description: "shpc-registry automated BioContainers addition for r-rcppparallel"
config: {"url": "https://biocontainers.pro/tools/r-rcppparallel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rcppparallel", "latest": {"4.3.20--r3.3.1_1": "sha256:0b06b12d5cd926a5299f24a835f6b7ba14d615161fd2a0efdf17b448964de9ef"}, "tags": {"4.3.20--r3.3.1_1": "sha256:0b06b12d5cd926a5299f24a835f6b7ba14d615161fd2a0efdf17b448964de9ef"}, "docker": "quay.io/biocontainers/r-rcppparallel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rcppparallel.
shpc-registry automated BioContainers addition for r-rcppparallel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rcppparallel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rcppparallel:4.3.20--r3.3.1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rcppparallel/4.3.20--r3.3.1_1
$ module help quay.io/biocontainers/r-rcppparallel/4.3.20--r3.3.1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rcppparallel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rcppparallel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rcppparallel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rcppparallel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rcppparallel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rcppparallel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-rcppparallel

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