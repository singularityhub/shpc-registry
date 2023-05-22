---
layout: container
name:  "quay.io/biocontainers/bioconductor-genegeneinter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genegeneinter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genegeneinter/container.yaml"
updated_at: "2023-05-22 02:50:01.036578"
latest: "1.24.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genegeneinter"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.14.0--r40h5f743cb_0"
 - "1.12.0--r36he1b5a44_0"
 - "1.10.0--r36he1b5a44_1"
 - "1.24.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genegeneinter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genegeneinter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genegeneinter", "latest": {"1.24.0--r42hc247a5b_0": "sha256:8b67d23f269e8cf66d95186487bbf2f5924e1e8ec53adda8d89b7ea1e2c72c83"}, "tags": {"1.8.0--r351_0": "sha256:b1131d6e563f02e84c3123672330e6cc801dad1c5177a4ca11658176d4d12396", "1.20.0--r41hc247a5b_2": "sha256:ddd8ee1ac036360a9920f44f99d1c52cb1654e0e2ed3240f76d0323dda478e02", "1.18.0--r41h399db7b_0": "sha256:4b24d2cefd0765382356c12374eaa40b68f765917fb8618fe731f05379ab3ca0", "1.14.0--r40h5f743cb_0": "sha256:2d5031e80f787f862f46c6e87ed174c371308e8dc2ba80f9c2f506c7cc60f53f", "1.12.0--r36he1b5a44_0": "sha256:7b0e4ca8852113536cbcfb067e05a6dc2761e45bb556d3fa8d4b0b290d2b8f94", "1.10.0--r36he1b5a44_1": "sha256:511c6f58316ce3cf7ba7de21a228a5a925176015c22e70ec166cc93eb1756e47", "1.24.0--r42hc247a5b_0": "sha256:8b67d23f269e8cf66d95186487bbf2f5924e1e8ec53adda8d89b7ea1e2c72c83"}, "docker": "quay.io/biocontainers/bioconductor-genegeneinter", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genegeneinter.
shpc-registry automated BioContainers addition for bioconductor-genegeneinter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genegeneinter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genegeneinter:1.24.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genegeneinter/1.24.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-genegeneinter/1.24.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genegeneinter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genegeneinter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genegeneinter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genegeneinter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genegeneinter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genegeneinter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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