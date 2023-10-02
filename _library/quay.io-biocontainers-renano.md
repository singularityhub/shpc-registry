---
layout: container
name:  "quay.io/biocontainers/renano"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/renano/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/renano/container.yaml"
updated_at: "2023-10-02 03:14:21.171778"
latest: "1.3--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/renano"
aliases:
 - "renano"
versions:
 - "1.3--hd03093a_1"
 - "1.3--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for renano"
config: {"url": "https://biocontainers.pro/tools/renano", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for renano", "latest": {"1.3--hdcf5f25_3": "sha256:ae335a498fe3c1e8f471d8fa037a3ff61e9ca5698816b5d91d9fb054961a6906"}, "tags": {"1.3--hd03093a_1": "sha256:92b1f6e590c7bfe279cde04a8f3a3017e81a14e8fae5cea38586b4366a3f1027", "1.3--hdcf5f25_3": "sha256:ae335a498fe3c1e8f471d8fa037a3ff61e9ca5698816b5d91d9fb054961a6906"}, "docker": "quay.io/biocontainers/renano", "aliases": {"renano": "/usr/local/bin/renano"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/renano.
shpc-registry automated BioContainers addition for renano
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/renano
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/renano:1.3--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/renano/1.3--hdcf5f25_3
$ module help quay.io/biocontainers/renano/1.3--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### renano-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### renano-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### renano-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### renano-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### renano-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### renano-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### renano

```bash
$ singularity exec <container> /usr/local/bin/renano
$ podman run --it --rm --entrypoint /usr/local/bin/renano   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/renano   -v ${PWD} -w ${PWD} <container> -c " $@"
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