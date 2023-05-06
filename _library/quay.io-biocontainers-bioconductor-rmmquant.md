---
layout: container
name:  "quay.io/biocontainers/bioconductor-rmmquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rmmquant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rmmquant/container.yaml"
updated_at: "2023-05-06 02:50:46.596817"
latest: "1.16.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rmmquant"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.1--r40h399db7b_0"
 - "1.16.0--r42hc247a5b_0"
 - "1.12.0--r41hc247a5b_2"
 - "1.10.0--r41h399db7b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rmmquant"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rmmquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rmmquant", "latest": {"1.16.0--r42hc247a5b_0": "sha256:e8451b9264fb9966cceb59acb48ff8c1d0ca32fa7780995e1ccb9df00c7ff947"}, "tags": {"1.8.1--r40h399db7b_0": "sha256:ac4b5f7ceaa43bc4f6d80aec632eecb0821b3b525fd32a124349daa9d2d9e401", "1.16.0--r42hc247a5b_0": "sha256:e8451b9264fb9966cceb59acb48ff8c1d0ca32fa7780995e1ccb9df00c7ff947", "1.12.0--r41hc247a5b_2": "sha256:eeba87e7a56f2b3e89f4274759aea875ab271eb85a1bb86aa424e08d2e679739", "1.10.0--r41h399db7b_0": "sha256:3fd8f53dcd6b56e4a9aa38bb3324b3cdaaf1e9c2126ceee8aed3722fdff08337"}, "docker": "quay.io/biocontainers/bioconductor-rmmquant", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rmmquant.
shpc-registry automated BioContainers addition for bioconductor-rmmquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rmmquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rmmquant:1.16.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rmmquant/1.16.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-rmmquant/1.16.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rmmquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmmquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmmquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rmmquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rmmquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rmmquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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