---
layout: container
name:  "quay.io/biocontainers/plink2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plink2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plink2/container.yaml"
updated_at: "2023-02-21 03:32:28.440835"
latest: "2.00a3.3--hb2a7ceb_0"
container_url: "https://biocontainers.pro/tools/plink2"
aliases:
 - "plink2"
versions:
 - "2.00a3.3--hb2a7ceb_0"
description: "shpc-registry automated BioContainers addition for plink2"
config: {"url": "https://biocontainers.pro/tools/plink2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plink2", "latest": {"2.00a3.3--hb2a7ceb_0": "sha256:dfa04a7b5b5ec23ca8e2e3af6aebd322428ca7c6898546b6e10b9ad841413dd5"}, "tags": {"2.00a3.3--hb2a7ceb_0": "sha256:dfa04a7b5b5ec23ca8e2e3af6aebd322428ca7c6898546b6e10b9ad841413dd5"}, "docker": "quay.io/biocontainers/plink2", "aliases": {"plink2": "/usr/local/bin/plink2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plink2.
shpc-registry automated BioContainers addition for plink2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plink2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plink2:2.00a3.3--hb2a7ceb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plink2/2.00a3.3--hb2a7ceb_0
$ module help quay.io/biocontainers/plink2/2.00a3.3--hb2a7ceb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plink2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plink2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plink2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plink2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plink2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plink2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plink2

```bash
$ singularity exec <container> /usr/local/bin/plink2
$ podman run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
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