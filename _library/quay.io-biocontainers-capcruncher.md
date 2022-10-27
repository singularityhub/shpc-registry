---
layout: container
name:  "quay.io/biocontainers/capcruncher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/capcruncher/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/capcruncher/container.yaml"
updated_at: "2022-10-27 00:51:37.420032"
latest: "0.2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/capcruncher"
aliases:
 - "capcruncher"
 - "fetchChromSizes"
 - "ice"
 - "rich-click"
 - "trim_galore"
versions:
 - "0.2.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for capcruncher"
config: {"url": "https://biocontainers.pro/tools/capcruncher", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for capcruncher", "latest": {"0.2.3--pyhdfd78af_0": "sha256:8957ca955243f15d7c5dfb43be21b3ae4170b5f41c309f730b64adf9b6090da0"}, "tags": {"0.2.3--pyhdfd78af_0": "sha256:8957ca955243f15d7c5dfb43be21b3ae4170b5f41c309f730b64adf9b6090da0"}, "docker": "quay.io/biocontainers/capcruncher", "aliases": {"capcruncher": "/usr/local/bin/capcruncher", "fetchChromSizes": "/usr/local/bin/fetchChromSizes", "ice": "/usr/local/bin/ice", "rich-click": "/usr/local/bin/rich-click", "trim_galore": "/usr/local/bin/trim_galore"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/capcruncher.
shpc-registry automated BioContainers addition for capcruncher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/capcruncher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/capcruncher:0.2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/capcruncher/0.2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/capcruncher/0.2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### capcruncher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### capcruncher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### capcruncher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### capcruncher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### capcruncher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### capcruncher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### capcruncher

```bash
$ singularity exec <container> /usr/local/bin/capcruncher
$ podman run --it --rm --entrypoint /usr/local/bin/capcruncher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capcruncher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetchChromSizes

```bash
$ singularity exec <container> /usr/local/bin/fetchChromSizes
$ podman run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetchChromSizes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ice

```bash
$ singularity exec <container> /usr/local/bin/ice
$ podman run --it --rm --entrypoint /usr/local/bin/ice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
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