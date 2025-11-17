---
layout: container
name:  "quay.io/biocontainers/migrate-n"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/migrate-n/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/migrate-n/container.yaml"
updated_at: "2025-11-17 04:28:28.150192"
latest: "3.6.11--haf0c795_7"
container_url: "https://biocontainers.pro/tools/migrate-n"
aliases:
 - "migrate-n"
 - "migrate-n-mpi"
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
 - "3.6.11--hde308d1_4"
 - "3.6.11--hde308d1_5"
 - "3.6.11--h728fce2_6"
 - "3.6.11--haf0c795_7"
description: "shpc-registry automated BioContainers addition for migrate-n"
config: {"url": "https://biocontainers.pro/tools/migrate-n", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for migrate-n", "latest": {"3.6.11--haf0c795_7": "sha256:135132a2073f4c3a2d9ec1c769ee1b2e3ff5a1c9f213b7c7954e3a07442705a6"}, "tags": {"3.6.11--hde308d1_4": "sha256:a70dc735d72cef1097e750ee8e6b555efddb8a229e9fcfadb1e1c1b0c34e3804", "3.6.11--hde308d1_5": "sha256:81be9c38b5c26fa0c18932df05c8019aa2d698ebe2a2e1aa60e0907b26c5bf59", "3.6.11--h728fce2_6": "sha256:7eca408ede00625fc4b8a53181a7dcf692a0881de10f43f9de0e2caa4e75ddc6", "3.6.11--haf0c795_7": "sha256:135132a2073f4c3a2d9ec1c769ee1b2e3ff5a1c9f213b7c7954e3a07442705a6"}, "docker": "quay.io/biocontainers/migrate-n", "aliases": {"migrate-n": "/usr/local/bin/migrate-n", "migrate-n-mpi": "/usr/local/bin/migrate-n-mpi", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/migrate-n.
shpc-registry automated BioContainers addition for migrate-n
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/migrate-n
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/migrate-n:3.6.11--haf0c795_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/migrate-n/3.6.11--haf0c795_7
$ module help quay.io/biocontainers/migrate-n/3.6.11--haf0c795_7
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