---
layout: container
name:  "quay.io/biocontainers/mrbayes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mrbayes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mrbayes/container.yaml"
updated_at: "2025-08-18 03:48:22.835638"
latest: "3.2.7--hd0d793b_7"
container_url: "https://biocontainers.pro/tools/mrbayes"
aliases:
 - "mb"
 - "mb-mpi"
 - "giffilter"
 - "gifsponge"
 - "gifecho"
 - "gifinto"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "mpiCC"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
versions:
 - "3.2.7--h5465cc4_4"
 - "3.2.7--h5465cc4_5"
 - "3.2.7--h1b649f3_6"
 - "3.2.7--hd0d793b_7"
description: "shpc-registry automated BioContainers addition for mrbayes"
config: {"url": "https://biocontainers.pro/tools/mrbayes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mrbayes", "latest": {"3.2.7--hd0d793b_7": "sha256:070cd4f75e3a2bd7e91448539364eb89104d6463a54564bada233142ab70f965"}, "tags": {"3.2.7--h5465cc4_4": "sha256:c07cbbd563dec595ac4bf4aaedd87ce4c0fcc548ff92bc48a8a7d5cd151ec0a1", "3.2.7--h5465cc4_5": "sha256:ca5b56f1e49aa32ed0b64d2a58cbd61378145df6e483324c03b9faa0b3b163ad", "3.2.7--h1b649f3_6": "sha256:c287b75d5e22fe45f98440575e66a678b5c68a5d96885d611e526e4dc4c1a288", "3.2.7--hd0d793b_7": "sha256:070cd4f75e3a2bd7e91448539364eb89104d6463a54564bada233142ab70f965"}, "docker": "quay.io/biocontainers/mrbayes", "aliases": {"mb": "/usr/local/bin/mb", "mb-mpi": "/usr/local/bin/mb-mpi", "giffilter": "/usr/local/bin/giffilter", "gifsponge": "/usr/local/bin/gifsponge", "gifecho": "/usr/local/bin/gifecho", "gifinto": "/usr/local/bin/gifinto", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mrbayes.
shpc-registry automated BioContainers addition for mrbayes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mrbayes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mrbayes:3.2.7--hd0d793b_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mrbayes/3.2.7--hd0d793b_7
$ module help quay.io/biocontainers/mrbayes/3.2.7--hd0d793b_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mrbayes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mrbayes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mrbayes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mrbayes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mrbayes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mrbayes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mb

```bash
$ singularity exec <container> /usr/local/bin/mb
$ podman run --it --rm --entrypoint /usr/local/bin/mb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mb-mpi

```bash
$ singularity exec <container> /usr/local/bin/mb-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/mb-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mb-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffilter

```bash
$ singularity exec <container> /usr/local/bin/giffilter
$ podman run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifsponge

```bash
$ singularity exec <container> /usr/local/bin/gifsponge
$ podman run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifsponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifecho

```bash
$ singularity exec <container> /usr/local/bin/gifecho
$ podman run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifecho   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifinto

```bash
$ singularity exec <container> /usr/local/bin/gifinto
$ podman run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifinto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile2mat.pl

```bash
$ singularity exec <container> /usr/local/bin/profile2mat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiCC

```bash
$ singularity exec <container> /usr/local/bin/mpiCC
$ podman run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-clean

```bash
$ singularity exec <container> /usr/local/bin/ompi-clean
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-server

```bash
$ singularity exec <container> /usr/local/bin/ompi-server
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi_info

```bash
$ singularity exec <container> /usr/local/bin/ompi_info
$ podman run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
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