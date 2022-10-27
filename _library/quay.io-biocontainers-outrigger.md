---
layout: container
name:  "quay.io/biocontainers/outrigger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/outrigger/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/outrigger/container.yaml"
updated_at: "2022-10-27 00:44:48.759100"
latest: "1.1.1--pyh864c0ab_2"
container_url: "https://biocontainers.pro/tools/outrigger"
aliases:
 - "outrigger"
versions:
 - "1.1.1--pyh864c0ab_2"
description: "shpc-registry automated BioContainers addition for outrigger"
config: {"url": "https://biocontainers.pro/tools/outrigger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for outrigger", "latest": {"1.1.1--pyh864c0ab_2": "sha256:0a55b49a7076ec1a474536a3e4b01d99201e49488550e573a93a2b856f3007be"}, "tags": {"1.1.1--pyh864c0ab_2": "sha256:0a55b49a7076ec1a474536a3e4b01d99201e49488550e573a93a2b856f3007be"}, "docker": "quay.io/biocontainers/outrigger", "aliases": {"outrigger": "/usr/local/bin/outrigger"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/outrigger.
shpc-registry automated BioContainers addition for outrigger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/outrigger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/outrigger:1.1.1--pyh864c0ab_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/outrigger/1.1.1--pyh864c0ab_2
$ module help quay.io/biocontainers/outrigger/1.1.1--pyh864c0ab_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### outrigger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### outrigger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### outrigger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### outrigger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### outrigger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### outrigger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### outrigger

```bash
$ singularity exec <container> /usr/local/bin/outrigger
$ podman run --it --rm --entrypoint /usr/local/bin/outrigger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/outrigger   -v ${PWD} -w ${PWD} <container> -c " $@"
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