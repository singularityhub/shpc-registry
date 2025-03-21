---
layout: container
name:  "quay.io/biocontainers/graphaligner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphaligner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphaligner/container.yaml"
updated_at: "2025-03-21 03:45:14.386627"
latest: "1.0.20--h06902ac_0"
container_url: "https://biocontainers.pro/tools/graphaligner"
aliases:
 - "GraphAligner"
versions:
 - "1.0.9--he1c1bb9_1"
 - "1.0.16--hd03093a_1"
 - "1.0.17--hd03093a_0"
 - "1.0.17b--hdcf5f25_1"
 - "1.0.17b--h21ec9f0_2"
 - "1.0.18--h21ec9f0_0"
 - "1.0.19--h21ec9f0_0"
 - "1.0.19--hdcf5f25_1"
 - "1.0.20--h06902ac_0"
description: "shpc-registry automated BioContainers addition for graphaligner"
config: {"url": "https://biocontainers.pro/tools/graphaligner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphaligner", "latest": {"1.0.20--h06902ac_0": "sha256:79c319cfe1ef1025e5f31ec836ddf3faf94fef407fcdafb7df7695ea97042448"}, "tags": {"1.0.9--he1c1bb9_1": "sha256:4677d55eed9562f4dc13596ead51774a6eccf5b8ff877f562983f3daa86495ed", "1.0.16--hd03093a_1": "sha256:185a85aa0d8b1d30f92497336150734698a41d65c99ae74718b45f3764d24127", "1.0.17--hd03093a_0": "sha256:77abcaef757755bb848fcf1a0ca6dc6bd57e725375dcbb1fe3b85215ecef05fb", "1.0.17b--hdcf5f25_1": "sha256:a0a461d3a8b9c0a25838391b67b3f8d4d426b8013562c75ce27ab8af97c5b26a", "1.0.17b--h21ec9f0_2": "sha256:88b5d3047d6e7e9c0acbacc8786b99f70cd85b27722f4dfda3d7a5ddf70fd66a", "1.0.18--h21ec9f0_0": "sha256:d4be77b944ed1a0d549c2936b25c0010f6228bc00d833712979d3bd0eedfa235", "1.0.19--h21ec9f0_0": "sha256:dad4a6a62e3c103b22fa3da39f21101afff8f9ea093e06fa2e366f827bf33673", "1.0.19--hdcf5f25_1": "sha256:2a537e6ac2cf7e75eb6c9a766651c4c1c3fd85f52977e0b503369e9a9243aea2", "1.0.20--h06902ac_0": "sha256:79c319cfe1ef1025e5f31ec836ddf3faf94fef407fcdafb7df7695ea97042448"}, "docker": "quay.io/biocontainers/graphaligner", "aliases": {"GraphAligner": "/usr/local/bin/GraphAligner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphaligner.
shpc-registry automated BioContainers addition for graphaligner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphaligner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphaligner:1.0.20--h06902ac_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphaligner/1.0.20--h06902ac_0
$ module help quay.io/biocontainers/graphaligner/1.0.20--h06902ac_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphaligner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphaligner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphaligner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphaligner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphaligner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphaligner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphAligner

```bash
$ singularity exec <container> /usr/local/bin/GraphAligner
$ podman run --it --rm --entrypoint /usr/local/bin/GraphAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphAligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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