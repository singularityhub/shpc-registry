---
layout: container
name:  "quay.io/biocontainers/bioconductor-scran"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scran/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scran/container.yaml"
updated_at: "2023-06-15 03:27:33.151224"
latest: "1.26.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scran"
aliases:
 - "wget"
versions:
 - "1.8.4--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.1--r41hc247a5b_1"
 - "1.20.1--r41h399db7b_0"
 - "1.18.5--r40h399db7b_0"
 - "1.16.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scran"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scran", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scran", "latest": {"1.26.0--r42hc247a5b_0": "sha256:689b68fe8ef3fe12c97306a921eb2d4eef054f07192337b5e59798fc2fc2e744"}, "tags": {"1.8.4--r351hfc679d8_0": "sha256:c8e1836826ec416408dea1ed111010c2b80d20c73bda3c842d4edd6ac9bf96a0", "1.26.0--r42hc247a5b_0": "sha256:689b68fe8ef3fe12c97306a921eb2d4eef054f07192337b5e59798fc2fc2e744", "1.22.1--r41hc247a5b_1": "sha256:81c49c887e31971dbed6622754e827542a3d6fec34558d7871a0463cdf58e109", "1.20.1--r41h399db7b_0": "sha256:04720a73a2b27cf567e6befe4fb6a5ece898005d93f20129ebb58b9f6b969aca", "1.18.5--r40h399db7b_0": "sha256:8b5aa410aae85504d4da76c9a42337a7c345dc0424a2ec41e03843a1663e53ae", "1.16.0--r40h5f743cb_0": "sha256:29d80cd38ba0852a5082bde469ba6292087fbe2873495db2ba0cb18f2bb28b16"}, "docker": "quay.io/biocontainers/bioconductor-scran", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scran.
shpc-registry automated BioContainers addition for bioconductor-scran
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scran
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scran:1.26.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scran/1.26.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-scran/1.26.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scran-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scran-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scran-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scran-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scran-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scran-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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