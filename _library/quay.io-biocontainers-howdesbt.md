---
layout: container
name:  "quay.io/biocontainers/howdesbt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/howdesbt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/howdesbt/container.yaml"
updated_at: "2024-06-16 02:49:25.073469"
latest: "2.00.13--h4ac6f70_1"
container_url: "https://biocontainers.pro/tools/howdesbt"
aliases:
 - "howdesbt"
 - "jellyfish"
versions:
 - "2.00.07--h9f5acd7_0"
 - "2.00.10--h9f5acd7_0"
 - "2.00.13--h9f5acd7_0"
 - "2.00.13--h4ac6f70_1"
description: "shpc-registry automated BioContainers addition for howdesbt"
config: {"url": "https://biocontainers.pro/tools/howdesbt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for howdesbt", "latest": {"2.00.13--h4ac6f70_1": "sha256:572af9027e579c185865e7fc7306fef3d4851728c91ae0e2e925d51a6650e1da"}, "tags": {"2.00.07--h9f5acd7_0": "sha256:2f65d9482b045fee7237abc8295ca7541649dee872d2955fe49770578186302d", "2.00.10--h9f5acd7_0": "sha256:605d4b3eb0ad1a35393757afab0d2014d0342e8cdefac3c39197602e28e4fdc1", "2.00.13--h9f5acd7_0": "sha256:cf639774810dc2849ca78bdbf439c284140703c9c6eaa41a1e7f6fa04918b1cc", "2.00.13--h4ac6f70_1": "sha256:572af9027e579c185865e7fc7306fef3d4851728c91ae0e2e925d51a6650e1da"}, "docker": "quay.io/biocontainers/howdesbt", "aliases": {"howdesbt": "/usr/local/bin/howdesbt", "jellyfish": "/usr/local/bin/jellyfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/howdesbt.
shpc-registry automated BioContainers addition for howdesbt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/howdesbt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/howdesbt:2.00.13--h4ac6f70_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/howdesbt/2.00.13--h4ac6f70_1
$ module help quay.io/biocontainers/howdesbt/2.00.13--h4ac6f70_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### howdesbt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### howdesbt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### howdesbt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### howdesbt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### howdesbt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### howdesbt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### howdesbt

```bash
$ singularity exec <container> /usr/local/bin/howdesbt
$ podman run --it --rm --entrypoint /usr/local/bin/howdesbt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/howdesbt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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