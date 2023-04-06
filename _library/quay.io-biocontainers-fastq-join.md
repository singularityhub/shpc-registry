---
layout: container
name:  "quay.io/biocontainers/fastq-join"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-join/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-join/container.yaml"
updated_at: "2023-04-06 02:32:14.936972"
latest: "1.3.1--h9f5acd7_5"
container_url: "https://biocontainers.pro/tools/fastq-join"
aliases:
 - "fastq-join"
versions:
 - "1.3.1--h9f5acd7_5"
description: "shpc-registry automated BioContainers addition for fastq-join"
config: {"url": "https://biocontainers.pro/tools/fastq-join", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-join", "latest": {"1.3.1--h9f5acd7_5": "sha256:36c5408357a3a1d2a6639116b83f13c16826bc2eb1384c8f6edc714c4c06144f"}, "tags": {"1.3.1--h9f5acd7_5": "sha256:36c5408357a3a1d2a6639116b83f13c16826bc2eb1384c8f6edc714c4c06144f"}, "docker": "quay.io/biocontainers/fastq-join", "aliases": {"fastq-join": "/usr/local/bin/fastq-join"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-join.
shpc-registry automated BioContainers addition for fastq-join
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-join
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-join:1.3.1--h9f5acd7_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-join/1.3.1--h9f5acd7_5
$ module help quay.io/biocontainers/fastq-join/1.3.1--h9f5acd7_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-join-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-join-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-join-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-join-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-join-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-join-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-join

```bash
$ singularity exec <container> /usr/local/bin/fastq-join
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
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