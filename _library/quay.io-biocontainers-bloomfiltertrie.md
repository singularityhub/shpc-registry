---
layout: container
name:  "quay.io/biocontainers/bloomfiltertrie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bloomfiltertrie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bloomfiltertrie/container.yaml"
updated_at: "2025-09-23 05:17:22.772136"
latest: "0.8.7--h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/bloomfiltertrie"
aliases:
 - "bft"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
versions:
 - "0.8.7--hec16e2b_3"
 - "0.8.7--hec16e2b_4"
 - "0.8.7--h031d066_5"
 - "0.8.7--h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for bloomfiltertrie"
config: {"url": "https://biocontainers.pro/tools/bloomfiltertrie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bloomfiltertrie", "latest": {"0.8.7--h7b50bb2_6": "sha256:3a8fd69c849e4454eabfe492eb859dd66ff990584b19daa3a041bc0a5f87efa8"}, "tags": {"0.8.7--hec16e2b_3": "sha256:08adec15bffd0c4dda0082d8f33425cf27edf2e044c74eb3a091957daad33103", "0.8.7--hec16e2b_4": "sha256:0d96bdd5c749659bdfeb3d936a408967bb8104f54c5af062a2425ec159608da5", "0.8.7--h031d066_5": "sha256:a31bf024e7ae40fdbf55f0072ece3a9b08ad2423ebf891ca3b215b94ffaf9ab7", "0.8.7--h7b50bb2_6": "sha256:3a8fd69c849e4454eabfe492eb859dd66ff990584b19daa3a041bc0a5f87efa8"}, "docker": "quay.io/biocontainers/bloomfiltertrie", "aliases": {"bft": "/usr/local/bin/bft", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bloomfiltertrie.
shpc-registry automated BioContainers addition for bloomfiltertrie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bloomfiltertrie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bloomfiltertrie:0.8.7--h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bloomfiltertrie/0.8.7--h7b50bb2_6
$ module help quay.io/biocontainers/bloomfiltertrie/0.8.7--h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bloomfiltertrie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bloomfiltertrie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bloomfiltertrie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bloomfiltertrie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bloomfiltertrie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bloomfiltertrie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bft

```bash
$ singularity exec <container> /usr/local/bin/bft
$ podman run --it --rm --entrypoint /usr/local/bin/bft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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