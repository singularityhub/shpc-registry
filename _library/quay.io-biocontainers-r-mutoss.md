---
layout: container
name:  "quay.io/biocontainers/r-mutoss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mutoss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mutoss/container.yaml"
updated_at: "2025-11-25 03:50:24.253345"
latest: "0.1_12--r44h3121a25_8"
container_url: "https://biocontainers.pro/tools/r-mutoss"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1_12--r41h3121a25_5"
 - "0.1_12--r42h3121a25_6"
 - "0.1_12--r43h3121a25_7"
 - "0.1_12--r44h3121a25_8"
description: "shpc-registry automated BioContainers addition for r-mutoss"
config: {"url": "https://biocontainers.pro/tools/r-mutoss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-mutoss", "latest": {"0.1_12--r44h3121a25_8": "sha256:f2f3e9bc95a0eb6fd568efad0ed8f425d11cf98a14819f696d8eeb05deb0bacf"}, "tags": {"0.1_12--r41h3121a25_5": "sha256:ea655537de28a5e10262bdafbbcef33694476f6a6938279506e7d84db1187de5", "0.1_12--r42h3121a25_6": "sha256:5da5fc65557967dbc3456d942fdc223cb1a73ec98b80e452863e0711a69078a8", "0.1_12--r43h3121a25_7": "sha256:f7f3ae48a0c3397258d6078aa7117c751692fd9aeda7c94c9aaefa803598a8c3", "0.1_12--r44h3121a25_8": "sha256:f2f3e9bc95a0eb6fd568efad0ed8f425d11cf98a14819f696d8eeb05deb0bacf"}, "docker": "quay.io/biocontainers/r-mutoss", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mutoss.
shpc-registry automated BioContainers addition for r-mutoss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mutoss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mutoss:0.1_12--r44h3121a25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mutoss/0.1_12--r44h3121a25_8
$ module help quay.io/biocontainers/r-mutoss/0.1_12--r44h3121a25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mutoss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mutoss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mutoss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mutoss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mutoss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mutoss-inspect-deffile:

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