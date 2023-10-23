---
layout: container
name:  "quay.io/biocontainers/mosaik"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mosaik/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mosaik/container.yaml"
updated_at: "2023-10-23 02:45:04.718023"
latest: "2.2.26--he941832_4"
container_url: "https://biocontainers.pro/tools/mosaik"
aliases:
 - "MosaikAligner"
 - "MosaikBuild"
 - "MosaikJump"
 - "MosaikText"
versions:
 - "2.2.26--he941832_4"
description: "shpc-registry automated BioContainers addition for mosaik"
config: {"url": "https://biocontainers.pro/tools/mosaik", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mosaik", "latest": {"2.2.26--he941832_4": "sha256:4bd7cb403e8ca7f8db422dd9c4381902b3a2053f503b62396306e88ecba3e65d"}, "tags": {"2.2.26--he941832_4": "sha256:4bd7cb403e8ca7f8db422dd9c4381902b3a2053f503b62396306e88ecba3e65d"}, "docker": "quay.io/biocontainers/mosaik", "aliases": {"MosaikAligner": "/usr/local/bin/MosaikAligner", "MosaikBuild": "/usr/local/bin/MosaikBuild", "MosaikJump": "/usr/local/bin/MosaikJump", "MosaikText": "/usr/local/bin/MosaikText"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mosaik.
shpc-registry automated BioContainers addition for mosaik
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mosaik
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mosaik:2.2.26--he941832_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mosaik/2.2.26--he941832_4
$ module help quay.io/biocontainers/mosaik/2.2.26--he941832_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mosaik-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mosaik-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mosaik-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mosaik-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mosaik-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mosaik-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MosaikAligner

```bash
$ singularity exec <container> /usr/local/bin/MosaikAligner
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikBuild

```bash
$ singularity exec <container> /usr/local/bin/MosaikBuild
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikBuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikJump

```bash
$ singularity exec <container> /usr/local/bin/MosaikJump
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikJump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikJump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MosaikText

```bash
$ singularity exec <container> /usr/local/bin/MosaikText
$ podman run --it --rm --entrypoint /usr/local/bin/MosaikText   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MosaikText   -v ${PWD} -w ${PWD} <container> -c " $@"
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