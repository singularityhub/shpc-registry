---
layout: container
name:  "quay.io/biocontainers/3seq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/3seq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/3seq/container.yaml"
updated_at: "2023-04-03 02:59:11.220725"
latest: "1.8--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/3seq"
aliases:
 - "3seq"
versions:
 - "1.8--h9f5acd7_1"
description: "singularity registry hpc automated addition for 3seq"
config: {"url": "https://biocontainers.pro/tools/3seq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for 3seq", "latest": {"1.8--h9f5acd7_1": "sha256:471d0948d34338bb871ef005b267bd08119f1d4fde178a4a755e696f635542e7"}, "tags": {"1.8--h9f5acd7_1": "sha256:471d0948d34338bb871ef005b267bd08119f1d4fde178a4a755e696f635542e7"}, "docker": "quay.io/biocontainers/3seq", "aliases": {"3seq": "/usr/local/bin/3seq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/3seq.
singularity registry hpc automated addition for 3seq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/3seq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/3seq:1.8--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/3seq/1.8--h9f5acd7_1
$ module help quay.io/biocontainers/3seq/1.8--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### 3seq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### 3seq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### 3seq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### 3seq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### 3seq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### 3seq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 3seq

```bash
$ singularity exec <container> /usr/local/bin/3seq
$ podman run --it --rm --entrypoint /usr/local/bin/3seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/3seq   -v ${PWD} -w ${PWD} <container> -c " $@"
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