---
layout: container
name:  "quay.io/biocontainers/revbayes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/revbayes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/revbayes/container.yaml"
updated_at: "2024-09-26 10:38:24.892095"
latest: "1.0.13--hdf94a1f_7"
container_url: "https://biocontainers.pro/tools/revbayes"
aliases:
 - "rb"
 - "rb-mpi"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
 - "oshrun"
versions:
 - "1.0.13--h105e827_5"
 - "1.0.13--hdf94a1f_7"
description: "shpc-registry automated BioContainers addition for revbayes"
config: {"url": "https://biocontainers.pro/tools/revbayes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for revbayes", "latest": {"1.0.13--hdf94a1f_7": "sha256:d677b591ea546f9db2f2dfb947bd63c52f8e47fed4f8455c6830fe3b81d401f8"}, "tags": {"1.0.13--h105e827_5": "sha256:b36ea89b8ad6f695ccea031d451e58912de27299ca7ce9e31f96a7789b1fd428", "1.0.13--hdf94a1f_7": "sha256:d677b591ea546f9db2f2dfb947bd63c52f8e47fed4f8455c6830fe3b81d401f8"}, "docker": "quay.io/biocontainers/revbayes", "aliases": {"rb": "/usr/local/bin/rb", "rb-mpi": "/usr/local/bin/rb-mpi", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/revbayes.
shpc-registry automated BioContainers addition for revbayes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/revbayes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/revbayes:1.0.13--hdf94a1f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/revbayes/1.0.13--hdf94a1f_7
$ module help quay.io/biocontainers/revbayes/1.0.13--hdf94a1f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### revbayes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### revbayes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### revbayes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### revbayes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### revbayes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### revbayes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rb

```bash
$ singularity exec <container> /usr/local/bin/rb
$ podman run --it --rm --entrypoint /usr/local/bin/rb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rb-mpi

```bash
$ singularity exec <container> /usr/local/bin/rb-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/rb-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rb-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshrun

```bash
$ singularity exec <container> /usr/local/bin/oshrun
$ podman run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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