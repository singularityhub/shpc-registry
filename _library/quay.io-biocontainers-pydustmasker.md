---
layout: container
name:  "quay.io/biocontainers/pydustmasker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pydustmasker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pydustmasker/container.yaml"
updated_at: "2025-10-14 03:06:50.776226"
latest: "1.0.3--py310hc7d9715_0"
container_url: "https://biocontainers.pro/tools/pydustmasker"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "1.0.0--py310h7c593f9_0"
 - "1.0.0--py38h0020b31_1"
 - "1.0.0--py310h1fe012e_2"
 - "1.0.0--py310hc7d9715_3"
 - "1.0.2--py310hc7d9715_0"
 - "1.0.3--py310hc7d9715_0"
description: "singularity registry hpc automated addition for pydustmasker"
config: {"url": "https://biocontainers.pro/tools/pydustmasker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pydustmasker", "latest": {"1.0.3--py310hc7d9715_0": "sha256:a189a6545edccd18743e7adf1e960f5c1e679d9af1e6d4991d63a1be67dcd212"}, "tags": {"1.0.0--py310h7c593f9_0": "sha256:99dff24cc7577a7d1e88fbdbf22ef477bcc16c84f56436c90f51089fe62f19cb", "1.0.0--py38h0020b31_1": "sha256:37282d928f8b2448186ce89feeef7dfa13d2a8afc874fbd34b4a5d0888523865", "1.0.0--py310h1fe012e_2": "sha256:4a3044e99e0d1858d6d6736a23a9bccc84470dd02f787d8795460219b2c26deb", "1.0.0--py310hc7d9715_3": "sha256:c34fdde1c43b0263c50876ec1c8ab5a054dfd7edae1a2d79fd936917dbf341a0", "1.0.2--py310hc7d9715_0": "sha256:462e9245ebfe56ba41274cc8be4e10fa3aaf4d68dcab12e53046c370d15d65fd", "1.0.3--py310hc7d9715_0": "sha256:a189a6545edccd18743e7adf1e960f5c1e679d9af1e6d4991d63a1be67dcd212"}, "docker": "quay.io/biocontainers/pydustmasker", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pydustmasker.
singularity registry hpc automated addition for pydustmasker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pydustmasker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pydustmasker:1.0.3--py310hc7d9715_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pydustmasker/1.0.3--py310hc7d9715_0
$ module help quay.io/biocontainers/pydustmasker/1.0.3--py310hc7d9715_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pydustmasker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pydustmasker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pydustmasker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pydustmasker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pydustmasker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pydustmasker-inspect-deffile:

```bash
$ singularity inspect -d <container>
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