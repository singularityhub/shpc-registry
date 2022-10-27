---
layout: container
name:  "quay.io/biocontainers/edd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/edd/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/edd/container.yaml"
updated_at: "2022-10-27 00:40:05.099485"
latest: "1.1.19--py27h4329609_4"
container_url: "https://biocontainers.pro/tools/edd"
aliases:
 - "edd"
versions:
 - "1.1.19--py27h4329609_4"
description: "shpc-registry automated BioContainers addition for edd"
config: {"url": "https://biocontainers.pro/tools/edd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for edd", "latest": {"1.1.19--py27h4329609_4": "sha256:5e9c6125f0b26c4a697618e0f1f8096703dada38dafa1604ae144f5c56309d89"}, "tags": {"1.1.19--py27h4329609_4": "sha256:5e9c6125f0b26c4a697618e0f1f8096703dada38dafa1604ae144f5c56309d89"}, "docker": "quay.io/biocontainers/edd", "aliases": {"edd": "/usr/local/bin/edd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/edd.
shpc-registry automated BioContainers addition for edd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/edd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/edd:1.1.19--py27h4329609_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/edd/1.1.19--py27h4329609_4
$ module help quay.io/biocontainers/edd/1.1.19--py27h4329609_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### edd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### edd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### edd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### edd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### edd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### edd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### edd

```bash
$ singularity exec <container> /usr/local/bin/edd
$ podman run --it --rm --entrypoint /usr/local/bin/edd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edd   -v ${PWD} -w ${PWD} <container> -c " $@"
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