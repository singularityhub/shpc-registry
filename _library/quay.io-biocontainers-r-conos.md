---
layout: container
name:  "quay.io/biocontainers/r-conos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-conos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-conos/container.yaml"
updated_at: "2023-09-25 03:49:29.311680"
latest: "1.5.0--r43h21a89ab_3"
container_url: "https://biocontainers.pro/tools/r-conos"
aliases:
 - "glpsol"
versions:
 - "1.5.0--r42hecf12ef_1"
 - "1.5.0--r42h21a89ab_2"
 - "1.5.0--r43h21a89ab_3"
description: "singularity registry hpc automated addition for r-conos"
config: {"url": "https://biocontainers.pro/tools/r-conos", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-conos", "latest": {"1.5.0--r43h21a89ab_3": "sha256:14fa5afd67e8e10c4f991373c236fc106f829bcc16442d5c6b0fa1c6fec414b8"}, "tags": {"1.5.0--r42hecf12ef_1": "sha256:4ce4c6ab1175e1a91010471fef16810ef3bc888db8485abdfed999cabc7b7c0c", "1.5.0--r42h21a89ab_2": "sha256:7144043067e76c31c87be93bfd2cc87adcf1601ef764953800f6bf3e54e40b7e", "1.5.0--r43h21a89ab_3": "sha256:14fa5afd67e8e10c4f991373c236fc106f829bcc16442d5c6b0fa1c6fec414b8"}, "docker": "quay.io/biocontainers/r-conos", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-conos.
singularity registry hpc automated addition for r-conos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-conos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-conos:1.5.0--r43h21a89ab_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-conos/1.5.0--r43h21a89ab_3
$ module help quay.io/biocontainers/r-conos/1.5.0--r43h21a89ab_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-conos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-conos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-conos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-conos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-conos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-conos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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