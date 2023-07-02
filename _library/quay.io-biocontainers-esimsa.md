---
layout: container
name:  "quay.io/biocontainers/esimsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esimsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esimsa/container.yaml"
updated_at: "2023-07-02 03:21:17.483500"
latest: "1.0--h470a237_1"
container_url: "https://biocontainers.pro/tools/esimsa"
aliases:
 - "esimsa"
versions:
 - "1.0--h470a237_1"
description: "shpc-registry automated BioContainers addition for esimsa"
config: {"url": "https://biocontainers.pro/tools/esimsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for esimsa", "latest": {"1.0--h470a237_1": "sha256:21f1bc79e5c89c82edaf939cae515b962d5f3670e29191abfc5991e34428cb5e"}, "tags": {"1.0--h470a237_1": "sha256:21f1bc79e5c89c82edaf939cae515b962d5f3670e29191abfc5991e34428cb5e"}, "docker": "quay.io/biocontainers/esimsa", "aliases": {"esimsa": "/usr/local/bin/esimsa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esimsa.
shpc-registry automated BioContainers addition for esimsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esimsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esimsa:1.0--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esimsa/1.0--h470a237_1
$ module help quay.io/biocontainers/esimsa/1.0--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esimsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esimsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esimsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esimsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esimsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esimsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### esimsa

```bash
$ singularity exec <container> /usr/local/bin/esimsa
$ podman run --it --rm --entrypoint /usr/local/bin/esimsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esimsa   -v ${PWD} -w ${PWD} <container> -c " $@"
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