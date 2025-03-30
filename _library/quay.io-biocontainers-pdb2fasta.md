---
layout: container
name:  "quay.io/biocontainers/pdb2fasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pdb2fasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pdb2fasta/container.yaml"
updated_at: "2025-03-30 03:27:25.592151"
latest: "1.0--h7b50bb2_0"
container_url: "https://biocontainers.pro/tools/pdb2fasta"
aliases:
 - "pdb2fasta"
versions:
 - "1.0--h7b50bb2_0"
description: "singularity registry hpc automated addition for pdb2fasta"
config: {"url": "https://biocontainers.pro/tools/pdb2fasta", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pdb2fasta", "latest": {"1.0--h7b50bb2_0": "sha256:dd0148ce168eb9111f9c55ef9474071990f0078cb15d5d8ed52b5ad469391879"}, "tags": {"1.0--h7b50bb2_0": "sha256:dd0148ce168eb9111f9c55ef9474071990f0078cb15d5d8ed52b5ad469391879"}, "docker": "quay.io/biocontainers/pdb2fasta", "aliases": {"pdb2fasta": "/usr/local/bin/pdb2fasta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pdb2fasta.
singularity registry hpc automated addition for pdb2fasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pdb2fasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pdb2fasta:1.0--h7b50bb2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pdb2fasta/1.0--h7b50bb2_0
$ module help quay.io/biocontainers/pdb2fasta/1.0--h7b50bb2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pdb2fasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pdb2fasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pdb2fasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pdb2fasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pdb2fasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pdb2fasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pdb2fasta

```bash
$ singularity exec <container> /usr/local/bin/pdb2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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