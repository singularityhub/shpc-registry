---
layout: container
name:  "quay.io/biocontainers/pronto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pronto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pronto/container.yaml"
updated_at: "2024-10-05 03:09:05.705442"
latest: "2.5.7--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pronto"
aliases:
 - "x86_64-conda_cos7-linux-gnu-ld"
 - "chardetect"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "2.5.1--pyhdfd78af_0"
 - "2.5.2--pyhdfd78af_0"
 - "2.5.3--pyhdfd78af_0"
 - "2.5.4--pyhdfd78af_0"
 - "2.5.5--pyhdfd78af_0"
 - "2.5.6--pyhdfd78af_0"
 - "2.5.7--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pronto"
config: {"url": "https://biocontainers.pro/tools/pronto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pronto", "latest": {"2.5.7--pyhdfd78af_0": "sha256:799e2450a7d9f9bb153d8e0e6be50e2788aacc30525ff311ed7f34acb72438c9"}, "tags": {"2.5.1--pyhdfd78af_0": "sha256:639b5301b7af8ebac01c28673852f49df0c565fdfe63232824a25af2bc9702d6", "2.5.2--pyhdfd78af_0": "sha256:6a403584a79512fb0a02c2cbe7eb548531164ee5f35cb6371c7ab10e4bafed96", "2.5.3--pyhdfd78af_0": "sha256:3bd8bf9b2571a15636117f90f05b919762226379e6b21674202d2abc9aaf3d89", "2.5.4--pyhdfd78af_0": "sha256:9b4ca03021b47ab0c57ae778d56aecbd23907532205df2bea2c33b7e08446650", "2.5.5--pyhdfd78af_0": "sha256:de1c639da68cb0834c9bc867cd4aba122c6840730d7e5e4d58196dde8c04f3f9", "2.5.6--pyhdfd78af_0": "sha256:9b171a0697ccede6209a936eee1953f60533e37903201e44b1611c0c21b2c58d", "2.5.7--pyhdfd78af_0": "sha256:799e2450a7d9f9bb153d8e0e6be50e2788aacc30525ff311ed7f34acb72438c9"}, "docker": "quay.io/biocontainers/pronto", "aliases": {"x86_64-conda_cos7-linux-gnu-ld": "/usr/local/bin/x86_64-conda_cos7-linux-gnu-ld", "chardetect": "/usr/local/bin/chardetect", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pronto.
shpc-registry automated BioContainers addition for pronto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pronto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pronto:2.5.7--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pronto/2.5.7--pyhdfd78af_0
$ module help quay.io/biocontainers/pronto/2.5.7--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pronto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pronto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pronto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pronto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pronto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pronto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda_cos7-linux-gnu-ld

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos7-linux-gnu-ld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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