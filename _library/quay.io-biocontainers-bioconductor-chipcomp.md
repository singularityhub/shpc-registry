---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipcomp/container.yaml"
updated_at: "2023-03-19 13:30:22.358311"
latest: "1.28.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipcomp"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hc0cfd56_0"
 - "1.24.0--r41hc0cfd56_2"
 - "1.22.0--r41hd029910_0"
 - "1.20.0--r40hd029910_2"
 - "1.18.0--r40h037d062_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipcomp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipcomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipcomp", "latest": {"1.28.0--r42hc0cfd56_0": "sha256:3242eeb5c6cdaa895981a524ecc7dbbdfb174293acb3bc5272548ebc22ecb618"}, "tags": {"1.8.0--r3.4.1_0": "sha256:0b04e3775e9354d1d1d6c39c9ec6d62a9cf8c3a6d1b03d041f834d560876cd7c", "1.28.0--r42hc0cfd56_0": "sha256:3242eeb5c6cdaa895981a524ecc7dbbdfb174293acb3bc5272548ebc22ecb618", "1.24.0--r41hc0cfd56_2": "sha256:6c7996496037c75005709d09eaf0bbda3296184dba6c2675fe8b3e6b9ed76d65", "1.22.0--r41hd029910_0": "sha256:22a5715f03cad9d4a0de62bb077df1fd6eb924e126ece4c0fb4fa819667c28d5", "1.20.0--r40hd029910_2": "sha256:2a1291444a97e9b451d3f00c4594b34d23040a9c4e1fbefe29e076ad4556cf73", "1.18.0--r40h037d062_0": "sha256:b4ab7d51dd1ad62c2ce0d5d834e81b42d7ba245a4d2a649ba12da0a7718e7746"}, "docker": "quay.io/biocontainers/bioconductor-chipcomp", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipcomp.
shpc-registry automated BioContainers addition for bioconductor-chipcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipcomp:1.28.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipcomp/1.28.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-chipcomp/1.28.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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