---
layout: container
name:  "quay.io/biocontainers/fastphylo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastphylo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastphylo/container.yaml"
updated_at: "2022-10-29 05:52:38.742316"
latest: "1.0.3--h648b6df_5"
container_url: "https://biocontainers.pro/tools/fastphylo"
aliases:
 - "fastdist"
 - "fastprot"
 - "fastprot_mpi"
 - "fnj"
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
 - "1.0.3--h648b6df_5"
description: "shpc-registry automated BioContainers addition for fastphylo"
config: {"url": "https://biocontainers.pro/tools/fastphylo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastphylo", "latest": {"1.0.3--h648b6df_5": "sha256:6e9756acdd3d68fdc034a4fe7dece58dc23c8c78d41fb1661c11aa794a33a130"}, "tags": {"1.0.3--h648b6df_5": "sha256:6e9756acdd3d68fdc034a4fe7dece58dc23c8c78d41fb1661c11aa794a33a130"}, "docker": "quay.io/biocontainers/fastphylo", "aliases": {"fastdist": "/usr/local/bin/fastdist", "fastprot": "/usr/local/bin/fastprot", "fastprot_mpi": "/usr/local/bin/fastprot_mpi", "fnj": "/usr/local/bin/fnj", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "mpiCC": "/usr/local/bin/mpiCC", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc", "mpicxx": "/usr/local/bin/mpicxx", "mpiexec": "/usr/local/bin/mpiexec", "mpif77": "/usr/local/bin/mpif77", "mpif90": "/usr/local/bin/mpif90", "mpifort": "/usr/local/bin/mpifort", "mpirun": "/usr/local/bin/mpirun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastphylo.
shpc-registry automated BioContainers addition for fastphylo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastphylo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastphylo:1.0.3--h648b6df_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastphylo/1.0.3--h648b6df_5
$ module help quay.io/biocontainers/fastphylo/1.0.3--h648b6df_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastphylo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastphylo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastphylo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastphylo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastphylo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastphylo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastdist

```bash
$ singularity exec <container> /usr/local/bin/fastdist
$ podman run --it --rm --entrypoint /usr/local/bin/fastdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastprot

```bash
$ singularity exec <container> /usr/local/bin/fastprot
$ podman run --it --rm --entrypoint /usr/local/bin/fastprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastprot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastprot_mpi

```bash
$ singularity exec <container> /usr/local/bin/fastprot_mpi
$ podman run --it --rm --entrypoint /usr/local/bin/fastprot_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastprot_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fnj

```bash
$ singularity exec <container> /usr/local/bin/fnj
$ podman run --it --rm --entrypoint /usr/local/bin/fnj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fnj   -v ${PWD} -w ${PWD} <container> -c " $@"
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