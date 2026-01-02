---
layout: container
name:  "quay.io/biocontainers/needletail"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/needletail/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/needletail/container.yaml"
updated_at: "2026-01-02 04:13:52.363505"
latest: "0.7.1--py311hb6b3792_0"
container_url: "https://biocontainers.pro/tools/needletail"
aliases:
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.6.1--py310hc7d9715_0"
 - "0.6.1--py39hfa26904_0"
 - "0.6.2--py311hb6b3792_0"
 - "0.6.3--py39hfa26904_0"
 - "0.7.0--py39hfa26904_0"
 - "0.7.1--py311hb6b3792_0"
description: "singularity registry hpc automated addition for needletail"
config: {"url": "https://biocontainers.pro/tools/needletail", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for needletail", "latest": {"0.7.1--py311hb6b3792_0": "sha256:965a0e0cdea4732ce855dc6e94efd6320a4bda69d26911023ec0859bd2225c19"}, "tags": {"0.6.1--py310hc7d9715_0": "sha256:55a341b1a7ef16606832f4aa3b2aedc2f49f7e67dc1f220410c6eccc92f917fc", "0.6.1--py39hfa26904_0": "sha256:85ee4348754bdb341218b00169e70cd460a3d9fc7347a0733b19d46a8244c539", "0.6.2--py311hb6b3792_0": "sha256:599a6e1f563e11abf3499d4d8eb2509b2cf60a5c131329571f3a90967f380b04", "0.6.3--py39hfa26904_0": "sha256:4916a16ad9879b692d012874d2a0d13b1c738bb751a0c6c1a8361028d1f98a16", "0.7.0--py39hfa26904_0": "sha256:3eda0a7cc17ff17a6eaf26dd6e76b3b3289258b5dacb355f74a24018a40eab25", "0.7.1--py311hb6b3792_0": "sha256:965a0e0cdea4732ce855dc6e94efd6320a4bda69d26911023ec0859bd2225c19"}, "docker": "quay.io/biocontainers/needletail", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/needletail.
singularity registry hpc automated addition for needletail
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/needletail
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/needletail:0.7.1--py311hb6b3792_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/needletail/0.7.1--py311hb6b3792_0
$ module help quay.io/biocontainers/needletail/0.7.1--py311hb6b3792_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### needletail-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### needletail-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### needletail-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### needletail-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### needletail-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### needletail-inspect-deffile:

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