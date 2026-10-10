---
layout: container
name:  "quay.io/biocontainers/bionym"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bionym/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bionym/container.yaml"
updated_at: "2026-10-10 19:13:38.910551"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bionym"
aliases:
 - "bionym"
 - "dotenv"
 - "httpx"
 - "idna"
 - "typer"
 - "markdown-it"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "pygmentize"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for bionym"
config: {"url": "https://biocontainers.pro/tools/bionym", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bionym", "latest": {"0.1.0--pyhdfd78af_0": "sha256:54bddfca4747d8faf74d5d8c9bb0d90d25300b08c50eda62e97dea27a3bc387d"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:54bddfca4747d8faf74d5d8c9bb0d90d25300b08c50eda62e97dea27a3bc387d"}, "docker": "quay.io/biocontainers/bionym", "aliases": {"bionym": "/usr/local/bin/bionym", "dotenv": "/usr/local/bin/dotenv", "httpx": "/usr/local/bin/httpx", "idna": "/usr/local/bin/idna", "typer": "/usr/local/bin/typer", "markdown-it": "/usr/local/bin/markdown-it", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bionym.
singularity registry hpc automated addition for bionym
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bionym
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bionym:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bionym/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/bionym/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bionym-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bionym-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bionym-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bionym-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bionym-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bionym-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bionym

```bash
$ singularity exec <container> /usr/local/bin/bionym
$ podman run --it --rm --entrypoint /usr/local/bin/bionym   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bionym   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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