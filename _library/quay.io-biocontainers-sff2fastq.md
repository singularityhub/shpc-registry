---
layout: container
name:  "quay.io/biocontainers/sff2fastq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sff2fastq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sff2fastq/container.yaml"
updated_at: "2023-09-11 02:57:02.451686"
latest: "0.9.2--h470a237_1"
container_url: "https://biocontainers.pro/tools/sff2fastq"
aliases:
 - "sff2fastq"
versions:
 - "0.9.2--h470a237_1"
description: "shpc-registry automated BioContainers addition for sff2fastq"
config: {"url": "https://biocontainers.pro/tools/sff2fastq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sff2fastq", "latest": {"0.9.2--h470a237_1": "sha256:d5b5ba733b9e615faf720b5562c5c9fe450c69ce5869e722c4cd7e0e693b8960"}, "tags": {"0.9.2--h470a237_1": "sha256:d5b5ba733b9e615faf720b5562c5c9fe450c69ce5869e722c4cd7e0e693b8960"}, "docker": "quay.io/biocontainers/sff2fastq", "aliases": {"sff2fastq": "/usr/local/bin/sff2fastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sff2fastq.
shpc-registry automated BioContainers addition for sff2fastq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sff2fastq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sff2fastq:0.9.2--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sff2fastq/0.9.2--h470a237_1
$ module help quay.io/biocontainers/sff2fastq/0.9.2--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sff2fastq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sff2fastq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sff2fastq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sff2fastq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sff2fastq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sff2fastq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sff2fastq

```bash
$ singularity exec <container> /usr/local/bin/sff2fastq
$ podman run --it --rm --entrypoint /usr/local/bin/sff2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sff2fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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