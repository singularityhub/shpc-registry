---
layout: container
name:  "quay.io/biocontainers/seqfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqfold/container.yaml"
updated_at: "2026-02-01 04:43:19.224275"
latest: "0.9.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/seqfold"
aliases:
 - "seqfold"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.7.17--pyhdfd78af_0"
 - "0.9.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for seqfold"
config: {"url": "https://biocontainers.pro/tools/seqfold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for seqfold", "latest": {"0.9.0--pyhdfd78af_0": "sha256:51aceef14d254dd488d9c59f707a1877c0c298cf153a28c6b93d6dc8a2ea17b7"}, "tags": {"0.7.17--pyhdfd78af_0": "sha256:a4a58f46c9f6ff9a0ea36bab8cfd6809d2b5ac115f7d94ac99a328c5b52b9671", "0.9.0--pyhdfd78af_0": "sha256:51aceef14d254dd488d9c59f707a1877c0c298cf153a28c6b93d6dc8a2ea17b7"}, "docker": "quay.io/biocontainers/seqfold", "aliases": {"seqfold": "/usr/local/bin/seqfold", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqfold.
singularity registry hpc automated addition for seqfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqfold:0.9.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqfold/0.9.0--pyhdfd78af_0
$ module help quay.io/biocontainers/seqfold/0.9.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqfold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqfold

```bash
$ singularity exec <container> /usr/local/bin/seqfold
$ podman run --it --rm --entrypoint /usr/local/bin/seqfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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