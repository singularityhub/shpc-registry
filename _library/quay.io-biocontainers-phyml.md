---
layout: container
name:  "quay.io/biocontainers/phyml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phyml/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phyml/container.yaml"
updated_at: "2022-10-29 05:43:27.455620"
latest: "3.3.20211231--hee9e358_0"
container_url: "https://biocontainers.pro/tools/phyml"
aliases:
 - "phyml"
 - "phyml-mpi"
 - "phyrex"
 - "phytime"
 - "aggregate_profile.pl"
 - "mpiCC"
 - "mpic++"
 - "mpicc"
 - "mpicxx"
 - "mpiexec"
 - "mpif77"
 - "mpif90"
 - "mpifort"
 - "mpirun"
versions:
 - "3.3.20211231--hee9e358_0"
description: "shpc-registry automated BioContainers addition for phyml"
config: {"url": "https://biocontainers.pro/tools/phyml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phyml", "latest": {"3.3.20211231--hee9e358_0": "sha256:1be3026768229e8f439fbb3357f1a13f8c4706378daaa35a0a646816a61a880f"}, "tags": {"3.3.20211231--hee9e358_0": "sha256:1be3026768229e8f439fbb3357f1a13f8c4706378daaa35a0a646816a61a880f"}, "docker": "quay.io/biocontainers/phyml", "aliases": {"phyml": "/usr/local/bin/phyml", "phyml-mpi": "/usr/local/bin/phyml-mpi", "phyrex": "/usr/local/bin/phyrex", "phytime": "/usr/local/bin/phytime", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "mpiCC": "/usr/local/bin/mpiCC", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc", "mpicxx": "/usr/local/bin/mpicxx", "mpiexec": "/usr/local/bin/mpiexec", "mpif77": "/usr/local/bin/mpif77", "mpif90": "/usr/local/bin/mpif90", "mpifort": "/usr/local/bin/mpifort", "mpirun": "/usr/local/bin/mpirun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phyml.
shpc-registry automated BioContainers addition for phyml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phyml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phyml:3.3.20211231--hee9e358_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phyml/3.3.20211231--hee9e358_0
$ module help quay.io/biocontainers/phyml/3.3.20211231--hee9e358_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phyml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phyml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phyml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phyml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phyml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phyml-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiCC

```bash
$ singularity exec <container> /usr/local/bin/mpiCC
$ podman run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpic++

```bash
$ singularity exec <container> /usr/local/bin/mpic++
$ podman run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicc

```bash
$ singularity exec <container> /usr/local/bin/mpicc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicxx

```bash
$ singularity exec <container> /usr/local/bin/mpicxx
$ podman run --it --rm --entrypoint /usr/local/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec

```bash
$ singularity exec <container> /usr/local/bin/mpiexec
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpif77

```bash
$ singularity exec <container> /usr/local/bin/mpif77
$ podman run --it --rm --entrypoint /usr/local/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpif90

```bash
$ singularity exec <container> /usr/local/bin/mpif90
$ podman run --it --rm --entrypoint /usr/local/bin/mpif90   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpif90   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpifort

```bash
$ singularity exec <container> /usr/local/bin/mpifort
$ podman run --it --rm --entrypoint /usr/local/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpirun

```bash
$ singularity exec <container> /usr/local/bin/mpirun
$ podman run --it --rm --entrypoint /usr/local/bin/mpirun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpirun   -v ${PWD} -w ${PWD} <container> -c " $@"
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