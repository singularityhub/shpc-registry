---
layout: container
name:  "quay.io/biocontainers/cgt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgt/container.yaml"
updated_at: "2025-09-11 05:26:18.610003"
latest: "1.0.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/cgt"
aliases:
 - "cgt_bacpop"
versions:
 - "1.0.0--h4349ce8_0"
description: "singularity registry hpc automated addition for cgt"
config: {"url": "https://biocontainers.pro/tools/cgt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cgt", "latest": {"1.0.0--h4349ce8_0": "sha256:23f3cdc3f1de65ff9e1f2f673d68488587bb20ac37403417559918fc2aca3225"}, "tags": {"1.0.0--h4349ce8_0": "sha256:23f3cdc3f1de65ff9e1f2f673d68488587bb20ac37403417559918fc2aca3225"}, "docker": "quay.io/biocontainers/cgt", "aliases": {"cgt_bacpop": "/usr/local/bin/cgt_bacpop"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgt.
singularity registry hpc automated addition for cgt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgt:1.0.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgt/1.0.0--h4349ce8_0
$ module help quay.io/biocontainers/cgt/1.0.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cgt_bacpop

```bash
$ singularity exec <container> /usr/local/bin/cgt_bacpop
$ podman run --it --rm --entrypoint /usr/local/bin/cgt_bacpop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgt_bacpop   -v ${PWD} -w ${PWD} <container> -c " $@"
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