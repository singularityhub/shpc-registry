---
layout: container
name:  "quay.io/biocontainers/wfa2-lib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wfa2-lib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wfa2-lib/container.yaml"
updated_at: "2025-04-17 03:50:54.588710"
latest: "2.3.5--h9948957_3"
container_url: "https://biocontainers.pro/tools/wfa2-lib"

versions:
 - "2.3.3--h4ac6f70_0"
 - "2.3.3--h4ac6f70_1"
 - "2.3.4--h4ac6f70_0"
 - "2.3.4--h4ac6f70_1"
 - "2.3.5--h4ac6f70_0"
 - "2.3.5--h4ac6f70_1"
 - "2.3.5--h4ac6f70_2"
 - "2.3.5--h9948957_3"
description: "singularity registry hpc automated addition for wfa2-lib"
config: {"url": "https://biocontainers.pro/tools/wfa2-lib", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for wfa2-lib", "latest": {"2.3.5--h9948957_3": "sha256:92cdc4640703b304c7413cc895637c4805e0615bddb2ab27a28a220eb7f5ea95"}, "tags": {"2.3.3--h4ac6f70_0": "sha256:62df605f9d9cac3fa9a3a4283692f74a818bb992da3c8d1218c8f7ea5204545d", "2.3.3--h4ac6f70_1": "sha256:263f84c297911d5a74da0ccd8d07cd3f2afe95bcd3c6e93c0ebdf422ef95939e", "2.3.4--h4ac6f70_0": "sha256:582f548d1d513596a094db779394f0b4338888d6e21e893f619771afcbb5340e", "2.3.4--h4ac6f70_1": "sha256:5d0d1292c4c354393667788b7c9ebf1475dc4edb658e47d9b1362430473592a1", "2.3.5--h4ac6f70_0": "sha256:b3b93c4ebb019ac78f1c464677456188c618266e37fb6d36ac735a4f0b897792", "2.3.5--h4ac6f70_1": "sha256:a4b13cd383b882ef50ab80363c2c01baa58c5529e069a37d40aca6e03c76e3bb", "2.3.5--h4ac6f70_2": "sha256:8445636f3de75b6838885b03ac9965dad8195bdfb6f7ea96b1473e5e1376cae8", "2.3.5--h9948957_3": "sha256:92cdc4640703b304c7413cc895637c4805e0615bddb2ab27a28a220eb7f5ea95"}, "docker": "quay.io/biocontainers/wfa2-lib"}
---

This module is a singularity container wrapper for quay.io/biocontainers/wfa2-lib.
singularity registry hpc automated addition for wfa2-lib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wfa2-lib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wfa2-lib:2.3.5--h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wfa2-lib/2.3.5--h9948957_3
$ module help quay.io/biocontainers/wfa2-lib/2.3.5--h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wfa2-lib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wfa2-lib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wfa2-lib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wfa2-lib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wfa2-lib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wfa2-lib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### wfa2-lib

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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