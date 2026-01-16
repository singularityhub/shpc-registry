---
layout: container
name:  "quay.io/biocontainers/lorma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lorma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lorma/container.yaml"
updated_at: "2026-01-16 04:03:50.826283"
latest: "0.4--2"
container_url: "https://biocontainers.pro/tools/lorma"
aliases:
 - "LoRMA"
 - "lordec-build-SR-graph"
 - "lordec-correct"
 - "lordec-stat"
 - "lordec-trim"
 - "lordec-trim-split"
 - "lorma.sh"
versions:
 - "0.4--2"
description: "shpc-registry automated BioContainers addition for lorma"
config: {"url": "https://biocontainers.pro/tools/lorma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lorma", "latest": {"0.4--2": "sha256:7adb25f7f2eca90f8d7037f7c33991e4aa6b995e844c0a91d653c40fe9318ca7"}, "tags": {"0.4--2": "sha256:7adb25f7f2eca90f8d7037f7c33991e4aa6b995e844c0a91d653c40fe9318ca7"}, "docker": "quay.io/biocontainers/lorma", "aliases": {"LoRMA": "/usr/local/bin/LoRMA", "lordec-build-SR-graph": "/usr/local/bin/lordec-build-SR-graph", "lordec-correct": "/usr/local/bin/lordec-correct", "lordec-stat": "/usr/local/bin/lordec-stat", "lordec-trim": "/usr/local/bin/lordec-trim", "lordec-trim-split": "/usr/local/bin/lordec-trim-split", "lorma.sh": "/usr/local/bin/lorma.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lorma.
shpc-registry automated BioContainers addition for lorma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lorma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lorma:0.4--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lorma/0.4--2
$ module help quay.io/biocontainers/lorma/0.4--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lorma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lorma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lorma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lorma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lorma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lorma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LoRMA

```bash
$ singularity exec <container> /usr/local/bin/LoRMA
$ podman run --it --rm --entrypoint /usr/local/bin/LoRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LoRMA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-build-SR-graph

```bash
$ singularity exec <container> /usr/local/bin/lordec-build-SR-graph
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-build-SR-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-build-SR-graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-correct

```bash
$ singularity exec <container> /usr/local/bin/lordec-correct
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-correct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-stat

```bash
$ singularity exec <container> /usr/local/bin/lordec-stat
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-trim

```bash
$ singularity exec <container> /usr/local/bin/lordec-trim
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-trim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-trim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lordec-trim-split

```bash
$ singularity exec <container> /usr/local/bin/lordec-trim-split
$ podman run --it --rm --entrypoint /usr/local/bin/lordec-trim-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordec-trim-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lorma.sh

```bash
$ singularity exec <container> /usr/local/bin/lorma.sh
$ podman run --it --rm --entrypoint /usr/local/bin/lorma.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lorma.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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