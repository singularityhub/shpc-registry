---
layout: container
name:  "quay.io/biocontainers/kissplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kissplice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kissplice/container.yaml"
updated_at: "2025-12-24 03:34:16.120914"
latest: "2.6.5--h077b44d_1"
container_url: "https://biocontainers.pro/tools/kissplice"
aliases:
 - "bcalm"
 - "kissplice"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
 - "h5cc"
versions:
 - "2.5.5--h5b5514e_0"
 - "2.5.5--h43eeafb_2"
 - "2.6.2--hdcf5f25_0"
 - "2.6.5--hdcf5f25_0"
 - "2.6.5--h077b44d_1"
description: "shpc-registry automated BioContainers addition for kissplice"
config: {"url": "https://biocontainers.pro/tools/kissplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kissplice", "latest": {"2.6.5--h077b44d_1": "sha256:3b368cf0be886385068fb7635c667a5b911f68906a74e7eabf1ff56ee12355b8"}, "tags": {"2.5.5--h5b5514e_0": "sha256:bd7e29a41f935f295d7e9c3d39f8ab1377e5e1e3663db7175ddf75fa9ef323e1", "2.5.5--h43eeafb_2": "sha256:073687d2a67acf1a02a2b9b68c5453b98d524f36943416cfab5a788af8ba5878", "2.6.2--hdcf5f25_0": "sha256:f9eb8ae3b29d69b07979144444b63d73d9ea68c1d3e308c133c507cabf51d923", "2.6.5--hdcf5f25_0": "sha256:01a3fd6803f2641c2a3160790def1e8a35fdd3470f5e42c5703686843ae528aa", "2.6.5--h077b44d_1": "sha256:3b368cf0be886385068fb7635c667a5b911f68906a74e7eabf1ff56ee12355b8"}, "docker": "quay.io/biocontainers/kissplice", "aliases": {"bcalm": "/usr/local/bin/bcalm", "kissplice": "/usr/local/bin/kissplice", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "h5cc": "/usr/local/bin/h5cc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kissplice.
shpc-registry automated BioContainers addition for kissplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kissplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kissplice:2.6.5--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kissplice/2.6.5--h077b44d_1
$ module help quay.io/biocontainers/kissplice/2.6.5--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kissplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kissplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kissplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kissplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kissplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kissplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcalm

```bash
$ singularity exec <container> /usr/local/bin/bcalm
$ podman run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcalm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kissplice

```bash
$ singularity exec <container> /usr/local/bin/kissplice
$ podman run --it --rm --entrypoint /usr/local/bin/kissplice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kissplice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
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