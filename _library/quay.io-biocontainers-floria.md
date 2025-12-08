---
layout: container
name:  "quay.io/biocontainers/floria"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/floria/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/floria/container.yaml"
updated_at: "2025-12-08 03:59:58.351585"
latest: "0.0.2--ha6fb395_0"
container_url: "https://biocontainers.pro/tools/floria"
aliases:
 - "floria"
 - "vartig-dump"
versions:
 - "0.0.1--h4ac6f70_0"
 - "0.0.2--ha6fb395_0"
description: "singularity registry hpc automated addition for floria"
config: {"url": "https://biocontainers.pro/tools/floria", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for floria", "latest": {"0.0.2--ha6fb395_0": "sha256:bc4cba21ad69e09f6d8ccd6776d64386559ebc06cd369b58f5d59cde3b4527c9"}, "tags": {"0.0.1--h4ac6f70_0": "sha256:345661481a964dc4faa28deaf1ed11ae9edcfa4579559351ad1db5f50c9b7980", "0.0.2--ha6fb395_0": "sha256:bc4cba21ad69e09f6d8ccd6776d64386559ebc06cd369b58f5d59cde3b4527c9"}, "docker": "quay.io/biocontainers/floria", "aliases": {"floria": "/usr/local/bin/floria", "vartig-dump": "/usr/local/bin/vartig-dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/floria.
singularity registry hpc automated addition for floria
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/floria
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/floria:0.0.2--ha6fb395_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/floria/0.0.2--ha6fb395_0
$ module help quay.io/biocontainers/floria/0.0.2--ha6fb395_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### floria-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### floria-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### floria-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### floria-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### floria-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### floria-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### floria

```bash
$ singularity exec <container> /usr/local/bin/floria
$ podman run --it --rm --entrypoint /usr/local/bin/floria   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/floria   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vartig-dump

```bash
$ singularity exec <container> /usr/local/bin/vartig-dump
$ podman run --it --rm --entrypoint /usr/local/bin/vartig-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vartig-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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