---
layout: container
name:  "quay.io/biocontainers/autobigs-engine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/autobigs-engine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/autobigs-engine/container.yaml"
updated_at: "2026-01-02 04:32:27.515644"
latest: "0.14.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/autobigs-engine"
aliases:
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
versions:
 - "0.8.0--pyhdfd78af_0"
 - "0.13.0--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.14.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for autobigs-engine"
config: {"url": "https://biocontainers.pro/tools/autobigs-engine", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for autobigs-engine", "latest": {"0.14.2--pyhdfd78af_0": "sha256:ca8cee5fbd60b4e63f1721ca69f0b386236c9f25bbec0da211f5c424a09a7743"}, "tags": {"0.8.0--pyhdfd78af_0": "sha256:7a460891855f43a4fc410c0a9de33b0eab75cf0f9c68e7ad35a8e86f4ab13529", "0.13.0--pyhdfd78af_0": "sha256:2dfcb08dad5b433ad851ed27a8f84a8b1c8e92a26a073a25bca4192f978dfdec", "0.12.0--pyhdfd78af_0": "sha256:6dacc4091932be9c76f3321528e51ad2c9f1ff474cdf07cf51d70047b735196f", "0.11.0--pyhdfd78af_0": "sha256:9d0b0348a35e8ecd4f382b8a53caa47cf9c8874ae3482ca1ca3858dc1290fb6f", "0.14.2--pyhdfd78af_0": "sha256:ca8cee5fbd60b4e63f1721ca69f0b386236c9f25bbec0da211f5c424a09a7743"}, "docker": "quay.io/biocontainers/autobigs-engine", "aliases": {"idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/autobigs-engine.
singularity registry hpc automated addition for autobigs-engine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/autobigs-engine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/autobigs-engine:0.14.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/autobigs-engine/0.14.2--pyhdfd78af_0
$ module help quay.io/biocontainers/autobigs-engine/0.14.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autobigs-engine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autobigs-engine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autobigs-engine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autobigs-engine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autobigs-engine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autobigs-engine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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