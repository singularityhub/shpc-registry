---
layout: container
name:  "quay.io/biocontainers/rerconverge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rerconverge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rerconverge/container.yaml"
updated_at: "2025-10-10 03:51:05.367791"
latest: "0.3.0--r44h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/rerconverge"
aliases:
 - "f2py3.11"
 - "git2_cli"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "glpsol"
 - "pandoc"
 - "python3.1"
versions:
 - "0.3.0--r42hec16e2b_0"
 - "0.3.0--r42h031d066_1"
 - "0.3.0--r43h031d066_2"
 - "0.3.0--r44h7b50bb2_3"
description: "singularity registry hpc automated addition for rerconverge"
config: {"url": "https://biocontainers.pro/tools/rerconverge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rerconverge", "latest": {"0.3.0--r44h7b50bb2_3": "sha256:00bd63827e9cc7d4e1dd63b654f98ad851bb9132cb63f1fe4b4e821c077ead73"}, "tags": {"0.3.0--r42hec16e2b_0": "sha256:b06238ea9029dd228d01dbe9c535afc8c674d72893b8681ec3af4494f641c790", "0.3.0--r42h031d066_1": "sha256:0920e1694afbe2297e7895ba27c77e3d658ebefb5de2440f4b3304d4cd299fb5", "0.3.0--r43h031d066_2": "sha256:0f372c8253fc1474f5b8bfe76df8d7ff43f067ef749d587faf9bc77d31db7aea", "0.3.0--r44h7b50bb2_3": "sha256:00bd63827e9cc7d4e1dd63b654f98ad851bb9132cb63f1fe4b4e821c077ead73"}, "docker": "quay.io/biocontainers/rerconverge", "aliases": {"f2py3.11": "/usr/local/bin/f2py3.11", "git2_cli": "/usr/local/bin/git2_cli", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rerconverge.
singularity registry hpc automated addition for rerconverge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rerconverge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rerconverge:0.3.0--r44h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rerconverge/0.3.0--r44h7b50bb2_3
$ module help quay.io/biocontainers/rerconverge/0.3.0--r44h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rerconverge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rerconverge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rerconverge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rerconverge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rerconverge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rerconverge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2_cli

```bash
$ singularity exec <container> /usr/local/bin/git2_cli
$ podman run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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