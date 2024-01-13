---
layout: container
name:  "quay.io/biocontainers/r-sequenza"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sequenza/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sequenza/container.yaml"
updated_at: "2024-01-13 03:02:36.430011"
latest: "3.0.0--r42h3342da4_5"
container_url: "https://biocontainers.pro/tools/r-sequenza"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.0.0--r41h3342da4_4"
 - "3.0.0--r42h3342da4_5"
description: "shpc-registry automated BioContainers addition for r-sequenza"
config: {"url": "https://biocontainers.pro/tools/r-sequenza", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sequenza", "latest": {"3.0.0--r42h3342da4_5": "sha256:200a1a345af39828bb42d04ba632ffafedad5b1992820541fe61d2172a73136a"}, "tags": {"3.0.0--r41h3342da4_4": "sha256:7d1f967f7a5739b45c78fdf485c1776f248558127087ee360293ec593450f6c0", "3.0.0--r42h3342da4_5": "sha256:200a1a345af39828bb42d04ba632ffafedad5b1992820541fe61d2172a73136a"}, "docker": "quay.io/biocontainers/r-sequenza", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sequenza.
shpc-registry automated BioContainers addition for r-sequenza
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sequenza
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sequenza:3.0.0--r42h3342da4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sequenza/3.0.0--r42h3342da4_5
$ module help quay.io/biocontainers/r-sequenza/3.0.0--r42h3342da4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sequenza-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sequenza-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sequenza-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sequenza-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sequenza-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sequenza-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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