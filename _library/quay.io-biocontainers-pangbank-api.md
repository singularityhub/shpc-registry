---
layout: container
name:  "quay.io/biocontainers/pangbank-api"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pangbank-api/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pangbank-api/container.yaml"
updated_at: "2025-12-20 03:42:41.020997"
latest: "0.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pangbank-api"
aliases:
 - "email_validator"
 - "fastapi"
 - "pangbank_db"
 - "uvicorn"
 - "watchfiles"
 - "websockets"
 - "dotenv"
 - "typer"
 - "httpx"
 - "markdown-it"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "pygmentize"
versions:
 - "0.1.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pangbank-api"
config: {"url": "https://biocontainers.pro/tools/pangbank-api", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pangbank-api", "latest": {"0.1.2--pyhdfd78af_0": "sha256:f55ba8e5e551ad24359f5329e9dee5f281c0c0ac617477287f6e954683fd2c1d"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:f55ba8e5e551ad24359f5329e9dee5f281c0c0ac617477287f6e954683fd2c1d"}, "docker": "quay.io/biocontainers/pangbank-api", "aliases": {"email_validator": "/usr/local/bin/email_validator", "fastapi": "/usr/local/bin/fastapi", "pangbank_db": "/usr/local/bin/pangbank_db", "uvicorn": "/usr/local/bin/uvicorn", "watchfiles": "/usr/local/bin/watchfiles", "websockets": "/usr/local/bin/websockets", "dotenv": "/usr/local/bin/dotenv", "typer": "/usr/local/bin/typer", "httpx": "/usr/local/bin/httpx", "markdown-it": "/usr/local/bin/markdown-it", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "pygmentize": "/usr/local/bin/pygmentize"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pangbank-api.
singularity registry hpc automated addition for pangbank-api
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pangbank-api
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pangbank-api:0.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pangbank-api/0.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/pangbank-api/0.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pangbank-api-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pangbank-api-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pangbank-api-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pangbank-api-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pangbank-api-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pangbank-api-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### email_validator

```bash
$ singularity exec <container> /usr/local/bin/email_validator
$ podman run --it --rm --entrypoint /usr/local/bin/email_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/email_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastapi

```bash
$ singularity exec <container> /usr/local/bin/fastapi
$ podman run --it --rm --entrypoint /usr/local/bin/fastapi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastapi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pangbank_db

```bash
$ singularity exec <container> /usr/local/bin/pangbank_db
$ podman run --it --rm --entrypoint /usr/local/bin/pangbank_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pangbank_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvicorn

```bash
$ singularity exec <container> /usr/local/bin/uvicorn
$ podman run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchfiles

```bash
$ singularity exec <container> /usr/local/bin/watchfiles
$ podman run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### websockets

```bash
$ singularity exec <container> /usr/local/bin/websockets
$ podman run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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