---
layout: container
name:  "quay.io/biocontainers/graphmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/graphmap/container.yaml"
updated_at: "2023-12-09 03:06:09.249650"
latest: "0.6.3--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/graphmap"
aliases:
 - "graphmap2"
versions:
 - "0.6.3--hd03093a_2"
 - "0.6.3--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for graphmap"
config: {"url": "https://biocontainers.pro/tools/graphmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphmap", "latest": {"0.6.3--hdcf5f25_4": "sha256:41b45104db696870699dc91ab22630a5337bf63f202af2ae646f98621f0c5729"}, "tags": {"0.6.3--hd03093a_2": "sha256:bd4913f93a27e40bb2fca04497eb34518f68363d5e3863bce8674630dd179f0f", "0.6.3--hdcf5f25_4": "sha256:41b45104db696870699dc91ab22630a5337bf63f202af2ae646f98621f0c5729"}, "docker": "quay.io/biocontainers/graphmap", "aliases": {"graphmap2": "/usr/local/bin/graphmap2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphmap.
shpc-registry automated BioContainers addition for graphmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphmap:0.6.3--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphmap/0.6.3--hdcf5f25_4
$ module help quay.io/biocontainers/graphmap/0.6.3--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### graphmap2

```bash
$ singularity exec <container> /usr/local/bin/graphmap2
$ podman run --it --rm --entrypoint /usr/local/bin/graphmap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphmap2   -v ${PWD} -w ${PWD} <container> -c " $@"
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