---
layout: container
name:  "quay.io/biocontainers/easel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/easel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/easel/container.yaml"
updated_at: "2022-10-27 01:05:45.995522"
latest: "0.48--hec16e2b_1"
container_url: "https://biocontainers.pro/tools/easel"

versions:
 - "0.48--hec16e2b_1"
description: "shpc-registry automated BioContainers addition for easel"
config: {"url": "https://biocontainers.pro/tools/easel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for easel", "latest": {"0.48--hec16e2b_1": "sha256:eec502257796955e682002f3b9e4b72375656240b7435c27b2e1fba147fd1688"}, "tags": {"0.48--hec16e2b_1": "sha256:eec502257796955e682002f3b9e4b72375656240b7435c27b2e1fba147fd1688"}, "docker": "quay.io/biocontainers/easel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/easel.
shpc-registry automated BioContainers addition for easel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/easel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/easel:0.48--hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/easel/0.48--hec16e2b_1
$ module help quay.io/biocontainers/easel/0.48--hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### easel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### easel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### easel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### easel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### easel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### easel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### easel

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