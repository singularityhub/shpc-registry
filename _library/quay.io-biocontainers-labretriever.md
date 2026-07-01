---
layout: container
name:  "quay.io/biocontainers/labretriever"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/labretriever/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/labretriever/container.yaml"
updated_at: "2026-07-01 06:47:38.434676"
latest: "1.1.3--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/labretriever"
aliases:
 - "labretriever-mcp"
 - "labretriever-mcp-repo"
 - "mcp"
 - "uvicorn"
 - "hf"
 - "tiny-agents"
 - "huggingface-cli"
 - "idna"
 - "dotenv"
 - "httpx"
 - "typer"
 - "markdown-it"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "jsonschema"
 - "pygmentize"
 - "numpy-config"
 - "tqdm"
 - "normalizer"
versions:
 - "1.1.3--pyh106432d_0"
description: "singularity registry hpc automated addition for labretriever"
config: {"url": "https://biocontainers.pro/tools/labretriever", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for labretriever", "latest": {"1.1.3--pyh106432d_0": "sha256:d27e7e241d948c6df64878bf2cba1b397876e7ccfc2d71acdf5d9ad06438e05f"}, "tags": {"1.1.3--pyh106432d_0": "sha256:d27e7e241d948c6df64878bf2cba1b397876e7ccfc2d71acdf5d9ad06438e05f"}, "docker": "quay.io/biocontainers/labretriever", "aliases": {"labretriever-mcp": "/usr/local/bin/labretriever-mcp", "labretriever-mcp-repo": "/usr/local/bin/labretriever-mcp-repo", "mcp": "/usr/local/bin/mcp", "uvicorn": "/usr/local/bin/uvicorn", "hf": "/usr/local/bin/hf", "tiny-agents": "/usr/local/bin/tiny-agents", "huggingface-cli": "/usr/local/bin/huggingface-cli", "idna": "/usr/local/bin/idna", "dotenv": "/usr/local/bin/dotenv", "httpx": "/usr/local/bin/httpx", "typer": "/usr/local/bin/typer", "markdown-it": "/usr/local/bin/markdown-it", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "numpy-config": "/usr/local/bin/numpy-config", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/labretriever.
singularity registry hpc automated addition for labretriever
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/labretriever
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/labretriever:1.1.3--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/labretriever/1.1.3--pyh106432d_0
$ module help quay.io/biocontainers/labretriever/1.1.3--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### labretriever-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### labretriever-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### labretriever-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### labretriever-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### labretriever-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### labretriever-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### labretriever-mcp

```bash
$ singularity exec <container> /usr/local/bin/labretriever-mcp
$ podman run --it --rm --entrypoint /usr/local/bin/labretriever-mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/labretriever-mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### labretriever-mcp-repo

```bash
$ singularity exec <container> /usr/local/bin/labretriever-mcp-repo
$ podman run --it --rm --entrypoint /usr/local/bin/labretriever-mcp-repo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/labretriever-mcp-repo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcp

```bash
$ singularity exec <container> /usr/local/bin/mcp
$ podman run --it --rm --entrypoint /usr/local/bin/mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uvicorn

```bash
$ singularity exec <container> /usr/local/bin/uvicorn
$ podman run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uvicorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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