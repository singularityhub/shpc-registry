---
layout: container
name:  "quay.io/biocontainers/pybarrnap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pybarrnap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pybarrnap/container.yaml"
updated_at: "2025-04-07 03:05:59.176283"
latest: "0.5.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pybarrnap"
aliases:
 - "pybarrnap"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.4.1--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pybarrnap"
config: {"url": "https://biocontainers.pro/tools/pybarrnap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pybarrnap", "latest": {"0.5.1--pyhdfd78af_0": "sha256:e89130dd359b71f5f32a5c47bae1988f2edc36422b9176c8dba7b2d97e2fc6e5"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:c655d65772907c31d613135beedf40ab27528b060054624635861124838ae464", "0.5.0--pyhdfd78af_0": "sha256:75e10395646bfca2a245712cc6f5f1d307c20061bf213ca4f6fc008eec8938e9", "0.5.1--pyhdfd78af_0": "sha256:e89130dd359b71f5f32a5c47bae1988f2edc36422b9176c8dba7b2d97e2fc6e5"}, "docker": "quay.io/biocontainers/pybarrnap", "aliases": {"pybarrnap": "/usr/local/bin/pybarrnap", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pybarrnap.
singularity registry hpc automated addition for pybarrnap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pybarrnap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pybarrnap:0.5.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pybarrnap/0.5.1--pyhdfd78af_0
$ module help quay.io/biocontainers/pybarrnap/0.5.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pybarrnap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pybarrnap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pybarrnap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pybarrnap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pybarrnap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pybarrnap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pybarrnap

```bash
$ singularity exec <container> /usr/local/bin/pybarrnap
$ podman run --it --rm --entrypoint /usr/local/bin/pybarrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybarrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
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