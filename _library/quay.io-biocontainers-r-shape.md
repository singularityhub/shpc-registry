---
layout: container
name:  "quay.io/biocontainers/r-shape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-shape/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-shape/container.yaml"
updated_at: "2022-10-27 01:14:24.724772"
latest: "1.4.2--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-shape"

versions:
 - "1.4.2--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-shape"
config: {"url": "https://biocontainers.pro/tools/r-shape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-shape", "latest": {"1.4.2--r3.2.2_0": "sha256:6b49d2ac5150ced92e41f093722d3ce75ee76c26c8786f22d5ccc57b369b7c0d"}, "tags": {"1.4.2--r3.2.2_0": "sha256:6b49d2ac5150ced92e41f093722d3ce75ee76c26c8786f22d5ccc57b369b7c0d"}, "docker": "quay.io/biocontainers/r-shape"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-shape.
shpc-registry automated BioContainers addition for r-shape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-shape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-shape:1.4.2--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-shape/1.4.2--r3.2.2_0
$ module help quay.io/biocontainers/r-shape/1.4.2--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-shape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-shape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-shape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-shape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-shape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-shape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-shape

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