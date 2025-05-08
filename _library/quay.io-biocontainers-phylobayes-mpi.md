---
layout: container
name:  "quay.io/biocontainers/phylobayes-mpi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylobayes-mpi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylobayes-mpi/container.yaml"
updated_at: "2025-05-08 03:43:52.501247"
latest: "1.9--hf316886_3"
container_url: "https://biocontainers.pro/tools/phylobayes-mpi"
aliases:
 - "bpcomp"
 - "cvrep"
 - "io_demo"
 - "pb_mpi"
 - "readpb_mpi"
 - "tracecomp"
 - "ucx_info"
 - "ucx_perftest"
 - "ucx_read_profile"
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
 - "1.9--h5c6ebe3_0"
 - "1.9--h103dbdd_2"
 - "1.9--hf316886_3"
description: "shpc-registry automated BioContainers addition for phylobayes-mpi"
config: {"url": "https://biocontainers.pro/tools/phylobayes-mpi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylobayes-mpi", "latest": {"1.9--hf316886_3": "sha256:44379c21734e14f9fa3941817a778fcc3ef50018daf247fda4afea5167ac0f88"}, "tags": {"1.9--h5c6ebe3_0": "sha256:59cea55c90b867a650fdbcf1935c621a4a37daca90aba2c4e4317777a626fae5", "1.9--h103dbdd_2": "sha256:d3b7cba604d7816ed2efef76a99a01ec2a220cda6ade2dc025040a5d35492495", "1.9--hf316886_3": "sha256:44379c21734e14f9fa3941817a778fcc3ef50018daf247fda4afea5167ac0f88"}, "docker": "quay.io/biocontainers/phylobayes-mpi", "aliases": {"bpcomp": "/usr/local/bin/bpcomp", "cvrep": "/usr/local/bin/cvrep", "io_demo": "/usr/local/bin/io_demo", "pb_mpi": "/usr/local/bin/pb_mpi", "readpb_mpi": "/usr/local/bin/readpb_mpi", "tracecomp": "/usr/local/bin/tracecomp", "ucx_info": "/usr/local/bin/ucx_info", "ucx_perftest": "/usr/local/bin/ucx_perftest", "ucx_read_profile": "/usr/local/bin/ucx_read_profile", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylobayes-mpi.
shpc-registry automated BioContainers addition for phylobayes-mpi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylobayes-mpi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylobayes-mpi:1.9--hf316886_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylobayes-mpi/1.9--hf316886_3
$ module help quay.io/biocontainers/phylobayes-mpi/1.9--hf316886_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylobayes-mpi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylobayes-mpi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylobayes-mpi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylobayes-mpi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylobayes-mpi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylobayes-mpi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bpcomp

```bash
$ singularity exec <container> /usr/local/bin/bpcomp
$ podman run --it --rm --entrypoint /usr/local/bin/bpcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cvrep

```bash
$ singularity exec <container> /usr/local/bin/cvrep
$ podman run --it --rm --entrypoint /usr/local/bin/cvrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cvrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_demo

```bash
$ singularity exec <container> /usr/local/bin/io_demo
$ podman run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pb_mpi

```bash
$ singularity exec <container> /usr/local/bin/pb_mpi
$ podman run --it --rm --entrypoint /usr/local/bin/pb_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pb_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readpb_mpi

```bash
$ singularity exec <container> /usr/local/bin/readpb_mpi
$ podman run --it --rm --entrypoint /usr/local/bin/readpb_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readpb_mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tracecomp

```bash
$ singularity exec <container> /usr/local/bin/tracecomp
$ podman run --it --rm --entrypoint /usr/local/bin/tracecomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracecomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_info

```bash
$ singularity exec <container> /usr/local/bin/ucx_info
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_read_profile

```bash
$ singularity exec <container> /usr/local/bin/ucx_read_profile
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
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