---
layout: container
name:  "quay.io/biocontainers/migrate-n"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/migrate-n/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/migrate-n/container.yaml"
updated_at: "2022-10-29 05:33:48.507579"
latest: "3.6.11--hde308d1_4"
container_url: "https://biocontainers.pro/tools/migrate-n"
aliases:
 - "migrate-n"
 - "migrate-n-mpi"
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
 - "3.6.11--hde308d1_4"
description: "shpc-registry automated BioContainers addition for migrate-n"
config: {"url": "https://biocontainers.pro/tools/migrate-n", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for migrate-n", "latest": {"3.6.11--hde308d1_4": "sha256:a70dc735d72cef1097e750ee8e6b555efddb8a229e9fcfadb1e1c1b0c34e3804"}, "tags": {"3.6.11--hde308d1_4": "sha256:a70dc735d72cef1097e750ee8e6b555efddb8a229e9fcfadb1e1c1b0c34e3804"}, "docker": "quay.io/biocontainers/migrate-n", "aliases": {"migrate-n": "/usr/local/bin/migrate-n", "migrate-n-mpi": "/usr/local/bin/migrate-n-mpi", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "mpiCC": "/usr/local/bin/mpiCC", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc", "mpicxx": "/usr/local/bin/mpicxx", "mpiexec": "/usr/local/bin/mpiexec", "mpif77": "/usr/local/bin/mpif77", "mpif90": "/usr/local/bin/mpif90", "mpifort": "/usr/local/bin/mpifort", "mpirun": "/usr/local/bin/mpirun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/migrate-n.
shpc-registry automated BioContainers addition for migrate-n
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/migrate-n
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/migrate-n:3.6.11--hde308d1_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/migrate-n/3.6.11--hde308d1_4
$ module help quay.io/biocontainers/migrate-n/3.6.11--hde308d1_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### migrate-n-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### migrate-n-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### migrate-n-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### migrate-n-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### migrate-n-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### migrate-n-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### migrate-n

```bash
$ singularity exec <container> /usr/local/bin/migrate-n
$ podman run --it --rm --entrypoint /usr/local/bin/migrate-n   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migrate-n   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### migrate-n-mpi

```bash
$ singularity exec <container> /usr/local/bin/migrate-n-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/migrate-n-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/migrate-n-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
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