---
layout: container
name:  "quay.io/biocontainers/sherpas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sherpas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sherpas/container.yaml"
updated_at: "2023-08-29 03:57:14.048975"
latest: "1.0.2--h376f1d3_4"
container_url: "https://biocontainers.pro/tools/sherpas"
aliases:
 - "SHERPAS"
versions:
 - "1.0.2--h2df963e_2"
 - "1.0.2--h2df963e_3"
 - "1.0.2--h376f1d3_4"
description: "shpc-registry automated BioContainers addition for sherpas"
config: {"url": "https://biocontainers.pro/tools/sherpas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sherpas", "latest": {"1.0.2--h376f1d3_4": "sha256:4b6d6d5d0e8f80798d1546baa76369455235d3de76dcd7f5bc89a3436d3ee271"}, "tags": {"1.0.2--h2df963e_2": "sha256:33063490cbf9298117682f7960e9c98d39313fd5eedd3af74c953b72c838d83b", "1.0.2--h2df963e_3": "sha256:79e346d8b5274eef1555e0a9a95e29d8fae8ab91c14b97f099a54df28e57d544", "1.0.2--h376f1d3_4": "sha256:4b6d6d5d0e8f80798d1546baa76369455235d3de76dcd7f5bc89a3436d3ee271"}, "docker": "quay.io/biocontainers/sherpas", "aliases": {"SHERPAS": "/usr/local/bin/SHERPAS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sherpas.
shpc-registry automated BioContainers addition for sherpas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sherpas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sherpas:1.0.2--h376f1d3_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sherpas/1.0.2--h376f1d3_4
$ module help quay.io/biocontainers/sherpas/1.0.2--h376f1d3_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sherpas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sherpas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sherpas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sherpas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sherpas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sherpas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SHERPAS

```bash
$ singularity exec <container> /usr/local/bin/SHERPAS
$ podman run --it --rm --entrypoint /usr/local/bin/SHERPAS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHERPAS   -v ${PWD} -w ${PWD} <container> -c " $@"
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