---
layout: container
name:  "quay.io/biocontainers/bioconductor-linc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-linc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-linc/container.yaml"
updated_at: "2024-10-31 03:05:32.399442"
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
 - "1.8.0--r351hfc679d8_0"
description: "shpc-registry automated BioContainers addition for bioconductor-linc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-linc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-linc", "latest": {"1.15.0--r40h5f743cb_0": "sha256:f9ba91f388330a62e2a9667ac30d493cc6747d3609d53e09637ab9b5ee116184"}, "tags": {"1.8.0--r341hfc679d8_0": "sha256:a4cd2951da0066cccfb7da15dffe08dad424d00632aa5a80203f14b35a041f91", "1.15.0--r40h5f743cb_0": "sha256:f9ba91f388330a62e2a9667ac30d493cc6747d3609d53e09637ab9b5ee116184", "1.14.0--r36he1b5a44_0": "sha256:9772b887a9c81712a0911e7fabc9162e811f4a0a5a52347f22acb0c57323b8de", "1.12.0--r36he1b5a44_1": "sha256:8894a6896d38f0125d834986aee8ad49fdcdf296515edeb2b59f221891074026", "1.10.0--r351hf484d3e_0": "sha256:392d36f5e37afafac0aa6e7c3cf6f09b1ffef600213b778e5c1392365d25d477", "1.8.0--r351hfc679d8_0": "sha256:e6ac30076ff04f4d424f0b38473494ba64f0acc0097601c2a463a81592e219e4"}, "docker": "quay.io/biocontainers/bioconductor-linc", "aliases": {"udunits2": "/usr/local/bin/udunits2", "wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
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