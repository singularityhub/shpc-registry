---
layout: container
name:  "quay.io/biocontainers/ipk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ipk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ipk/container.yaml"
updated_at: "2025-11-26 04:02:01.984173"
latest: "0.5.1--h077b44d_4"
container_url: "https://biocontainers.pro/tools/ipk"
aliases:
 - "ipk-aa"
 - "ipk-aa-pos"
 - "ipk-dna"
 - "ipk.py"
 - "ipkdiff-aa"
 - "ipkdiff-dna"
 - "ipkdump-aa"
 - "ipkdump-dna"
 - "phyml"
 - "phyml-mpi"
 - "phytime"
 - "raxml-ng"
 - "raxml-ng-mpi"
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
 - "shmemcc"
 - "shmemfort"
 - "shmemrun"
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
 - "ortecc"
 - "orted"
versions:
 - "0.5.1--hdcf5f25_0"
 - "0.5.1--hdcf5f25_2"
 - "0.5.1--h077b44d_3"
 - "0.5.1--h077b44d_4"
description: "singularity registry hpc automated addition for ipk"
config: {"url": "https://biocontainers.pro/tools/ipk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ipk", "latest": {"0.5.1--h077b44d_4": "sha256:b5850a4bd21abae65678c0280c6a4c186747802b4b04a23a6c904db7c173077d"}, "tags": {"0.5.1--hdcf5f25_0": "sha256:bd17de5540f03275b2b4d69c8757d04822791d5e9e82a74fe5124b755b80580a", "0.5.1--hdcf5f25_2": "sha256:cda0c82182b78da0c4830605897c4d4444f2bd0e646dbb5ab3679725897473fb", "0.5.1--h077b44d_3": "sha256:ca475c55b7967bfbb03bfc80348438f357aa1ec6cec140f8bab36331c232fa4e", "0.5.1--h077b44d_4": "sha256:b5850a4bd21abae65678c0280c6a4c186747802b4b04a23a6c904db7c173077d"}, "docker": "quay.io/biocontainers/ipk", "aliases": {"ipk-aa": "/usr/local/bin/ipk-aa", "ipk-aa-pos": "/usr/local/bin/ipk-aa-pos", "ipk-dna": "/usr/local/bin/ipk-dna", "ipk.py": "/usr/local/bin/ipk.py", "ipkdiff-aa": "/usr/local/bin/ipkdiff-aa", "ipkdiff-dna": "/usr/local/bin/ipkdiff-dna", "ipkdump-aa": "/usr/local/bin/ipkdump-aa", "ipkdump-dna": "/usr/local/bin/ipkdump-dna", "phyml": "/usr/local/bin/phyml", "phyml-mpi": "/usr/local/bin/phyml-mpi", "phytime": "/usr/local/bin/phytime", "raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc", "shmemfort": "/usr/local/bin/shmemfort", "shmemrun": "/usr/local/bin/shmemrun", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server", "ortecc": "/usr/local/bin/ortecc", "orted": "/usr/local/bin/orted"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ipk.
singularity registry hpc automated addition for ipk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ipk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ipk:0.5.1--h077b44d_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ipk/0.5.1--h077b44d_4
$ module help quay.io/biocontainers/ipk/0.5.1--h077b44d_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ipk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ipk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ipk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ipk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ipk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ipk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ipk-aa

```bash
$ singularity exec <container> /usr/local/bin/ipk-aa
$ podman run --it --rm --entrypoint /usr/local/bin/ipk-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipk-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipk-aa-pos

```bash
$ singularity exec <container> /usr/local/bin/ipk-aa-pos
$ podman run --it --rm --entrypoint /usr/local/bin/ipk-aa-pos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipk-aa-pos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipk-dna

```bash
$ singularity exec <container> /usr/local/bin/ipk-dna
$ podman run --it --rm --entrypoint /usr/local/bin/ipk-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipk-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipk.py

```bash
$ singularity exec <container> /usr/local/bin/ipk.py
$ podman run --it --rm --entrypoint /usr/local/bin/ipk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipkdiff-aa

```bash
$ singularity exec <container> /usr/local/bin/ipkdiff-aa
$ podman run --it --rm --entrypoint /usr/local/bin/ipkdiff-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipkdiff-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipkdiff-dna

```bash
$ singularity exec <container> /usr/local/bin/ipkdiff-dna
$ podman run --it --rm --entrypoint /usr/local/bin/ipkdiff-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipkdiff-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipkdump-aa

```bash
$ singularity exec <container> /usr/local/bin/ipkdump-aa
$ podman run --it --rm --entrypoint /usr/local/bin/ipkdump-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipkdump-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipkdump-dna

```bash
$ singularity exec <container> /usr/local/bin/ipkdump-dna
$ podman run --it --rm --entrypoint /usr/local/bin/ipkdump-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipkdump-dna   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### phytime

```bash
$ singularity exec <container> /usr/local/bin/phytime
$ podman run --it --rm --entrypoint /usr/local/bin/phytime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phytime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxml-ng-mpi

```bash
$ singularity exec <container> /usr/local/bin/raxml-ng-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxml-ng-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### shmemcc

```bash
$ singularity exec <container> /usr/local/bin/shmemcc
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemfort

```bash
$ singularity exec <container> /usr/local/bin/shmemfort
$ podman run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ortecc

```bash
$ singularity exec <container> /usr/local/bin/ortecc
$ podman run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orted

```bash
$ singularity exec <container> /usr/local/bin/orted
$ podman run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
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