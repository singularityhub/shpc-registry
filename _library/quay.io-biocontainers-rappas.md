---
layout: container
name:  "quay.io/biocontainers/rappas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rappas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rappas/container.yaml"
updated_at: "2023-02-22 03:06:43.349430"
latest: "1.21--0"
container_url: "https://biocontainers.pro/tools/rappas"
aliases:
 - "RAPPAS.jar"
 - "phyml"
 - "phyml-mpi"
 - "phyrex"
 - "phytime"
 - "rappas"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "mpiCC"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
 - "opal_wrapper"
 - "orte-clean"
 - "orte-info"
 - "orte-server"
versions:
 - "1.21--0"
description: "shpc-registry automated BioContainers addition for rappas"
config: {"url": "https://biocontainers.pro/tools/rappas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rappas", "latest": {"1.21--0": "sha256:99e868752e0efe443814a465632b8fd169896e5d72e220e34e2d57ecb466d8bf"}, "tags": {"1.21--0": "sha256:99e868752e0efe443814a465632b8fd169896e5d72e220e34e2d57ecb466d8bf"}, "docker": "quay.io/biocontainers/rappas", "aliases": {"RAPPAS.jar": "/usr/local/bin/RAPPAS.jar", "phyml": "/usr/local/bin/phyml", "phyml-mpi": "/usr/local/bin/phyml-mpi", "phyrex": "/usr/local/bin/phyrex", "phytime": "/usr/local/bin/phytime", "rappas": "/usr/local/bin/rappas", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rappas.
shpc-registry automated BioContainers addition for rappas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rappas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rappas:1.21--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rappas/1.21--0
$ module help quay.io/biocontainers/rappas/1.21--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rappas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rappas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rappas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rappas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rappas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rappas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RAPPAS.jar

```bash
$ singularity exec <container> /usr/local/bin/RAPPAS.jar
$ podman run --it --rm --entrypoint /usr/local/bin/RAPPAS.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RAPPAS.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyml

```bash
$ singularity exec <container> /usr/local/bin/phyml
$ podman run --it --rm --entrypoint /usr/local/bin/phyml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyml-mpi

```bash
$ singularity exec <container> /usr/local/bin/phyml-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/phyml-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyml-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phyrex

```bash
$ singularity exec <container> /usr/local/bin/phyrex
$ podman run --it --rm --entrypoint /usr/local/bin/phyrex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phyrex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phytime

```bash
$ singularity exec <container> /usr/local/bin/phytime
$ podman run --it --rm --entrypoint /usr/local/bin/phytime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phytime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rappas

```bash
$ singularity exec <container> /usr/local/bin/rappas
$ podman run --it --rm --entrypoint /usr/local/bin/rappas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rappas   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### opal_wrapper

```bash
$ singularity exec <container> /usr/local/bin/opal_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-clean

```bash
$ singularity exec <container> /usr/local/bin/orte-clean
$ podman run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-info

```bash
$ singularity exec <container> /usr/local/bin/orte-info
$ podman run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-server

```bash
$ singularity exec <container> /usr/local/bin/orte-server
$ podman run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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