---
layout: container
name:  "quay.io/biocontainers/bioconductor-splicer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splicer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splicer/container.yaml"
updated_at: "2023-09-24 02:32:12.892553"
latest: "1.22.0--r351h470a237_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splicer"
aliases:
 - "wget"
versions:
 - "1.22.0--r351h470a237_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splicer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splicer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splicer", "latest": {"1.22.0--r351h470a237_0": "sha256:3565b1c171972813a6b33aa68a8f104ca8b67355e14119f8f4fe0b75595f9e8b"}, "tags": {"1.22.0--r351h470a237_0": "sha256:3565b1c171972813a6b33aa68a8f104ca8b67355e14119f8f4fe0b75595f9e8b"}, "docker": "quay.io/biocontainers/bioconductor-splicer", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splicer.
shpc-registry automated BioContainers addition for bioconductor-splicer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splicer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splicer:1.22.0--r351h470a237_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splicer/1.22.0--r351h470a237_0
$ module help quay.io/biocontainers/bioconductor-splicer/1.22.0--r351h470a237_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splicer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splicer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splicer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splicer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splicer-inspect-deffile:

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