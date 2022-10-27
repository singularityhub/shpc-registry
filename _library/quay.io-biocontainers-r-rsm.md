---
layout: container
name:  "quay.io/biocontainers/r-rsm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rsm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-rsm/container.yaml"
updated_at: "2022-10-27 00:40:30.518566"
latest: "2.7_4--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-rsm"

versions:
 - "2.7_4--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-rsm"
config: {"url": "https://biocontainers.pro/tools/r-rsm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rsm", "latest": {"2.7_4--r3.2.2_0": "sha256:656c6e69c499a3d84b8dc9b30ab7ea1a3a3e142ade127218f8b5ce6b82f5f170"}, "tags": {"2.7_4--r3.2.2_0": "sha256:656c6e69c499a3d84b8dc9b30ab7ea1a3a3e142ade127218f8b5ce6b82f5f170"}, "docker": "quay.io/biocontainers/r-rsm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rsm.
shpc-registry automated BioContainers addition for r-rsm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rsm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rsm:2.7_4--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rsm/2.7_4--r3.2.2_0
$ module help quay.io/biocontainers/r-rsm/2.7_4--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rsm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rsm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rsm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rsm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rsm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rsm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-rsm

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