---
layout: container
name:  "quay.io/biocontainers/rapidnj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapidnj/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapidnj/container.yaml"
updated_at: "2024-04-13 02:37:19.771720"
latest: "2.3.2--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/rapidnj"
aliases:
 - "rapidnj"
versions:
 - "v2.3.2--hc9558a2_2"
 - "2.3.2--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for rapidnj"
config: {"url": "https://biocontainers.pro/tools/rapidnj", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapidnj", "latest": {"2.3.2--h4ac6f70_4": "sha256:34592a643def95ddda29de76ad78380f3b298d7112a29556bff652d67dbd24a6"}, "tags": {"v2.3.2--hc9558a2_2": "sha256:954cf73252442f5e037d53f07b8e74b96bbd1636db1baa44b6d18d4006e8a63a", "2.3.2--h4ac6f70_4": "sha256:34592a643def95ddda29de76ad78380f3b298d7112a29556bff652d67dbd24a6"}, "docker": "quay.io/biocontainers/rapidnj", "aliases": {"rapidnj": "/usr/local/bin/rapidnj"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapidnj.
shpc-registry automated BioContainers addition for rapidnj
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapidnj
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapidnj:2.3.2--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapidnj/2.3.2--h4ac6f70_4
$ module help quay.io/biocontainers/rapidnj/2.3.2--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapidnj-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapidnj-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapidnj-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapidnj-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapidnj-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapidnj-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rapidnj

```bash
$ singularity exec <container> /usr/local/bin/rapidnj
$ podman run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidnj   -v ${PWD} -w ${PWD} <container> -c " $@"
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