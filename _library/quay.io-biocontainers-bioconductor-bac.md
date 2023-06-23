---
layout: container
name:  "quay.io/biocontainers/bioconductor-bac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bac/container.yaml"
updated_at: "2023-06-23 03:22:16.449051"
latest: "1.58.0--r42ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-bac"

versions:
 - "1.54.0--r41hc0cfd56_2"
 - "1.58.0--r42hc0cfd56_0"
 - "1.58.0--r42ha9d7317_2"
description: "shpc-registry automated BioContainers addition for bioconductor-bac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bac", "latest": {"1.58.0--r42ha9d7317_2": "sha256:19e6a878c30f39e67fa0e0bce177273067845e32d1df336f3a45e5f2a1ceb31f"}, "tags": {"1.54.0--r41hc0cfd56_2": "sha256:c69a959426dd39720597992418aa0f30699ddb2d0b706f6a023fcd7f7b8ce945", "1.58.0--r42hc0cfd56_0": "sha256:f292b2f24764f9cd69bf1770b16e9f910ff088b906b462761be6741a719b51c4", "1.58.0--r42ha9d7317_2": "sha256:19e6a878c30f39e67fa0e0bce177273067845e32d1df336f3a45e5f2a1ceb31f"}, "docker": "quay.io/biocontainers/bioconductor-bac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bac.
shpc-registry automated BioContainers addition for bioconductor-bac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bac:1.58.0--r42ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bac/1.58.0--r42ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-bac/1.58.0--r42ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bac

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