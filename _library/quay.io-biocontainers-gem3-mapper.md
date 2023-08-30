---
layout: container
name:  "quay.io/biocontainers/gem3-mapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gem3-mapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gem3-mapper/container.yaml"
updated_at: "2023-08-30 02:36:04.329684"
latest: "3.6.1--h9d449c0_12"
container_url: "https://biocontainers.pro/tools/gem3-mapper"
aliases:
 - "gem-indexer"
 - "gem-mapper"
 - "gem-retriever"
versions:
 - "3.6.1--h36cd882_9"
 - "3.6.1--h67092d7_10"
 - "3.6.1--h9d449c0_12"
description: "shpc-registry automated BioContainers addition for gem3-mapper"
config: {"url": "https://biocontainers.pro/tools/gem3-mapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gem3-mapper", "latest": {"3.6.1--h9d449c0_12": "sha256:d8fd45131ea03fe270f74288a9833122ecedd78a599eb9f0d4ef3901c3d4a7fa"}, "tags": {"3.6.1--h36cd882_9": "sha256:c99eee888ac719f16886b56cbc6db85f6755aba2129fec10eba628a467b30136", "3.6.1--h67092d7_10": "sha256:171004494f57544a86349dd1d843751af7bb2f88d22a819a945c7f4a38fea169", "3.6.1--h9d449c0_12": "sha256:d8fd45131ea03fe270f74288a9833122ecedd78a599eb9f0d4ef3901c3d4a7fa"}, "docker": "quay.io/biocontainers/gem3-mapper", "aliases": {"gem-indexer": "/usr/local/bin/gem-indexer", "gem-mapper": "/usr/local/bin/gem-mapper", "gem-retriever": "/usr/local/bin/gem-retriever"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gem3-mapper.
shpc-registry automated BioContainers addition for gem3-mapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gem3-mapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gem3-mapper:3.6.1--h9d449c0_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gem3-mapper/3.6.1--h9d449c0_12
$ module help quay.io/biocontainers/gem3-mapper/3.6.1--h9d449c0_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gem3-mapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gem3-mapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gem3-mapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gem3-mapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gem3-mapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gem3-mapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gem-indexer

```bash
$ singularity exec <container> /usr/local/bin/gem-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-mapper

```bash
$ singularity exec <container> /usr/local/bin/gem-mapper
$ podman run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem-retriever

```bash
$ singularity exec <container> /usr/local/bin/gem-retriever
$ podman run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gem-retriever   -v ${PWD} -w ${PWD} <container> -c " $@"
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