---
layout: container
name:  "quay.io/pawsey/namd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/namd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/pawsey/namd/container.yaml"
updated_at: "2026-01-08 03:43:19.658959"
latest: "3.0.1-rocm6.3.0"
container_url: "https://singularity-hpc.readthedocs.io"
aliases:
 - "charmrun"
 - "namd3"
versions:
 - "3.0.1-rocm6.3.0"
 - "3.0.1"
description: "Pawsey build of NAMD built on top of MPICH and ROCm"
config: {"docker": "quay.io/pawsey/namd", "url": "https://singularity-hpc.readthedocs.io", "description": "Pawsey build of NAMD built on top of MPICH and ROCm", "maintainer": "@craigmeyer", "latest": {"3.0.1-rocm6.3.0": "sha256:1098a0896521eaa2929fc72738b213c797199a3f885ada35fe17e35ba0ecc1fd"}, "tags": {"3.0.1-rocm6.3.0": "sha256:1098a0896521eaa2929fc72738b213c797199a3f885ada35fe17e35ba0ecc1fd", "3.0.1": "sha256:256fd50371294ef26c5f277e508e6986c7c2bf9853771c5c6f02b7886f8e07c2"}, "aliases": {"charmrun": "/opt/namd/bin/charmrun", "namd3": "/opt/namd/bin/namd3"}}
---

This module is a singularity container wrapper for quay.io/pawsey/namd.
Pawsey build of NAMD built on top of MPICH and ROCm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/namd
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/namd:3.0.1-rocm6.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/namd/3.0.1-rocm6.3.0
$ module help quay.io/pawsey/namd/3.0.1-rocm6.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### namd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### namd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### namd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### namd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### namd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### namd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### charmrun

```bash
$ singularity exec <container> /opt/namd/bin/charmrun
$ podman run --it --rm --entrypoint /opt/namd/bin/charmrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/namd/bin/charmrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### namd3

```bash
$ singularity exec <container> /opt/namd/bin/namd3
$ podman run --it --rm --entrypoint /opt/namd/bin/namd3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/namd/bin/namd3   -v ${PWD} -w ${PWD} <container> -c " $@"
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