---
layout: container
name:  "quay.io/biocontainers/scelestial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scelestial/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scelestial/container.yaml"
updated_at: "2026-01-16 04:14:19.468663"
latest: "1.2--h9948957_4"
container_url: "https://biocontainers.pro/tools/scelestial"
aliases:
 - "scelestial"
 - "scelestial-synthesis"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "1.2--ha038e3a_0"
 - "1.2--ha038e3a_1"
 - "1.2--h2374e42_2"
 - "1.2--h9948957_4"
description: "singularity registry hpc automated addition for scelestial"
config: {"url": "https://biocontainers.pro/tools/scelestial", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for scelestial", "latest": {"1.2--h9948957_4": "sha256:7657ebf9ee2954bd8e5fd06b78d127dc480325cba45f76778cd4c9fda500a65c"}, "tags": {"1.2--ha038e3a_0": "sha256:7511424a988ccc7a257b2dafb32ecbca7d0a4a54da768777334626b51f0ec063", "1.2--ha038e3a_1": "sha256:ed4f52989db7c932805a66c30774f579562a921a53747b5688eeabf8a824d31c", "1.2--h2374e42_2": "sha256:befcef4bde2afa24b7a2a481806712b401510506a22fecec0947a4ea5640417e", "1.2--h9948957_4": "sha256:7657ebf9ee2954bd8e5fd06b78d127dc480325cba45f76778cd4c9fda500a65c"}, "docker": "quay.io/biocontainers/scelestial", "aliases": {"scelestial": "/usr/local/bin/scelestial", "scelestial-synthesis": "/usr/local/bin/scelestial-synthesis", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scelestial.
singularity registry hpc automated addition for scelestial
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scelestial
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scelestial:1.2--h9948957_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scelestial/1.2--h9948957_4
$ module help quay.io/biocontainers/scelestial/1.2--h9948957_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scelestial-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scelestial-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scelestial-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scelestial-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scelestial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scelestial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scelestial

```bash
$ singularity exec <container> /usr/local/bin/scelestial
$ podman run --it --rm --entrypoint /usr/local/bin/scelestial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scelestial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scelestial-synthesis

```bash
$ singularity exec <container> /usr/local/bin/scelestial-synthesis
$ podman run --it --rm --entrypoint /usr/local/bin/scelestial-synthesis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scelestial-synthesis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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