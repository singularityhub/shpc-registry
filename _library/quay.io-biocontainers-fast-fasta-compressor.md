---
layout: container
name:  "quay.io/biocontainers/fast-fasta-compressor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fast-fasta-compressor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fast-fasta-compressor/container.yaml"
updated_at: "2026-01-13 03:54:56.755902"
latest: "1.0--h9948957_0"
container_url: "https://biocontainers.pro/tools/fast-fasta-compressor"
aliases:
 - "ffc"
versions:
 - "1.0--h9948957_0"
description: "singularity registry hpc automated addition for fast-fasta-compressor"
config: {"url": "https://biocontainers.pro/tools/fast-fasta-compressor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fast-fasta-compressor", "latest": {"1.0--h9948957_0": "sha256:ce78868d5dbc1d694008335be208aa798c832436e0b5ac2a46449f68d1820128"}, "tags": {"1.0--h9948957_0": "sha256:ce78868d5dbc1d694008335be208aa798c832436e0b5ac2a46449f68d1820128"}, "docker": "quay.io/biocontainers/fast-fasta-compressor", "aliases": {"ffc": "/usr/local/bin/ffc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fast-fasta-compressor.
singularity registry hpc automated addition for fast-fasta-compressor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fast-fasta-compressor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fast-fasta-compressor:1.0--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fast-fasta-compressor/1.0--h9948957_0
$ module help quay.io/biocontainers/fast-fasta-compressor/1.0--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fast-fasta-compressor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fast-fasta-compressor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fast-fasta-compressor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fast-fasta-compressor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fast-fasta-compressor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fast-fasta-compressor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ffc

```bash
$ singularity exec <container> /usr/local/bin/ffc
$ podman run --it --rm --entrypoint /usr/local/bin/ffc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ffc   -v ${PWD} -w ${PWD} <container> -c " $@"
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