---
layout: container
name:  "quay.io/biocontainers/bioconductor-dnashaper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dnashaper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dnashaper/container.yaml"
updated_at: "2024-02-25 02:43:29.878520"
latest: "1.30.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dnashaper"
aliases:
 - "wget"
versions:
 - "1.8.0--r351hfc679d8_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dnashaper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dnashaper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dnashaper", "latest": {"1.30.0--r43hf17093f_0": "sha256:9d2a3f28d23f3d2176e3cd8a06f67e522f46954be853435474010217c4636fe1"}, "tags": {"1.8.0--r351hfc679d8_0": "sha256:ce797282afc1a6d1f99ec0f0bc8cdbee47126c958e8ef8c1dc031b070200a897", "1.26.0--r42hc247a5b_0": "sha256:fc4fb4be2dd75e600b22dabaf576bf01c0e6e7130d7a97ec7b53d1f10ef7a8f1", "1.22.0--r41hc247a5b_2": "sha256:b181907c79d518a07e703c17491d41489b4919d74899da630d0f21d530829fa2", "1.20.0--r41h399db7b_0": "sha256:001f81dae9656fc4bf7571d8626eb40bdeb947284b396b5db3bc8877282f99a0", "1.18.0--r40h399db7b_1": "sha256:feb4132c0fcfa0697976807d52165faba302f052d07f82c3761d9b28c06857ff", "1.16.0--r40h5f743cb_0": "sha256:3f38cb66fb6a0a5d6a18a41c968c15be6b6c18d56dd7fdf4ec8dfc1bf3e5f7bb", "1.26.0--r42hf17093f_1": "sha256:ff76f1b7a1cacf976a9b914bc90fe361e65b1c41254c92f8f0204f7aa41a245b", "1.28.0--r43hf17093f_0": "sha256:53bc1519be67e4dc1857b5196dda4ac34db7ed752d6f43570f4b95e982fd472e", "1.30.0--r43hf17093f_0": "sha256:9d2a3f28d23f3d2176e3cd8a06f67e522f46954be853435474010217c4636fe1"}, "docker": "quay.io/biocontainers/bioconductor-dnashaper", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dnashaper.
shpc-registry automated BioContainers addition for bioconductor-dnashaper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dnashaper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dnashaper:1.30.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dnashaper/1.30.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-dnashaper/1.30.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dnashaper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnashaper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dnashaper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dnashaper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dnashaper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dnashaper-inspect-deffile:

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