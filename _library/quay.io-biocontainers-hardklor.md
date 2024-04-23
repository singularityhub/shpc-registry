---
layout: container
name:  "quay.io/biocontainers/hardklor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hardklor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hardklor/container.yaml"
updated_at: "2024-04-23 02:44:24.264433"
latest: "2.3.2--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/hardklor"
aliases:
 - "hardklor"
versions:
 - "2.3.2--h87f3376_2"
 - "2.3.2--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for hardklor"
config: {"url": "https://biocontainers.pro/tools/hardklor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hardklor", "latest": {"2.3.2--hdbdd923_4": "sha256:0a53aca888a1ed97c898389f5fde33088238d282fb21b1db0cdc0a9adad68eca"}, "tags": {"2.3.2--h87f3376_2": "sha256:fe507306b8bfcf84ec3531ac8150bf32cc295727570acd00594f2a1cbb1cb1eb", "2.3.2--hdbdd923_4": "sha256:0a53aca888a1ed97c898389f5fde33088238d282fb21b1db0cdc0a9adad68eca"}, "docker": "quay.io/biocontainers/hardklor", "aliases": {"hardklor": "/usr/local/bin/hardklor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hardklor.
shpc-registry automated BioContainers addition for hardklor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hardklor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hardklor:2.3.2--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hardklor/2.3.2--hdbdd923_4
$ module help quay.io/biocontainers/hardklor/2.3.2--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hardklor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hardklor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hardklor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hardklor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hardklor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hardklor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hardklor

```bash
$ singularity exec <container> /usr/local/bin/hardklor
$ podman run --it --rm --entrypoint /usr/local/bin/hardklor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hardklor   -v ${PWD} -w ${PWD} <container> -c " $@"
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