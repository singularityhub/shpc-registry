---
layout: container
name:  "quay.io/biocontainers/metaphlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaphlan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaphlan/container.yaml"
updated_at: "2023-12-08 02:39:22.178462"
latest: "4.0.6--pyhca03a8a_0"
container_url: "https://biocontainers.pro/tools/metaphlan"

versions:
 - "4.0.3--pyhca03a8a_0"
 - "4.0.4--pyhca03a8a_0"
 - "4.0.6--pyhca03a8a_0"
description: "shpc-registry automated BioContainers addition for metaphlan"
config: {"url": "https://biocontainers.pro/tools/metaphlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaphlan", "latest": {"4.0.6--pyhca03a8a_0": "sha256:384f10cfbabe93a1458e66601c187a7497eee4aaef7a8d4bbfe9991a01537c20"}, "tags": {"4.0.3--pyhca03a8a_0": "sha256:27232335b55baa59202253dd1d12f3ea42c665e94fff1115f1c59eb515707975", "4.0.4--pyhca03a8a_0": "sha256:2d21c3c3ae6dc2f35eebfe24f533ac9748626bd0c7e8632173d9170b191783b7", "4.0.6--pyhca03a8a_0": "sha256:384f10cfbabe93a1458e66601c187a7497eee4aaef7a8d4bbfe9991a01537c20"}, "docker": "quay.io/biocontainers/metaphlan"}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaphlan.
shpc-registry automated BioContainers addition for metaphlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaphlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaphlan:4.0.6--pyhca03a8a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaphlan/4.0.6--pyhca03a8a_0
$ module help quay.io/biocontainers/metaphlan/4.0.6--pyhca03a8a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaphlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaphlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaphlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaphlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaphlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaphlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### metaphlan

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