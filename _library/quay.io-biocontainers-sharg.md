---
layout: container
name:  "quay.io/biocontainers/sharg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sharg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sharg/container.yaml"
updated_at: "2024-10-21 03:32:09.666834"
latest: "1.1.1--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/sharg"

versions:
 - "1.1.1--h4ac6f70_0"
description: "singularity registry hpc automated addition for sharg"
config: {"url": "https://biocontainers.pro/tools/sharg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sharg", "latest": {"1.1.1--h4ac6f70_0": "sha256:6bca616723eafdb581679add5354eab9c0aa1b1c0fab2d9c004eeb43d5698c89"}, "tags": {"1.1.1--h4ac6f70_0": "sha256:6bca616723eafdb581679add5354eab9c0aa1b1c0fab2d9c004eeb43d5698c89"}, "docker": "quay.io/biocontainers/sharg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sharg.
singularity registry hpc automated addition for sharg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sharg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sharg:1.1.1--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sharg/1.1.1--h4ac6f70_0
$ module help quay.io/biocontainers/sharg/1.1.1--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sharg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sharg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sharg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sharg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sharg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sharg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sharg

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