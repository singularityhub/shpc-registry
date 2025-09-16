---
layout: container
name:  "quay.io/biocontainers/grz-db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-db/container.yaml"
updated_at: "2025-09-16 04:18:18.055318"
latest: "0.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grz-db"
aliases:
 - "alembic"
 - "mako-render"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.1.0--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grz-db"
config: {"url": "https://biocontainers.pro/tools/grz-db", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-db", "latest": {"0.5.0--pyhdfd78af_0": "sha256:36edc6f835cb6f6add801b769b6a20057c348b8655e99ca657d219b031b5290d"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:b0db71f5a1d852f434208c715a2526fd6b953ee04abb3e52d728e01455bcd9cf", "0.2.0--pyhdfd78af_0": "sha256:7c7daf6afd453db5e3fffbffb6e030fc20fa0abd4424104c3b065ae39fbc704f", "0.3.0--pyhdfd78af_0": "sha256:2ccc38b35969d0c5f3364c57a4219d5f93abbcd89e93cac91b92653d6cacff2d", "0.2.1--pyhdfd78af_0": "sha256:09373eacefd40538ee853be4149c2c3f57e7b3561e95e25544377f8a7f6bc03c", "0.5.0--pyhdfd78af_0": "sha256:36edc6f835cb6f6add801b769b6a20057c348b8655e99ca657d219b031b5290d", "0.4.0--pyhdfd78af_0": "sha256:cd5b6a4e09942d9532c877c6457a1a37706865510f95df03750cff2cb5ea3937"}, "docker": "quay.io/biocontainers/grz-db", "aliases": {"alembic": "/usr/local/bin/alembic", "mako-render": "/usr/local/bin/mako-render", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-db.
singularity registry hpc automated addition for grz-db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-db:0.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-db/0.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/grz-db/0.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
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