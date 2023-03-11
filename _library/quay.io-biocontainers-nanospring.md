---
layout: container
name:  "quay.io/biocontainers/nanospring"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanospring/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanospring/container.yaml"
updated_at: "2023-03-11 03:11:37.161174"
latest: "0.2--h5b5514e_0"
container_url: "https://biocontainers.pro/tools/nanospring"
aliases:
 - "NanoSpring"
versions:
 - "0.1--h5b5514e_1"
 - "0.2--h5b5514e_0"
description: "shpc-registry automated BioContainers addition for nanospring"
config: {"url": "https://biocontainers.pro/tools/nanospring", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanospring", "latest": {"0.2--h5b5514e_0": "sha256:eec0fc7ad6a4dd7febd5a683dae5930db38988baef1644ff81b36bcb675882d1"}, "tags": {"0.1--h5b5514e_1": "sha256:be76695277722cc0541b08f714b2c753e50c6c362cc65bdbd26f53fe38f07104", "0.2--h5b5514e_0": "sha256:eec0fc7ad6a4dd7febd5a683dae5930db38988baef1644ff81b36bcb675882d1"}, "docker": "quay.io/biocontainers/nanospring", "aliases": {"NanoSpring": "/usr/local/bin/NanoSpring"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanospring.
shpc-registry automated BioContainers addition for nanospring
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanospring
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanospring:0.2--h5b5514e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanospring/0.2--h5b5514e_0
$ module help quay.io/biocontainers/nanospring/0.2--h5b5514e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanospring-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanospring-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanospring-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanospring-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanospring-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanospring-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NanoSpring

```bash
$ singularity exec <container> /usr/local/bin/NanoSpring
$ podman run --it --rm --entrypoint /usr/local/bin/NanoSpring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NanoSpring   -v ${PWD} -w ${PWD} <container> -c " $@"
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