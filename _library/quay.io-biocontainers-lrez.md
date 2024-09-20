---
layout: container
name:  "quay.io/biocontainers/lrez"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrez/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrez/container.yaml"
updated_at: "2024-09-20 03:05:42.558826"
latest: "2.2.4--hdcf5f25_3"
container_url: "https://biocontainers.pro/tools/lrez"
aliases:
 - "LRez"
versions:
 - "2.2.3--h7ff8a90_2"
 - "2.2.4--h7ff8a90_0"
 - "2.2.4--h21ec9f0_2"
 - "2.2.4--hdcf5f25_3"
description: "shpc-registry automated BioContainers addition for lrez"
config: {"url": "https://biocontainers.pro/tools/lrez", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lrez", "latest": {"2.2.4--hdcf5f25_3": "sha256:531b3e16ecfbf470690fc78abacee79c7a4b99c706c08191af0952fcd51af795"}, "tags": {"2.2.3--h7ff8a90_2": "sha256:64eb52f1c13a3597de8753975c7cacd3de74868c680a5fb9f790d014232c1a95", "2.2.4--h7ff8a90_0": "sha256:f7f555a4f606b1fea2270522cb7c7cd66c847ff376141e97fb3c17ced77ba9fa", "2.2.4--h21ec9f0_2": "sha256:94813d961203baa8ebd4a67e11f8cd0ded7d6a60c0f70d5cc8926b6a19472fda", "2.2.4--hdcf5f25_3": "sha256:531b3e16ecfbf470690fc78abacee79c7a4b99c706c08191af0952fcd51af795"}, "docker": "quay.io/biocontainers/lrez", "aliases": {"LRez": "/usr/local/bin/LRez"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrez.
shpc-registry automated BioContainers addition for lrez
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrez
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrez:2.2.4--hdcf5f25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrez/2.2.4--hdcf5f25_3
$ module help quay.io/biocontainers/lrez/2.2.4--hdcf5f25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrez-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrez-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrez-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrez-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrez-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrez-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LRez

```bash
$ singularity exec <container> /usr/local/bin/LRez
$ podman run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LRez   -v ${PWD} -w ${PWD} <container> -c " $@"
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