---
layout: container
name:  "quay.io/biocontainers/fastq-pair"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-pair/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-pair/container.yaml"
updated_at: "2024-08-18 03:26:06.390853"
latest: "1.0--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/fastq-pair"
aliases:
 - "fastq_pair"
versions:
 - "1.0--h87f3376_3"
 - "1.0--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for fastq-pair"
config: {"url": "https://biocontainers.pro/tools/fastq-pair", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-pair", "latest": {"1.0--hdbdd923_5": "sha256:520a373c0d126db156e8b5aedd3ac0049db960360cb889724c2736d7f1295f44"}, "tags": {"1.0--h87f3376_3": "sha256:7d3baecef5283435197244b5c3db6dfb7b51060089e4c464307c90af43262a78", "1.0--hdbdd923_5": "sha256:520a373c0d126db156e8b5aedd3ac0049db960360cb889724c2736d7f1295f44"}, "docker": "quay.io/biocontainers/fastq-pair", "aliases": {"fastq_pair": "/usr/local/bin/fastq_pair"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-pair.
shpc-registry automated BioContainers addition for fastq-pair
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-pair
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-pair:1.0--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-pair/1.0--hdbdd923_5
$ module help quay.io/biocontainers/fastq-pair/1.0--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-pair-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-pair-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-pair-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-pair-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-pair-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-pair-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq_pair

```bash
$ singularity exec <container> /usr/local/bin/fastq_pair
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_pair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_pair   -v ${PWD} -w ${PWD} <container> -c " $@"
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