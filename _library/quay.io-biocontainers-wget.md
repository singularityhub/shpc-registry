---
layout: container
name:  "quay.io/biocontainers/wget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wget/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wget/container.yaml"
updated_at: "2023-06-03 03:25:34.230876"
latest: "1.20.1"
container_url: "https://biocontainers.pro/tools/wget"
aliases:
 - "wget"
 - "idn2"
versions:
 - "1.20.1"
description: "shpc-registry automated BioContainers addition for wget"
config: {"url": "https://biocontainers.pro/tools/wget", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wget", "latest": {"1.20.1": "sha256:e8cecf9a14fbf12ad6beecf461dc80244e5f60f1ac2a91d80e61ee93f7c92881"}, "tags": {"1.20.1": "sha256:e8cecf9a14fbf12ad6beecf461dc80244e5f60f1ac2a91d80e61ee93f7c92881"}, "docker": "quay.io/biocontainers/wget", "aliases": {"wget": "/usr/local/bin/wget", "idn2": "/usr/local/bin/idn2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wget.
shpc-registry automated BioContainers addition for wget
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wget
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wget:1.20.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wget/1.20.1
$ module help quay.io/biocontainers/wget/1.20.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wget-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wget-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wget-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wget-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
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