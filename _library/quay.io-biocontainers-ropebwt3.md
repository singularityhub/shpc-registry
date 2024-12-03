---
layout: container
name:  "quay.io/biocontainers/ropebwt3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ropebwt3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ropebwt3/container.yaml"
updated_at: "2024-12-03 03:10:40.146670"
latest: "3.8--he4a0461_0"
container_url: "https://biocontainers.pro/tools/ropebwt3"
aliases:
 - "ropebwt3"
versions:
 - "3.3--he4a0461_0"
 - "3.4--he4a0461_0"
 - "3.7--he4a0461_0"
 - "3.6--he4a0461_0"
 - "3.5--he4a0461_0"
 - "3.8--he4a0461_0"
description: "singularity registry hpc automated addition for ropebwt3"
config: {"url": "https://biocontainers.pro/tools/ropebwt3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ropebwt3", "latest": {"3.8--he4a0461_0": "sha256:2afd17e53c3386c1c44992b562673873bb468e1ebad252bec4edf21d4cbbed4f"}, "tags": {"3.3--he4a0461_0": "sha256:7ba285cd082f69e33c6d43d5a7e6d369a328780dd4e3c7f36ae4c3c075f27746", "3.4--he4a0461_0": "sha256:1e9568f4f8be49dd25e025a07b8f9d34d1487bdbc78149f6c635ed2a3a4c890f", "3.7--he4a0461_0": "sha256:1d06ac02cf1d7d5057577289f5e9c287c988a08b9e8a146be6e227241ee31226", "3.6--he4a0461_0": "sha256:6b67309e6a1739400dc72b612ad7a514f87e1fcb840881ec8dd5868f989c7632", "3.5--he4a0461_0": "sha256:c4ac6e5f23e0db0733334c6a51b10035e867dc047a6c4e3663ed1704053a2279", "3.8--he4a0461_0": "sha256:2afd17e53c3386c1c44992b562673873bb468e1ebad252bec4edf21d4cbbed4f"}, "docker": "quay.io/biocontainers/ropebwt3", "aliases": {"ropebwt3": "/usr/local/bin/ropebwt3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ropebwt3.
singularity registry hpc automated addition for ropebwt3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ropebwt3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ropebwt3:3.8--he4a0461_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ropebwt3/3.8--he4a0461_0
$ module help quay.io/biocontainers/ropebwt3/3.8--he4a0461_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ropebwt3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ropebwt3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ropebwt3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ropebwt3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ropebwt3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ropebwt3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ropebwt3

```bash
$ singularity exec <container> /usr/local/bin/ropebwt3
$ podman run --it --rm --entrypoint /usr/local/bin/ropebwt3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ropebwt3   -v ${PWD} -w ${PWD} <container> -c " $@"
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