---
layout: container
name:  "quay.io/biocontainers/skani"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/skani/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/skani/container.yaml"
updated_at: "2024-06-09 02:39:00.080564"
latest: "0.2.1--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/skani"
aliases:
 - "skani"
versions:
 - "0.1.0--h9f5acd7_0"
 - "0.1.1--h9f5acd7_0"
 - "0.1.3--h9f5acd7_0"
 - "0.1.3--h4ac6f70_2"
 - "0.1.4--h4ac6f70_0"
 - "0.1.5--h4ac6f70_0"
 - "0.2.1--h4ac6f70_0"
description: "singularity registry hpc automated addition for skani"
config: {"url": "https://biocontainers.pro/tools/skani", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for skani", "latest": {"0.2.1--h4ac6f70_0": "sha256:ae0af15139b6189f477dae79098951e0d60abb3a0ff23727428cf14ea3907ee7"}, "tags": {"0.1.0--h9f5acd7_0": "sha256:b3d0afd09f684cbcb92b73737db2a0f75421c008804a66ba2a3f04357076facf", "0.1.1--h9f5acd7_0": "sha256:9db3ad6c21b830bee564baca3b957f6565c0a1d177262b6e68289fe34a9c9e54", "0.1.3--h9f5acd7_0": "sha256:2ea1d3d1d3faf96963c4b7abd3d5af512b1cba1c90b01dbbc4246ba786a3c5ba", "0.1.3--h4ac6f70_2": "sha256:70f6761b55bab2c937deee47d0ef5624817b83a879e3a19c95198eabe951d232", "0.1.4--h4ac6f70_0": "sha256:56977563b025868422c3c380156d4b135f931d674b7e68a41f9f8ed8fb39347f", "0.1.5--h4ac6f70_0": "sha256:75111df14faf2c15c1ed8fa1a7a642bac0298b5f5d0863014c9a06c7b45fbb86", "0.2.1--h4ac6f70_0": "sha256:ae0af15139b6189f477dae79098951e0d60abb3a0ff23727428cf14ea3907ee7"}, "docker": "quay.io/biocontainers/skani", "aliases": {"skani": "/usr/local/bin/skani"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/skani.
singularity registry hpc automated addition for skani
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/skani
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/skani:0.2.1--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/skani/0.2.1--h4ac6f70_0
$ module help quay.io/biocontainers/skani/0.2.1--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### skani-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### skani-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### skani-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### skani-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### skani-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### skani-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
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