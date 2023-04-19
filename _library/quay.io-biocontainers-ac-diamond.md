---
layout: container
name:  "quay.io/biocontainers/ac-diamond"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ac-diamond/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ac-diamond/container.yaml"
updated_at: "2023-04-19 03:18:56.728785"
latest: "1.0--h46c59ee_4"
container_url: "https://biocontainers.pro/tools/ac-diamond"
aliases:
 - "ac-diamond"
versions:
 - "1.0--h46c59ee_4"
description: "shpc-registry automated BioContainers addition for ac-diamond"
config: {"url": "https://biocontainers.pro/tools/ac-diamond", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ac-diamond", "latest": {"1.0--h46c59ee_4": "sha256:797beea248d4d705ae728663cb7ce82fc873b790fdfb774c61ae18ac416d596a"}, "tags": {"1.0--h46c59ee_4": "sha256:797beea248d4d705ae728663cb7ce82fc873b790fdfb774c61ae18ac416d596a"}, "docker": "quay.io/biocontainers/ac-diamond", "aliases": {"ac-diamond": "/usr/local/bin/ac-diamond"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ac-diamond.
shpc-registry automated BioContainers addition for ac-diamond
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ac-diamond
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ac-diamond:1.0--h46c59ee_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ac-diamond/1.0--h46c59ee_4
$ module help quay.io/biocontainers/ac-diamond/1.0--h46c59ee_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ac-diamond-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ac-diamond-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ac-diamond-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ac-diamond-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ac-diamond-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ac-diamond-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ac-diamond

```bash
$ singularity exec <container> /usr/local/bin/ac-diamond
$ podman run --it --rm --entrypoint /usr/local/bin/ac-diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ac-diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
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