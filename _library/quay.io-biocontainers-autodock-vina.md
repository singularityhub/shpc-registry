---
layout: container
name:  "quay.io/biocontainers/autodock-vina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autodock-vina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autodock-vina/container.yaml"
updated_at: "2025-04-07 03:31:54.682690"
latest: "1.1.2--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/autodock-vina"
aliases:
 - "vina"
 - "vina_split"
versions:
 - "1.1.2--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for autodock-vina"
config: {"url": "https://biocontainers.pro/tools/autodock-vina", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for autodock-vina", "latest": {"1.1.2--h9ee0642_3": "sha256:a60cdd1216f989f42741917855a29fc95f025373c261b8569c95d727631a5a19"}, "tags": {"1.1.2--h9ee0642_3": "sha256:a60cdd1216f989f42741917855a29fc95f025373c261b8569c95d727631a5a19"}, "docker": "quay.io/biocontainers/autodock-vina", "aliases": {"vina": "/usr/local/bin/vina", "vina_split": "/usr/local/bin/vina_split"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autodock-vina.
shpc-registry automated BioContainers addition for autodock-vina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autodock-vina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autodock-vina:1.1.2--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autodock-vina/1.1.2--h9ee0642_3
$ module help quay.io/biocontainers/autodock-vina/1.1.2--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autodock-vina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autodock-vina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autodock-vina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autodock-vina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autodock-vina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autodock-vina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vina

```bash
$ singularity exec <container> /usr/local/bin/vina
$ podman run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vina_split

```bash
$ singularity exec <container> /usr/local/bin/vina_split
$ podman run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vina_split   -v ${PWD} -w ${PWD} <container> -c " $@"
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