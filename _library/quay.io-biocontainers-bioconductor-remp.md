---
layout: container
name:  "quay.io/biocontainers/bioconductor-remp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-remp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-remp/container.yaml"
updated_at: "2024-06-09 02:53:17.335765"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-remp"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-remp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-remp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-remp", "latest": {"1.26.0--r43hdfd78af_0": "sha256:16a66c992e793ff5020e47976d4d7ffe93474bd8cbc1d3847ab6a393497a1c38"}, "tags": {"1.8.1--r36_1": "sha256:2226aacfbc6f34f9f10250ad1769c872398e69ff992d9d91495ef85559b1090a", "1.22.0--r42hdfd78af_0": "sha256:fefc1f89a4495a4e09b76cbf0f790576aab8a6bd3640848824e58626ef140f24", "1.18.0--r41hdfd78af_0": "sha256:c315793bd906c0425039b0db2efcdbfa8d4d997ececb8203c1cefe55ccb65da5", "1.16.0--r41hdfd78af_0": "sha256:5a0fb53532fca22b5fcb79f6aa0bb092b7d34a6c6a9a37ea87879fde2f4d98cd", "1.14.0--r40hdfd78af_1": "sha256:d9532eea5657a721fec641a53b11c0d43f953900cf9579bd12c55a1ed31e614e", "1.12.0--r40_0": "sha256:22a0a85eb7b6011f9222500dcc12b05c38a5cc182c5993549b04574a7c80cb17", "1.24.0--r43hdfd78af_0": "sha256:f3762b4d7650c79bc2ce1f9667e12136e256c36a2a6ec8cfee88a32cc3925600", "1.26.0--r43hdfd78af_0": "sha256:16a66c992e793ff5020e47976d4d7ffe93474bd8cbc1d3847ab6a393497a1c38"}, "docker": "quay.io/biocontainers/bioconductor-remp", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-remp.
shpc-registry automated BioContainers addition for bioconductor-remp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-remp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-remp:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-remp/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-remp/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-remp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-remp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-remp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-remp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-remp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-remp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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