---
layout: container
name:  "quay.io/biocontainers/bioconductor-linc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-linc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-linc/container.yaml"
updated_at: "2023-04-23 02:45:40.629960"
latest: "1.15.0--r40h5f743cb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-linc"
aliases:
 - "udunits2"
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341hfc679d8_0"
 - "1.15.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
 - "1.12.0--r36he1b5a44_1"
 - "1.10.0--r351hf484d3e_0"
description: "shpc-registry automated BioContainers addition for bioconductor-linc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-linc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-linc", "latest": {"1.15.0--r40h5f743cb_0": "sha256:f9ba91f388330a62e2a9667ac30d493cc6747d3609d53e09637ab9b5ee116184"}, "tags": {"1.8.0--r341hfc679d8_0": "sha256:60ec90d8ca9ecb214a254866a813dbeeaecd1f7618ebe5a05105ca99dc5d9e00", "1.15.0--r40h5f743cb_0": "sha256:f9ba91f388330a62e2a9667ac30d493cc6747d3609d53e09637ab9b5ee116184", "1.14.0--r36he1b5a44_0": "sha256:264942dd348b34dff97724839718b34b2abd0e022dfbc0258f0e47ae319a0498", "1.12.0--r36he1b5a44_1": "sha256:a4db30a3661434ef057fb6b62d7d614e695e05c48f2d6931289270a4ceed4bd3", "1.10.0--r351hf484d3e_0": "sha256:b5cb01f2c8c2ac11ce2b5479950dac32fb493c9ed26b381072d9b295b6e06d5f"}, "docker": "quay.io/biocontainers/bioconductor-linc", "aliases": {"udunits2": "/usr/local/bin/udunits2", "wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-linc.
shpc-registry automated BioContainers addition for bioconductor-linc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-linc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-linc:1.15.0--r40h5f743cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-linc/1.15.0--r40h5f743cb_0
$ module help quay.io/biocontainers/bioconductor-linc/1.15.0--r40h5f743cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-linc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-linc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-linc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-linc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-linc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### udunits2

```bash
$ singularity exec <container> /usr/local/bin/udunits2
$ podman run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udunits2   -v ${PWD} -w ${PWD} <container> -c " $@"
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