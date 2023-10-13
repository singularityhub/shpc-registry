---
layout: container
name:  "quay.io/biocontainers/stride"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stride/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stride/container.yaml"
updated_at: "2023-10-13 02:39:59.489453"
latest: "1.0--h8b12597_5"
container_url: "https://biocontainers.pro/tools/stride"
aliases:
 - "stride"
versions:
 - "1.0--h8b12597_5"
description: "shpc-registry automated BioContainers addition for stride"
config: {"url": "https://biocontainers.pro/tools/stride", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stride", "latest": {"1.0--h8b12597_5": "sha256:2ed78d461f2e6ac283a9e07bf727750ed0270f751c127fd2503a7b3b286b380b"}, "tags": {"1.0--h8b12597_5": "sha256:2ed78d461f2e6ac283a9e07bf727750ed0270f751c127fd2503a7b3b286b380b"}, "docker": "quay.io/biocontainers/stride", "aliases": {"stride": "/usr/local/bin/stride"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stride.
shpc-registry automated BioContainers addition for stride
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stride
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stride:1.0--h8b12597_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stride/1.0--h8b12597_5
$ module help quay.io/biocontainers/stride/1.0--h8b12597_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stride-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stride-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stride-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stride-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stride-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stride-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stride

```bash
$ singularity exec <container> /usr/local/bin/stride
$ podman run --it --rm --entrypoint /usr/local/bin/stride   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stride   -v ${PWD} -w ${PWD} <container> -c " $@"
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