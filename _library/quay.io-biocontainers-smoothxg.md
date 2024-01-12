---
layout: container
name:  "quay.io/biocontainers/smoothxg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smoothxg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smoothxg/container.yaml"
updated_at: "2024-01-12 03:12:16.816257"
latest: "0.7.2--h40c17d1_0"
container_url: "https://biocontainers.pro/tools/smoothxg"
aliases:
 - "smoothxg"
versions:
 - "0.6.5--hfb1f815_2"
 - "0.6.7--hfb1f815_1"
 - "0.6.8--hfb1f815_0"
 - "0.7.0--hfb1f815_0"
 - "0.7.0--h40c17d1_2"
 - "0.7.2--h40c17d1_0"
description: "shpc-registry automated BioContainers addition for smoothxg"
config: {"url": "https://biocontainers.pro/tools/smoothxg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for smoothxg", "latest": {"0.7.2--h40c17d1_0": "sha256:cdd3eb20d1aa2e27406d5aa41aab7bdddf2bef2af8bd8e9dcdc4d30cbebaeb0f"}, "tags": {"0.6.5--hfb1f815_2": "sha256:c4c82cbbf83b65d767c3f6af2b8a6fb5894ddb828d75d1a7f94da3224b2299ea", "0.6.7--hfb1f815_1": "sha256:0d752f242a36a696064edd84137b62fa7416645c324be5c1f30f4d69b8754189", "0.6.8--hfb1f815_0": "sha256:e1dc69f6bf1496a516a496fea187ae37c0b0dd125eacf8561f44dd71eb6348a1", "0.7.0--hfb1f815_0": "sha256:81ae8327cb62678ff597096f25141448f2ec3e3269b6e7c90e59acc94bb2ba38", "0.7.0--h40c17d1_2": "sha256:b524d46705dea8b18f700edbbc712c416b7216be9b3a05cc66a6ca5ccc412e00", "0.7.2--h40c17d1_0": "sha256:cdd3eb20d1aa2e27406d5aa41aab7bdddf2bef2af8bd8e9dcdc4d30cbebaeb0f"}, "docker": "quay.io/biocontainers/smoothxg", "aliases": {"smoothxg": "/usr/local/bin/smoothxg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smoothxg.
shpc-registry automated BioContainers addition for smoothxg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smoothxg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smoothxg:0.7.2--h40c17d1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smoothxg/0.7.2--h40c17d1_0
$ module help quay.io/biocontainers/smoothxg/0.7.2--h40c17d1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smoothxg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smoothxg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smoothxg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smoothxg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smoothxg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smoothxg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smoothxg

```bash
$ singularity exec <container> /usr/local/bin/smoothxg
$ podman run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smoothxg   -v ${PWD} -w ${PWD} <container> -c " $@"
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