---
layout: container
name:  "quay.io/biocontainers/sr2silo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sr2silo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sr2silo/container.yaml"
updated_at: "2025-04-13 04:17:59.173487"
latest: "0.0.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sr2silo"
aliases:
 - "jdiff"
 - "moto_proxy"
 - "moto_server"
 - "openapi-spec-validator"
 - "sr2silo"
 - "typer"
 - "flask"
 - "markdown-it"
 - "jp.py"
 - "numpy-config"
 - "jsonschema"
 - "pygmentize"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "tqdm"
 - "normalizer"
versions:
 - "0.0.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sr2silo"
config: {"url": "https://biocontainers.pro/tools/sr2silo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sr2silo", "latest": {"0.0.4--pyhdfd78af_0": "sha256:7fc220fe537894206e614a1d40223ca962249d41978dea86d07a15b17fb6e77b"}, "tags": {"0.0.4--pyhdfd78af_0": "sha256:7fc220fe537894206e614a1d40223ca962249d41978dea86d07a15b17fb6e77b"}, "docker": "quay.io/biocontainers/sr2silo", "aliases": {"jdiff": "/usr/local/bin/jdiff", "moto_proxy": "/usr/local/bin/moto_proxy", "moto_server": "/usr/local/bin/moto_server", "openapi-spec-validator": "/usr/local/bin/openapi-spec-validator", "sr2silo": "/usr/local/bin/sr2silo", "typer": "/usr/local/bin/typer", "flask": "/usr/local/bin/flask", "markdown-it": "/usr/local/bin/markdown-it", "jp.py": "/usr/local/bin/jp.py", "numpy-config": "/usr/local/bin/numpy-config", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sr2silo.
singularity registry hpc automated addition for sr2silo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sr2silo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sr2silo:0.0.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sr2silo/0.0.4--pyhdfd78af_0
$ module help quay.io/biocontainers/sr2silo/0.0.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sr2silo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sr2silo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sr2silo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sr2silo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sr2silo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sr2silo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jdiff

```bash
$ singularity exec <container> /usr/local/bin/jdiff
$ podman run --it --rm --entrypoint /usr/local/bin/jdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moto_proxy

```bash
$ singularity exec <container> /usr/local/bin/moto_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/moto_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moto_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moto_server

```bash
$ singularity exec <container> /usr/local/bin/moto_server
$ podman run --it --rm --entrypoint /usr/local/bin/moto_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moto_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openapi-spec-validator

```bash
$ singularity exec <container> /usr/local/bin/openapi-spec-validator
$ podman run --it --rm --entrypoint /usr/local/bin/openapi-spec-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openapi-spec-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sr2silo

```bash
$ singularity exec <container> /usr/local/bin/sr2silo
$ podman run --it --rm --entrypoint /usr/local/bin/sr2silo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sr2silo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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