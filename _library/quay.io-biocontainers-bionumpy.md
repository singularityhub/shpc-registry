---
layout: container
name:  "quay.io/biocontainers/bionumpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bionumpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bionumpy/container.yaml"
updated_at: "2023-05-30 02:44:44.187175"
latest: "0.2.23--pyha8f3691_0"
container_url: "https://biocontainers.pro/tools/bionumpy"
aliases:
 - "bionumpy"
 - "f2py3.11"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "0.2.17--pyha8f3691_0"
 - "0.2.20--pyha8f3691_0"
 - "0.2.22--pyha8f3691_0"
 - "0.2.23--pyha8f3691_0"
description: "singularity registry hpc automated addition for bionumpy"
config: {"url": "https://biocontainers.pro/tools/bionumpy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bionumpy", "latest": {"0.2.23--pyha8f3691_0": "sha256:a930c285af69efdddf1ac27638f48d387f76c176b89845d9dab7a20ec13f23b3"}, "tags": {"0.2.17--pyha8f3691_0": "sha256:4888799ec9467a088c72b11f5ebd1da9043d6153f6c83c45cbc5925d1eb7f28b", "0.2.20--pyha8f3691_0": "sha256:2e71d23cc90a5aeafdc668ea857f119e36b5edc47c471fa551ac3f6bcd99c2dc", "0.2.22--pyha8f3691_0": "sha256:6a21c6bb7b4d2e4d60564770b3827ebaa6748d88ccfe2b7587e17afc2d57ce14", "0.2.23--pyha8f3691_0": "sha256:a930c285af69efdddf1ac27638f48d387f76c176b89845d9dab7a20ec13f23b3"}, "docker": "quay.io/biocontainers/bionumpy", "aliases": {"bionumpy": "/usr/local/bin/bionumpy", "f2py3.11": "/usr/local/bin/f2py3.11", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bionumpy.
singularity registry hpc automated addition for bionumpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bionumpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bionumpy:0.2.23--pyha8f3691_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bionumpy/0.2.23--pyha8f3691_0
$ module help quay.io/biocontainers/bionumpy/0.2.23--pyha8f3691_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bionumpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bionumpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bionumpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bionumpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bionumpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bionumpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bionumpy

```bash
$ singularity exec <container> /usr/local/bin/bionumpy
$ podman run --it --rm --entrypoint /usr/local/bin/bionumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bionumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
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