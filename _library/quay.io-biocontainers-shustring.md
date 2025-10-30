---
layout: container
name:  "quay.io/biocontainers/shustring"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shustring/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shustring/container.yaml"
updated_at: "2025-10-30 03:41:18.197356"
latest: "2.6--h7b50bb2_8"
container_url: "https://biocontainers.pro/tools/shustring"
aliases:
 - "shustring"
versions:
 - "2.6--hec16e2b_5"
 - "2.6--hec16e2b_6"
 - "2.6--h031d066_7"
 - "2.6--h7b50bb2_8"
description: "shpc-registry automated BioContainers addition for shustring"
config: {"url": "https://biocontainers.pro/tools/shustring", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shustring", "latest": {"2.6--h7b50bb2_8": "sha256:91ca8a696e100e7c2efc498f6137afb7194a22c35a235444981a94bda4be2cae"}, "tags": {"2.6--hec16e2b_5": "sha256:e7ac14742b0c999542c858d465f40174b88de495888160ba9181e5feae92503a", "2.6--hec16e2b_6": "sha256:65c8036455f97c684fd7c8d6414f5c204340b1ff1ee471ef386cd3b19cd7c210", "2.6--h031d066_7": "sha256:691800dbb1d7d3f5f24f6798cc0518725ba847a268719ce0373912ea70e82ed3", "2.6--h7b50bb2_8": "sha256:91ca8a696e100e7c2efc498f6137afb7194a22c35a235444981a94bda4be2cae"}, "docker": "quay.io/biocontainers/shustring", "aliases": {"shustring": "/usr/local/bin/shustring"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shustring.
shpc-registry automated BioContainers addition for shustring
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shustring
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shustring:2.6--h7b50bb2_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shustring/2.6--h7b50bb2_8
$ module help quay.io/biocontainers/shustring/2.6--h7b50bb2_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shustring-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shustring-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shustring-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shustring-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shustring-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shustring-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shustring

```bash
$ singularity exec <container> /usr/local/bin/shustring
$ podman run --it --rm --entrypoint /usr/local/bin/shustring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shustring   -v ${PWD} -w ${PWD} <container> -c " $@"
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