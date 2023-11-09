---
layout: container
name:  "quay.io/biocontainers/abawaca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abawaca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abawaca/container.yaml"
updated_at: "2023-11-09 02:39:14.131050"
latest: "1.00--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/abawaca"
aliases:
 - "abawaca"
versions:
 - "1.00--h9f5acd7_4"
 - "1.00--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for abawaca"
config: {"url": "https://biocontainers.pro/tools/abawaca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abawaca", "latest": {"1.00--h4ac6f70_6": "sha256:91de874d4ed747bc28ea53377926f4a10a03c7e27755932d2ba285109ca7dabf"}, "tags": {"1.00--h9f5acd7_4": "sha256:df48ab45446d2e77faf912e9a990632a04e0aa7fa45133636f599504107bf724", "1.00--h4ac6f70_6": "sha256:91de874d4ed747bc28ea53377926f4a10a03c7e27755932d2ba285109ca7dabf"}, "docker": "quay.io/biocontainers/abawaca", "aliases": {"abawaca": "/usr/local/bin/abawaca"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abawaca.
shpc-registry automated BioContainers addition for abawaca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abawaca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abawaca:1.00--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abawaca/1.00--h4ac6f70_6
$ module help quay.io/biocontainers/abawaca/1.00--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abawaca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abawaca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abawaca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abawaca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abawaca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abawaca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abawaca

```bash
$ singularity exec <container> /usr/local/bin/abawaca
$ podman run --it --rm --entrypoint /usr/local/bin/abawaca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abawaca   -v ${PWD} -w ${PWD} <container> -c " $@"
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