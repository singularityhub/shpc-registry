---
layout: container
name:  "quay.io/biocontainers/bioconductor-abadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-abadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-abadata/container.yaml"
updated_at: "2024-07-08 03:32:48.196617"
latest: "1.24.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-abadata"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_1"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-abadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-abadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-abadata", "latest": {"1.24.0--r41hdfd78af_1": "sha256:f21285659cdddb9dea3befb7b70ab690a6cd3092671a79fc570c7dd1937d5959"}, "tags": {"1.8.0--r3.4.1_0": "sha256:6c1eaa0e9f7aec58f8f8dbb3c069fce7a0aee544f4674c569493e26a51009015", "1.24.0--r41hdfd78af_1": "sha256:f21285659cdddb9dea3befb7b70ab690a6cd3092671a79fc570c7dd1937d5959", "1.22.0--r41hdfd78af_0": "sha256:29d3559dbb3b5c60935d44b572fab5c20c080f6cb01dd0f5d38d20c4e407b266", "1.20.0--r40hdfd78af_1": "sha256:aa0d86a123047445b2d3724d3598f4197c9cfa60be16e82c1031fdc026d62e0e", "1.18.0--r40_0": "sha256:db6f067e2f060a5a70f1e8f7753f96bca828744f94ad70798d181aaf39558d02", "1.16.0--r36_0": "sha256:94b69bdccd3472c71359b11c6f8c4dc2980bd0dbd510780d3bdfe5b9bad76f1f"}, "docker": "quay.io/biocontainers/bioconductor-abadata", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-abadata.
shpc-registry automated BioContainers addition for bioconductor-abadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-abadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-abadata:1.24.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-abadata/1.24.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-abadata/1.24.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-abadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-abadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-abadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-abadata-inspect-deffile:

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