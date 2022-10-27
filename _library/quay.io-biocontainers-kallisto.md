---
layout: container
name:  "quay.io/biocontainers/kallisto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kallisto/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kallisto/container.yaml"
updated_at: "2022-10-27 01:07:32.706885"
latest: "0.48.0--h15996b6_2"
container_url: "https://biocontainers.pro/tools/kallisto"

versions:
 - "0.48.0--h15996b6_2"
description: "shpc-registry automated BioContainers addition for kallisto"
config: {"url": "https://biocontainers.pro/tools/kallisto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kallisto", "latest": {"0.48.0--h15996b6_2": "sha256:e44c2964d20ee3fb46488f77752e904168bf0c343759b02a4ab852361512c103"}, "tags": {"0.48.0--h15996b6_2": "sha256:e44c2964d20ee3fb46488f77752e904168bf0c343759b02a4ab852361512c103"}, "docker": "quay.io/biocontainers/kallisto"}
---

This module is a singularity container wrapper for quay.io/biocontainers/kallisto.
shpc-registry automated BioContainers addition for kallisto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kallisto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kallisto:0.48.0--h15996b6_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kallisto/0.48.0--h15996b6_2
$ module help quay.io/biocontainers/kallisto/0.48.0--h15996b6_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kallisto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kallisto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kallisto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kallisto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### kallisto

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