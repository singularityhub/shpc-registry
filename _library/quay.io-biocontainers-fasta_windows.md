---
layout: container
name:  "quay.io/biocontainers/fasta_windows"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fasta_windows/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fasta_windows/container.yaml"
updated_at: "2023-03-10 03:06:47.945085"
latest: "0.2.4--hec16e2b_1"
container_url: "https://biocontainers.pro/tools/fasta_windows"
aliases:
 - "fasta_windows"
versions:
 - "0.2.4--hec16e2b_1"
description: "shpc-registry automated BioContainers addition for fasta_windows"
config: {"url": "https://biocontainers.pro/tools/fasta_windows", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fasta_windows", "latest": {"0.2.4--hec16e2b_1": "sha256:cdcbceb94d381b3a24fcdd25694d1cbb2a86f00bc2f5d81da0b23d58340e0445"}, "tags": {"0.2.4--hec16e2b_1": "sha256:cdcbceb94d381b3a24fcdd25694d1cbb2a86f00bc2f5d81da0b23d58340e0445"}, "docker": "quay.io/biocontainers/fasta_windows", "aliases": {"fasta_windows": "/usr/local/bin/fasta_windows"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fasta_windows.
shpc-registry automated BioContainers addition for fasta_windows
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fasta_windows
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fasta_windows:0.2.4--hec16e2b_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fasta_windows/0.2.4--hec16e2b_1
$ module help quay.io/biocontainers/fasta_windows/0.2.4--hec16e2b_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fasta_windows-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fasta_windows-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fasta_windows-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fasta_windows-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fasta_windows-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fasta_windows-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta_windows

```bash
$ singularity exec <container> /usr/local/bin/fasta_windows
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_windows   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_windows   -v ${PWD} -w ${PWD} <container> -c " $@"
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