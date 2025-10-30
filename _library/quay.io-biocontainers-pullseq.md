---
layout: container
name:  "quay.io/biocontainers/pullseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pullseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pullseq/container.yaml"
updated_at: "2025-10-30 03:36:29.857964"
latest: "1.0.2--h1104d80_11"
container_url: "https://biocontainers.pro/tools/pullseq"
aliases:
 - "pullseq"
 - "seqdiff"
versions:
 - "1.0.2--hbd632db_7"
 - "1.0.2--h6ead514_9"
 - "1.0.2--h1104d80_10"
 - "1.0.2--h1104d80_11"
description: "shpc-registry automated BioContainers addition for pullseq"
config: {"url": "https://biocontainers.pro/tools/pullseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pullseq", "latest": {"1.0.2--h1104d80_11": "sha256:8c772940d4a2090fa104507b7b07b938471f56c04b487e12e8ca0083c7b9cb05"}, "tags": {"1.0.2--hbd632db_7": "sha256:18f98b3b5d8373dbbb04c03195580a619a9f136533c96ae9749561ee91db3521", "1.0.2--h6ead514_9": "sha256:cd98cfe9116c1f702c9af93bee2e31bc6da8724ed903bac6717154ad31c39814", "1.0.2--h1104d80_10": "sha256:5fc1cd87bc2d867c51121c3b09f31f7e8867b6e5aaf76fb058c7cbb1e3f3ff23", "1.0.2--h1104d80_11": "sha256:8c772940d4a2090fa104507b7b07b938471f56c04b487e12e8ca0083c7b9cb05"}, "docker": "quay.io/biocontainers/pullseq", "aliases": {"pullseq": "/usr/local/bin/pullseq", "seqdiff": "/usr/local/bin/seqdiff"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pullseq.
shpc-registry automated BioContainers addition for pullseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pullseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pullseq:1.0.2--h1104d80_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pullseq/1.0.2--h1104d80_11
$ module help quay.io/biocontainers/pullseq/1.0.2--h1104d80_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pullseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pullseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pullseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pullseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pullseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pullseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pullseq

```bash
$ singularity exec <container> /usr/local/bin/pullseq
$ podman run --it --rm --entrypoint /usr/local/bin/pullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pullseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdiff

```bash
$ singularity exec <container> /usr/local/bin/seqdiff
$ podman run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
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