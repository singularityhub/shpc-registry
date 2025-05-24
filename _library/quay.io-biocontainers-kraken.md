---
layout: container
name:  "quay.io/biocontainers/kraken"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kraken/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kraken/container.yaml"
updated_at: "2025-05-24 11:43:42.490439"
latest: "1.1--h470a237_2"
container_url: "https://biocontainers.pro/tools/kraken"

versions:
 - "1.1--h470a237_2"
description: "shpc-registry automated BioContainers addition for kraken"
config: {"url": "https://biocontainers.pro/tools/kraken", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kraken", "latest": {"1.1--h470a237_2": "sha256:4b414bcf4434c0f9a04b73dce6917965aeac0806542624b40910fae02fefb0e1"}, "tags": {"1.1--h470a237_2": "sha256:4b414bcf4434c0f9a04b73dce6917965aeac0806542624b40910fae02fefb0e1"}, "docker": "quay.io/biocontainers/kraken"}
---

This module is a singularity container wrapper for quay.io/biocontainers/kraken.
shpc-registry automated BioContainers addition for kraken
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kraken
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kraken:1.1--h470a237_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kraken/1.1--h470a237_2
$ module help quay.io/biocontainers/kraken/1.1--h470a237_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kraken-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kraken-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kraken-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kraken-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kraken-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kraken-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### kraken

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