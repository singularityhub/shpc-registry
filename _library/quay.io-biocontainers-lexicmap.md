---
layout: container
name:  "quay.io/biocontainers/lexicmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lexicmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lexicmap/container.yaml"
updated_at: "2025-09-07 03:08:59.780329"
latest: "0.7.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/lexicmap"
aliases:
 - "lexicmap"
versions:
 - "0.4.0--h9ee0642_0"
 - "0.5.0--h9ee0642_0"
 - "0.7.0--h9ee0642_0"
 - "0.6.1--h9ee0642_0"
description: "singularity registry hpc automated addition for lexicmap"
config: {"url": "https://biocontainers.pro/tools/lexicmap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lexicmap", "latest": {"0.7.0--h9ee0642_0": "sha256:21f9e4f8fec423fe5f0d4f61a049bf2425abe6e129b18f15ba6bbdcdc3913fdd"}, "tags": {"0.4.0--h9ee0642_0": "sha256:346ea5daff68dc6c84d878d9cb3cbbb51f5f9a6b047ab1c3250c8052ae44ea97", "0.5.0--h9ee0642_0": "sha256:f7a0a4113745f6a88734558962caf7b61b8608c3ff2e5d85ea73da4381419e58", "0.7.0--h9ee0642_0": "sha256:21f9e4f8fec423fe5f0d4f61a049bf2425abe6e129b18f15ba6bbdcdc3913fdd", "0.6.1--h9ee0642_0": "sha256:8f316c5a9ee9ec977a5cf0a7418d1ad8ea88b0167b1bce5892e0c6de9d316a8a"}, "docker": "quay.io/biocontainers/lexicmap", "aliases": {"lexicmap": "/usr/local/bin/lexicmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lexicmap.
singularity registry hpc automated addition for lexicmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lexicmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lexicmap:0.7.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lexicmap/0.7.0--h9ee0642_0
$ module help quay.io/biocontainers/lexicmap/0.7.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lexicmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lexicmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lexicmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lexicmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lexicmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lexicmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lexicmap

```bash
$ singularity exec <container> /usr/local/bin/lexicmap
$ podman run --it --rm --entrypoint /usr/local/bin/lexicmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lexicmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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