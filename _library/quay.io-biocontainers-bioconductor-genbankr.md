---
layout: container
name:  "quay.io/biocontainers/bioconductor-genbankr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genbankr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genbankr/container.yaml"
updated_at: "2024-09-25 03:25:21.172815"
latest: "1.27.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genbankr"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.27.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genbankr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genbankr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genbankr", "latest": {"1.27.0--r43hdfd78af_0": "sha256:c19cc037094cdcb5402998e26448d8e362aed6dbb311fcd07db52226e3c6f362"}, "tags": {"1.8.0--r341_0": "sha256:5d47cf67f34a9425b5185499c90c7915af601e6e5732a1e6bf8fa842f8e1ae02", "1.22.0--r41hdfd78af_0": "sha256:ed7cbacfb845981e4f4743d061125ff7e86e183c6135bb5f30e8e6d624216bb9", "1.20.0--r41hdfd78af_0": "sha256:d6c5d64ffb76afdf39725e831bff5219d85d40a7aef697003c221cae6aefed31", "1.18.0--r40hdfd78af_1": "sha256:78c6125eec26256b61721abf1d32ca36074185ca91ed2bcf04274186d4b18d52", "1.16.0--r40_0": "sha256:ea3076c115e3d6e4e39062468c4f96f6c1ce7780205493983a19fd6b23455f28", "1.14.0--r36_0": "sha256:c87ae6144de8441112562971e793ed643b8e39075abf9110c2ff39a39d9ed195", "1.26.0--r42hdfd78af_0": "sha256:a042623a2078a36ad03af82fb88ac0dec919cb08edfc53d8d20edef826a14738", "1.27.0--r43hdfd78af_0": "sha256:c19cc037094cdcb5402998e26448d8e362aed6dbb311fcd07db52226e3c6f362"}, "docker": "quay.io/biocontainers/bioconductor-genbankr", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genbankr.
shpc-registry automated BioContainers addition for bioconductor-genbankr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genbankr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genbankr:1.27.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genbankr/1.27.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genbankr/1.27.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genbankr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genbankr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genbankr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genbankr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genbankr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genbankr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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