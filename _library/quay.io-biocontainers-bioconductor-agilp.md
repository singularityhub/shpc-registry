---
layout: container
name:  "quay.io/biocontainers/bioconductor-agilp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-agilp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-agilp/container.yaml"
updated_at: "2024-02-29 03:11:02.508216"
latest: "3.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-agilp"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "3.8.0--r3.4.1_0"
 - "3.30.0--r42hdfd78af_0"
 - "3.26.0--r41hdfd78af_0"
 - "3.24.0--r41hdfd78af_0"
 - "3.22.0--r40hdfd78af_1"
 - "3.20.0--r40_0"
 - "3.32.0--r43hdfd78af_0"
 - "3.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-agilp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-agilp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-agilp", "latest": {"3.34.0--r43hdfd78af_0": "sha256:84a1358aaffba24da9135ea24caacdaea706101952f13b18dbc75a9f4f06ae22"}, "tags": {"3.8.0--r3.4.1_0": "sha256:c5ddac6bc9f3f26de008fccfba9027937e86cb4153d70777536145eb5c2f643e", "3.30.0--r42hdfd78af_0": "sha256:8bac8634d3d7b43a8a1b897c1602f0d856b0fb0c01d80622bdbb5e667777bcd7", "3.26.0--r41hdfd78af_0": "sha256:c1b0aece99c02a8fba401f575d8ca26153c60c53c626fa0442232f474f94272c", "3.24.0--r41hdfd78af_0": "sha256:d2ce98a8d943f079afdd14960919f98e06b7beb0ba0ed7418dccb3ba5383d120", "3.22.0--r40hdfd78af_1": "sha256:e7a88c058429f350331f5c75ef835c9e0fb5a4c21be207ee0fdb345d6ea86835", "3.20.0--r40_0": "sha256:0aeb25c42ecac5d903c9707b4ef773d505bb584a027ebe25adb56f390aa445e2", "3.32.0--r43hdfd78af_0": "sha256:e129821ef37e7d85c5deb6d6edc5facb4043dae8f05a4ef3e773bc2ff2006967", "3.34.0--r43hdfd78af_0": "sha256:84a1358aaffba24da9135ea24caacdaea706101952f13b18dbc75a9f4f06ae22"}, "docker": "quay.io/biocontainers/bioconductor-agilp", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-agilp.
shpc-registry automated BioContainers addition for bioconductor-agilp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-agilp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-agilp:3.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-agilp/3.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-agilp/3.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-agilp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agilp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agilp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-agilp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-agilp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-agilp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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