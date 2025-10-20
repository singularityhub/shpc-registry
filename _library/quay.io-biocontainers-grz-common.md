---
layout: container
name:  "quay.io/biocontainers/grz-common"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-common/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-common/container.yaml"
updated_at: "2025-10-20 03:50:39.082501"
latest: "1.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grz-common"
aliases:
 - "crypt4gh"
 - "crypt4gh-keygen"
 - "dotenv"
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
 - "1.0.2--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "1.2.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grz-common"
config: {"url": "https://biocontainers.pro/tools/grz-common", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-common", "latest": {"1.3.0--pyhdfd78af_0": "sha256:3d19431706a527b6a4b01b52bf3b922d2ec9cf34bf1f9e8c476c027487217be7"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:743bf023463b437eafe3cedf0a4e28d21447936ea332353e0fa5f61dca6566e0", "1.0.2--pyhdfd78af_0": "sha256:95438729df0e35a75e15a2ba50e29debf1a938525483796b88eb93ab7ad32f3e", "1.2.0--pyhdfd78af_0": "sha256:e9e72210683ff19ec6c3a8a6eef20d901560656c6e23af30d9874535b9326d62", "1.1.1--pyhdfd78af_0": "sha256:acd37eb9a44452adaa9a7512855e76dee90fc089ddca01545ca9c987b25ea3a1", "1.0.3--pyhdfd78af_0": "sha256:a443d4540b15cc23a307dd07bc488cf778b98a5453f5ccd8b627eaec9c31edfd", "1.3.0--pyhdfd78af_0": "sha256:3d19431706a527b6a4b01b52bf3b922d2ec9cf34bf1f9e8c476c027487217be7", "1.2.1--pyhdfd78af_0": "sha256:f675412754d6e6edc5738fd135b3ca69202d4ce21aabfd96a8bc90204aca2ce2"}, "docker": "quay.io/biocontainers/grz-common", "aliases": {"crypt4gh": "/usr/local/bin/crypt4gh", "crypt4gh-keygen": "/usr/local/bin/crypt4gh-keygen", "dotenv": "/usr/local/bin/dotenv", "markdown-it": "/usr/local/bin/markdown-it", "jp.py": "/usr/local/bin/jp.py", "jsonschema": "/usr/local/bin/jsonschema", "pygmentize": "/usr/local/bin/pygmentize", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "tqdm": "/usr/local/bin/tqdm", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-common.
singularity registry hpc automated addition for grz-common
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-common
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-common:1.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-common/1.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/grz-common/1.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-common-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-common-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-common-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-common-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-common-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-common-inspect-deffile:

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


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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