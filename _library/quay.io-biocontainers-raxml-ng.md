---
layout: container
name:  "quay.io/biocontainers/raxml-ng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raxml-ng/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/raxml-ng/container.yaml"
updated_at: "2026-01-05 04:38:00.813878"
latest: "1.2.2--h6747034_2"
container_url: "https://biocontainers.pro/tools/raxml-ng"
aliases:
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
versions:
 - "1.1.0--h22e3c99_1"
 - "1.2.0--h22e3c99_0"
 - "1.1.0--h6d1f11b_3"
 - "1.2.0--h6d1f11b_1"
 - "1.2.1--h6d1f11b_0"
 - "1.2.2--h6d1f11b_0"
 - "1.2.2--h6747034_1"
 - "1.2.2--h6747034_2"
description: "shpc-registry automated BioContainers addition for raxml-ng"
config: {"url": "https://biocontainers.pro/tools/raxml-ng", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for raxml-ng", "latest": {"1.2.2--h6747034_2": "sha256:cc233f539e2e4651ac8f59a9b552b3f9cfd7091d0c2d78f31b62d3acab9268e5"}, "tags": {"1.1.0--h22e3c99_1": "sha256:1f7d3b92b50ef5e2f7ec6330cdadf41e252e878b80657b15290e57cb54e86a82", "1.2.0--h22e3c99_0": "sha256:ce0db13822ea66e9d359fb501622f7e1f83bf282f47cf4a951000f6323b4c677", "1.1.0--h6d1f11b_3": "sha256:175e69fddd618fe37c5cb311570e6e2260a086c097077feac09e57f0fb4ac4e8", "1.2.0--h6d1f11b_1": "sha256:5ebd221a3a028112e92e683931cc653534c6fd12b7168c0404fcf5d4e38155e8", "1.2.1--h6d1f11b_0": "sha256:b40c34c587fac359d2ceed60a089c2ec03caf09627313e64da090c00cad13bab", "1.2.2--h6d1f11b_0": "sha256:3a8b9c37e3690fb1bdf315dc1a16c2ff3875927fcaaf8fa2b43e605e4bd5f6e3", "1.2.2--h6747034_1": "sha256:df3dd9de9e8e02e986d6e74354844a51d9d198fbe36e76e9a2c51a6e6bf25514", "1.2.2--h6747034_2": "sha256:cc233f539e2e4651ac8f59a9b552b3f9cfd7091d0c2d78f31b62d3acab9268e5"}, "docker": "quay.io/biocontainers/raxml-ng", "aliases": {"raxml-ng": "/usr/local/bin/raxml-ng", "raxml-ng-mpi": "/usr/local/bin/raxml-ng-mpi", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/raxml-ng.
shpc-registry automated BioContainers addition for raxml-ng
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raxml-ng
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raxml-ng:1.2.2--h6747034_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raxml-ng/1.2.2--h6747034_2
$ module help quay.io/biocontainers/raxml-ng/1.2.2--h6747034_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raxml-ng-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raxml-ng-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raxml-ng-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raxml-ng-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raxml-ng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raxml-ng-inspect-deffile:

```bash
$ singularity inspect -d <container>
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