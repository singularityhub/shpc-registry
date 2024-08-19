---
layout: container
name:  "quay.io/biocontainers/prinseq-plus-plus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prinseq-plus-plus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prinseq-plus-plus/container.yaml"
updated_at: "2024-08-19 03:05:52.246620"
latest: "1.2.4--hdcf5f25_5"
container_url: "https://biocontainers.pro/tools/prinseq-plus-plus"
aliases:
 - "prinseq++"
versions:
 - "1.2.4--h7ff8a90_2"
 - "1.2.4--h21ec9f0_4"
 - "1.2.4--hdcf5f25_5"
description: "shpc-registry automated BioContainers addition for prinseq-plus-plus"
config: {"url": "https://biocontainers.pro/tools/prinseq-plus-plus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prinseq-plus-plus", "latest": {"1.2.4--hdcf5f25_5": "sha256:30636c529281d6fabd7acc329fb70b38c16037b789e8361509bd2a6bacde648f"}, "tags": {"1.2.4--h7ff8a90_2": "sha256:cf25da5853576ccdd6cf80b3227854d6a2a01ead7a8be6d32b273077c14b0a6d", "1.2.4--h21ec9f0_4": "sha256:fc7c449535490139ee4e36d919efa40fbeb23849a17451ad9a63858aa39a71ac", "1.2.4--hdcf5f25_5": "sha256:30636c529281d6fabd7acc329fb70b38c16037b789e8361509bd2a6bacde648f"}, "docker": "quay.io/biocontainers/prinseq-plus-plus", "aliases": {"prinseq++": "/usr/local/bin/prinseq++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prinseq-plus-plus.
shpc-registry automated BioContainers addition for prinseq-plus-plus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prinseq-plus-plus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prinseq-plus-plus:1.2.4--hdcf5f25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prinseq-plus-plus/1.2.4--hdcf5f25_5
$ module help quay.io/biocontainers/prinseq-plus-plus/1.2.4--hdcf5f25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prinseq-plus-plus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prinseq-plus-plus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prinseq-plus-plus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prinseq-plus-plus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prinseq-plus-plus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prinseq-plus-plus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prinseq++

```bash
$ singularity exec <container> /usr/local/bin/prinseq++
$ podman run --it --rm --entrypoint /usr/local/bin/prinseq++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prinseq++   -v ${PWD} -w ${PWD} <container> -c " $@"
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