---
layout: container
name:  "quay.io/biocontainers/fastpca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastpca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastpca/container.yaml"
updated_at: "2024-06-09 02:46:18.082544"
latest: "0.9.1"
container_url: "https://biocontainers.pro/tools/fastpca"
aliases:
 - "fastpca"
versions:
 - "0.9.1"
description: "shpc-registry automated BioContainers addition for fastpca"
config: {"url": "https://biocontainers.pro/tools/fastpca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastpca", "latest": {"0.9.1": "sha256:24440f9942ff0d5871cc1b0897a6dcb80bf40da788d07fc5bd4abe1f3ea5df05"}, "tags": {"0.9.1": "sha256:24440f9942ff0d5871cc1b0897a6dcb80bf40da788d07fc5bd4abe1f3ea5df05"}, "docker": "quay.io/biocontainers/fastpca", "aliases": {"fastpca": "/usr/local/bin/fastpca"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastpca.
shpc-registry automated BioContainers addition for fastpca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastpca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastpca:0.9.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastpca/0.9.1
$ module help quay.io/biocontainers/fastpca/0.9.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastpca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastpca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastpca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastpca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastpca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastpca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastpca

```bash
$ singularity exec <container> /usr/local/bin/fastpca
$ podman run --it --rm --entrypoint /usr/local/bin/fastpca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastpca   -v ${PWD} -w ${PWD} <container> -c " $@"
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