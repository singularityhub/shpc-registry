---
layout: container
name:  "quay.io/biocontainers/yame"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yame/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yame/container.yaml"
updated_at: "2026-09-20 07:35:27.734945"
latest: "1.41--he9f63f3_0"
container_url: "https://biocontainers.pro/tools/yame"
aliases:
 - "yame"
versions:
 - "1.0.5--h96c455f_0"
 - "1.8--ha83d96e_0"
 - "1.41--he9f63f3_0"
 - "1.40--he9f63f3_0"
 - "1.37--he9f63f3_0"
 - "1.36--he9f63f3_0"
 - "1.35--he9f63f3_0"
description: "singularity registry hpc automated addition for yame"
config: {"url": "https://biocontainers.pro/tools/yame", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for yame", "latest": {"1.41--he9f63f3_0": "sha256:4c93d60bf95e916b6167011c8255f06791892383802725fec554a7dac91f0eb7"}, "tags": {"1.0.5--h96c455f_0": "sha256:ec031252221a2a8b223010270a3373bbca239c6b904c20bb05030a81806c41f4", "1.8--ha83d96e_0": "sha256:b946ce3c62f7d08431f6df78dfaae8d4774dff7c101e41d11984e3d1cf7ada73", "1.41--he9f63f3_0": "sha256:4c93d60bf95e916b6167011c8255f06791892383802725fec554a7dac91f0eb7", "1.40--he9f63f3_0": "sha256:f7e23f84f6c59dcdd19be23c3126189c1da4f5d18c736079fa18628914922e06", "1.37--he9f63f3_0": "sha256:24ff5ceaa9ac39fb5b6dfcc8b9f928b8f18f1232545688fc2b3863a7ecd7f493", "1.36--he9f63f3_0": "sha256:ea0c2b57d82bc2a36a8295264c2981ed7754ffead3a9f5a71735073c69cfb15a", "1.35--he9f63f3_0": "sha256:14348376b8bec9d4fb02a28b513ea969b2ea177e6be188ce34a491b293b10227"}, "docker": "quay.io/biocontainers/yame", "aliases": {"yame": "/usr/local/bin/yame"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yame.
singularity registry hpc automated addition for yame
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yame
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yame:1.41--he9f63f3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yame/1.41--he9f63f3_0
$ module help quay.io/biocontainers/yame/1.41--he9f63f3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yame-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yame-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yame-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yame-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yame-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yame-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### yame

```bash
$ singularity exec <container> /usr/local/bin/yame
$ podman run --it --rm --entrypoint /usr/local/bin/yame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yame   -v ${PWD} -w ${PWD} <container> -c " $@"
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