---
layout: container
name:  "quay.io/biocontainers/ripser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ripser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ripser/container.yaml"
updated_at: "2025-02-27 03:38:34.211611"
latest: "1.0.1--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/ripser"
aliases:
 - "ripser"
 - "ripser-coeff"
 - "ripser-debug"
versions:
 - "1.0.1--h9f5acd7_3"
 - "1.0.1--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for ripser"
config: {"url": "https://biocontainers.pro/tools/ripser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ripser", "latest": {"1.0.1--h9f5acd7_4": "sha256:316e4319f94d9fd2de02e39f2910efa27d05b9a6760dd40e548c09b3a3d7cfea"}, "tags": {"1.0.1--h9f5acd7_3": "sha256:f14e81d5860619c05c37eb648f977417eddfda5c2f3f1fa43c56b1a0bc1817e7", "1.0.1--h9f5acd7_4": "sha256:316e4319f94d9fd2de02e39f2910efa27d05b9a6760dd40e548c09b3a3d7cfea"}, "docker": "quay.io/biocontainers/ripser", "aliases": {"ripser": "/usr/local/bin/ripser", "ripser-coeff": "/usr/local/bin/ripser-coeff", "ripser-debug": "/usr/local/bin/ripser-debug"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ripser.
shpc-registry automated BioContainers addition for ripser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ripser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ripser:1.0.1--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ripser/1.0.1--h9f5acd7_4
$ module help quay.io/biocontainers/ripser/1.0.1--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ripser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ripser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ripser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ripser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ripser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ripser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ripser

```bash
$ singularity exec <container> /usr/local/bin/ripser
$ podman run --it --rm --entrypoint /usr/local/bin/ripser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ripser-coeff

```bash
$ singularity exec <container> /usr/local/bin/ripser-coeff
$ podman run --it --rm --entrypoint /usr/local/bin/ripser-coeff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripser-coeff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ripser-debug

```bash
$ singularity exec <container> /usr/local/bin/ripser-debug
$ podman run --it --rm --entrypoint /usr/local/bin/ripser-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ripser-debug   -v ${PWD} -w ${PWD} <container> -c " $@"
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