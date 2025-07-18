---
layout: container
name:  "quay.io/biocontainers/r-imputelcmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-imputelcmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-imputelcmd/container.yaml"
updated_at: "2025-07-18 04:09:46.787316"
latest: "2.1--r44h3342da4_3"
container_url: "https://biocontainers.pro/tools/r-imputelcmd"

versions:
 - "2.1--r41h3342da4_0"
 - "2.1--r42h3342da4_1"
 - "2.1--r43h3342da4_2"
 - "2.1--r44h3342da4_3"
description: "shpc-registry automated BioContainers addition for r-imputelcmd"
config: {"url": "https://biocontainers.pro/tools/r-imputelcmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-imputelcmd", "latest": {"2.1--r44h3342da4_3": "sha256:6f47f6cf2dfb0c7525dfa91643aac5c8bd0b4a63832e7ea0b56c6ac4b01dcf07"}, "tags": {"2.1--r41h3342da4_0": "sha256:8e72a79befe6e598ed2abed2cd14e03175864f4ae580a4aeaf3769be7fe61694", "2.1--r42h3342da4_1": "sha256:3758488584b4da3f9758658e47852c231aa2c2e9a0745c6b0fc0796876bb1c31", "2.1--r43h3342da4_2": "sha256:664a4ce121cd696f5e2f62fbf186d60e44df0bea1c3652ffcd3f03eb9806fa71", "2.1--r44h3342da4_3": "sha256:6f47f6cf2dfb0c7525dfa91643aac5c8bd0b4a63832e7ea0b56c6ac4b01dcf07"}, "docker": "quay.io/biocontainers/r-imputelcmd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-imputelcmd.
shpc-registry automated BioContainers addition for r-imputelcmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-imputelcmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-imputelcmd:2.1--r44h3342da4_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-imputelcmd/2.1--r44h3342da4_3
$ module help quay.io/biocontainers/r-imputelcmd/2.1--r44h3342da4_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-imputelcmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-imputelcmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-imputelcmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-imputelcmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-imputelcmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-imputelcmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-imputelcmd

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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