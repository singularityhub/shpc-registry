---
layout: container
name:  "quay.io/biocontainers/bioconductor-abaenrichment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-abaenrichment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-abaenrichment/container.yaml"
updated_at: "2023-04-07 02:38:29.293220"
latest: "1.24.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-abaenrichment"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hc247a5b_2"
 - "1.22.0--r41h399db7b_0"
 - "1.20.0--r40h399db7b_1"
 - "1.18.0--r40h5f743cb_0"
 - "1.16.0--r36he1b5a44_1"
description: "shpc-registry automated BioContainers addition for bioconductor-abaenrichment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-abaenrichment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-abaenrichment", "latest": {"1.24.0--r41hc247a5b_2": "sha256:ea2d6c94013a87e5147cc2e24a81bff213da779c8f90132b290113a3964b0e00"}, "tags": {"1.8.0--r3.4.1_0": "sha256:f054459f136805adc8f8f106ccb148bc166f5ade959478e1f5c32d11164c0f17", "1.24.0--r41hc247a5b_2": "sha256:ea2d6c94013a87e5147cc2e24a81bff213da779c8f90132b290113a3964b0e00", "1.22.0--r41h399db7b_0": "sha256:cabaecc51fbd37ac9e746d7b1349406e2c5111fb37cf358ea67e9a3fc6851345", "1.20.0--r40h399db7b_1": "sha256:393403cbe035339dbf69e6dd736d1270624a5bc3617f6dadf66b6bfa1e075c87", "1.18.0--r40h5f743cb_0": "sha256:fa3f6b8a254775887d6af0d9ddc022f66ff4f5e3a9f7be170711721418b84a92", "1.16.0--r36he1b5a44_1": "sha256:662af5408bcbef73062c399554829d771a69935e82c2b5fc440f2084bb78efc1"}, "docker": "quay.io/biocontainers/bioconductor-abaenrichment", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-abaenrichment.
shpc-registry automated BioContainers addition for bioconductor-abaenrichment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-abaenrichment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-abaenrichment:1.24.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-abaenrichment/1.24.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-abaenrichment/1.24.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-abaenrichment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abaenrichment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-abaenrichment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-abaenrichment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-abaenrichment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-abaenrichment-inspect-deffile:

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