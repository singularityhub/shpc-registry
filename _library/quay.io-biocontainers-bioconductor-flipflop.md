---
layout: container
name:  "quay.io/biocontainers/bioconductor-flipflop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flipflop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flipflop/container.yaml"
updated_at: "2025-03-21 03:34:30.859053"
latest: "1.18.0--r351hfc679d8_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flipflop"
aliases:
 - "wget"
versions:
 - "1.18.0--r351hfc679d8_0"
 - "1.18.0--r341hfc679d8_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flipflop"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flipflop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flipflop", "latest": {"1.18.0--r351hfc679d8_0": "sha256:7b87b2c95653cb8a46b9b032506526aa7dba7eaeb83983aad724044bb506881b"}, "tags": {"1.18.0--r351hfc679d8_0": "sha256:7b87b2c95653cb8a46b9b032506526aa7dba7eaeb83983aad724044bb506881b", "1.18.0--r341hfc679d8_0": "sha256:ab42ae21a7563af95ec649423f041ae3dc8aefbc4395ea709562c02ea3b5ecb1"}, "docker": "quay.io/biocontainers/bioconductor-flipflop", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flipflop.
shpc-registry automated BioContainers addition for bioconductor-flipflop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flipflop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flipflop:1.18.0--r351hfc679d8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flipflop/1.18.0--r351hfc679d8_0
$ module help quay.io/biocontainers/bioconductor-flipflop/1.18.0--r351hfc679d8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flipflop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flipflop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flipflop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flipflop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flipflop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flipflop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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