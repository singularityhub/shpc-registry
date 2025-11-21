---
layout: container
name:  "quay.io/biocontainers/grzctl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grzctl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grzctl/container.yaml"
updated_at: "2025-11-21 15:52:31.661206"
latest: "1.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grzctl"
aliases:
 - "crypt4gh"
 - "crypt4gh-keygen"
 - "grz-cli"
 - "grzctl"
 - "alembic"
 - "dotenv"
 - "mako-render"
 - "markdown-it"
 - "jp.py"
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
 - "0.1.0--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.2.6--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grzctl"
config: {"url": "https://biocontainers.pro/tools/grzctl", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grzctl", "latest": {"1.3.0--pyhdfd78af_0": "sha256:d6f22d7a5296a2c781b1662e2ebb5eab39c61c6c1bc73438a8ca88a3cd2e4692"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:a9a6307776305d81b2b511b80066ce6441297210ebf67e7c7dbe95539fa24296", "0.2.2--pyhdfd78af_0": "sha256:b7e07bbb412fa24b6f7b2cb5ad81582f9a377190248e21ac9b0a5d6d17040181", "0.3.0--pyhdfd78af_0": "sha256:5338687ef69c8e561509c939aa6f03c4b66309970f9078bdeed775f58839d84e", "0.2.6--pyhdfd78af_0": "sha256:1282f09759e7b47b8cc5bbec86c7321954d9a337da4cb9c56da945a83f3e5636", "0.5.0--pyhdfd78af_0": "sha256:a06f379914f80893425ceb0ddf8833b88daf553cdd77bf27fbba21797b03de75", "0.4.0--pyhdfd78af_0": "sha256:3b1d1ca64c3d615c4c551c17c6a77e0289d785a71024db82bbaf98b7136613b3", "0.6.0--pyhdfd78af_0": "sha256:651d67a87d25f23260d7907740d4cc3ab7d73e8e044e9810966db1f5e415f5f7", "1.3.0--pyhdfd78af_0": "sha256:d6f22d7a5296a2c781b1662e2ebb5eab39c61c6c1bc73438a8ca88a3cd2e4692", "1.2.0--pyhdfd78af_0": "sha256:4150f87fdb786b84cf429d8cdcd426f2107fe79083834f2d30ecb843145360d7", "1.0.1--pyhdfd78af_0": "sha256:81a4a4ff930c9b09b22b9e309d8efbffcf590a0b808fbd4cf25d02b555fe595e"}, "docker": "quay.io/biocontainers/grzctl", "aliases": {"crypt4gh": "/usr/local/bin/crypt4gh", "crypt4gh-keygen": "/usr/local/bin/crypt4gh-keygen", "grz-cli": "/usr/local/bin/grz-cli", "grzctl": "/usr/local/bin/grzctl", "alembic": "/usr/local/bin/alembic", "dotenv": "/usr/local/bin/dotenv", "mako-render": "/usr/local/bin/mako-render", "markdown-it": "/usr/local/bin/markdown-it", "jp.py": "/usr/local/bin/jp.py", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grzctl.
singularity registry hpc automated addition for grzctl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grzctl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grzctl:1.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grzctl/1.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/grzctl/1.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grzctl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grzctl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grzctl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grzctl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grzctl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grzctl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crypt4gh

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crypt4gh-keygen

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grz-cli

```bash
$ singularity exec <container> /usr/local/bin/grz-cli
$ podman run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grzctl

```bash
$ singularity exec <container> /usr/local/bin/grzctl
$ podman run --it --rm --entrypoint /usr/local/bin/grzctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grzctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alembic

```bash
$ singularity exec <container> /usr/local/bin/alembic
$ podman run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alembic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
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