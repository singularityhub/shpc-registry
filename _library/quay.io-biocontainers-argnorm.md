---
layout: container
name:  "quay.io/biocontainers/argnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/argnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/argnorm/container.yaml"
updated_at: "2025-08-21 03:15:37.233561"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/argnorm"
aliases:
 - "argnorm"
 - "pronto"
 - "py.test"
 - "pytest"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.2.0--pyh7cba7a3_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_1"
 - "0.7.0--pyhdfd78af_0"
 - "0.8.0--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for argnorm"
config: {"url": "https://biocontainers.pro/tools/argnorm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for argnorm", "latest": {"1.1.0--pyhdfd78af_0": "sha256:d05c922a9f62533638765434bca87f34c61fb2d697eb4f47ed77b5719c5e79af"}, "tags": {"0.2.0--pyh7cba7a3_0": "sha256:f23591e91a6394225c6e8f3527bc2d5dde35a88b6eb4d65b3f06d6b60d149f4d", "0.6.0--pyhdfd78af_0": "sha256:660423d1206726066431f892a93d06aa64e31b474ba7d98d1be4324c8ccaafe1", "0.5.0--pyhdfd78af_0": "sha256:1c388bd40271884fdb0c6afb72bb70fd6ca55b3a84b7cea2df31557945c02cba", "0.4.0--pyhdfd78af_0": "sha256:941ceb242a6b9ab4aabba22211f46e9d3a5075c8b56d4f1e298bdf73c658e9d0", "0.3.0--pyhdfd78af_0": "sha256:fdeb068082a9e5e76518634f1c6556bd37f9adac4e256c200edb7225b4303a0b", "0.2.0--pyhdfd78af_1": "sha256:7fe55a81250917eebe2c40f4563af0b96a1c6faa8769a65ba465e96cd41113c6", "0.7.0--pyhdfd78af_0": "sha256:ad4ac63f91c6b13b47c737532dae67bfa8eb215a2b22f0e4ea21a06859aedbdb", "0.8.0--pyhdfd78af_0": "sha256:9da7af55ba1173745db82684c60459740920553fc0dd32be370be26bd721ea08", "1.0.0--pyhdfd78af_0": "sha256:ae3d123d0d5d1b8ce728c40e661286f2fc4cd5fe9b56af69f1da3c23e64ba556", "1.1.0--pyhdfd78af_0": "sha256:d05c922a9f62533638765434bca87f34c61fb2d697eb4f47ed77b5719c5e79af"}, "docker": "quay.io/biocontainers/argnorm", "aliases": {"argnorm": "/usr/local/bin/argnorm", "pronto": "/usr/local/bin/pronto", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/argnorm.
singularity registry hpc automated addition for argnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/argnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/argnorm:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/argnorm/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/argnorm/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### argnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### argnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### argnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### argnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### argnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### argnorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### argnorm

```bash
$ singularity exec <container> /usr/local/bin/argnorm
$ podman run --it --rm --entrypoint /usr/local/bin/argnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/argnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pronto

```bash
$ singularity exec <container> /usr/local/bin/pronto
$ podman run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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