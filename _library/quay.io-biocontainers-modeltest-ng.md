---
layout: container
name:  "quay.io/biocontainers/modeltest-ng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/modeltest-ng/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/modeltest-ng/container.yaml"
updated_at: "2022-10-29 05:55:05.456317"
latest: "0.1.7--h5c6ebe3_0"
container_url: "https://biocontainers.pro/tools/modeltest-ng"
aliases:
 - "modeltest-ng"
 - "modeltest-ng-mpi"
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
 - "0.1.7--h5c6ebe3_0"
description: "shpc-registry automated BioContainers addition for modeltest-ng"
config: {"url": "https://biocontainers.pro/tools/modeltest-ng", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for modeltest-ng", "latest": {"0.1.7--h5c6ebe3_0": "sha256:7cc84ec52a7810e39b81e51fbeafcd19481c143dd164d7e898024577d4463d7d"}, "tags": {"0.1.7--h5c6ebe3_0": "sha256:7cc84ec52a7810e39b81e51fbeafcd19481c143dd164d7e898024577d4463d7d"}, "docker": "quay.io/biocontainers/modeltest-ng", "aliases": {"modeltest-ng": "/usr/local/bin/modeltest-ng", "modeltest-ng-mpi": "/usr/local/bin/modeltest-ng-mpi", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "mpiCC": "/usr/local/bin/mpiCC", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc", "mpicxx": "/usr/local/bin/mpicxx", "mpiexec": "/usr/local/bin/mpiexec", "mpif77": "/usr/local/bin/mpif77", "mpif90": "/usr/local/bin/mpif90", "mpifort": "/usr/local/bin/mpifort", "mpirun": "/usr/local/bin/mpirun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/modeltest-ng.
shpc-registry automated BioContainers addition for modeltest-ng
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/modeltest-ng
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/modeltest-ng:0.1.7--h5c6ebe3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/modeltest-ng/0.1.7--h5c6ebe3_0
$ module help quay.io/biocontainers/modeltest-ng/0.1.7--h5c6ebe3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### modeltest-ng-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### modeltest-ng-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### modeltest-ng-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### modeltest-ng-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### modeltest-ng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### modeltest-ng-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### modeltest-ng

```bash
$ singularity exec <container> /usr/local/bin/modeltest-ng
$ podman run --it --rm --entrypoint /usr/local/bin/modeltest-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modeltest-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### modeltest-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/modeltest-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/modeltest-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/modeltest-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
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