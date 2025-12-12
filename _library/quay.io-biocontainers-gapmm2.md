---
layout: container
name:  "quay.io/biocontainers/gapmm2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gapmm2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gapmm2/container.yaml"
updated_at: "2025-12-12 04:01:58.541719"
latest: "25.8.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/gapmm2"
aliases:
 - "gapmm2"
 - "minimap2.py"
 - "natsort"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "23.11.3--pyhdfd78af_0"
 - "25.4.13--pyhdfd78af_0"
 - "25.8.12--pyhdfd78af_0"
description: "singularity registry hpc automated addition for gapmm2"
config: {"url": "https://biocontainers.pro/tools/gapmm2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gapmm2", "latest": {"25.8.12--pyhdfd78af_0": "sha256:95fb0f6d632c6cb6ca213bfd79e4f7c77cf9d56e682297c4b392348506d7b228"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:a41112ff73ef13209d38658c8fc68a8bb06635f76e3b6b0a7076b1c6dce94d6c", "23.11.3--pyhdfd78af_0": "sha256:58d3894bc9a7f43959a2798c59aa046d277db031a13ec208f64cee96bd252643", "25.4.13--pyhdfd78af_0": "sha256:9f2c666045270327d9682cca1052161ed05779e6eb9bfa2caab847c1989662ce", "25.8.12--pyhdfd78af_0": "sha256:95fb0f6d632c6cb6ca213bfd79e4f7c77cf9d56e682297c4b392348506d7b228"}, "docker": "quay.io/biocontainers/gapmm2", "aliases": {"gapmm2": "/usr/local/bin/gapmm2", "minimap2.py": "/usr/local/bin/minimap2.py", "natsort": "/usr/local/bin/natsort", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gapmm2.
singularity registry hpc automated addition for gapmm2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gapmm2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gapmm2:25.8.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gapmm2/25.8.12--pyhdfd78af_0
$ module help quay.io/biocontainers/gapmm2/25.8.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gapmm2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gapmm2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gapmm2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gapmm2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gapmm2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gapmm2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gapmm2

```bash
$ singularity exec <container> /usr/local/bin/gapmm2
$ podman run --it --rm --entrypoint /usr/local/bin/gapmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gapmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2.py

```bash
$ singularity exec <container> /usr/local/bin/minimap2.py
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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