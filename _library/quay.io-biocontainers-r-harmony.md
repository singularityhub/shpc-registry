---
layout: container
name:  "quay.io/biocontainers/r-harmony"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-harmony/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-harmony/container.yaml"
updated_at: "2024-06-24 03:13:05.533521"
latest: "0.1--r43h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/r-harmony"

versions:
 - "0.1--r41h9f5acd7_3"
 - "0.1--r42h9f5acd7_4"
 - "0.1--r42h4ac6f70_5"
 - "0.1--r43h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for r-harmony"
config: {"url": "https://biocontainers.pro/tools/r-harmony", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-harmony", "latest": {"0.1--r43h4ac6f70_6": "sha256:d79d03066f8a704ad3ca4fa653d0e1e3eed2457a66d33f9e9fd93ddf0f66e857"}, "tags": {"0.1--r41h9f5acd7_3": "sha256:1fd01dbb8a21e4a10b2009513d6d34b85264fe6a11a8cd831a8111a8b99b7e1a", "0.1--r42h9f5acd7_4": "sha256:02a01d55d46df5ef85d305bece69df615b0c77bb0c0b91e9a2a4d588a3547a9f", "0.1--r42h4ac6f70_5": "sha256:dc93a4a12e6cec1dec913ff8f7053092a83ca18ee22c0b7eadc6eb6a6da5b73a", "0.1--r43h4ac6f70_6": "sha256:d79d03066f8a704ad3ca4fa653d0e1e3eed2457a66d33f9e9fd93ddf0f66e857"}, "docker": "quay.io/biocontainers/r-harmony"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-harmony.
shpc-registry automated BioContainers addition for r-harmony
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-harmony
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-harmony:0.1--r43h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-harmony/0.1--r43h4ac6f70_6
$ module help quay.io/biocontainers/r-harmony/0.1--r43h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-harmony-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-harmony-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-harmony-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-harmony-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-harmony-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-harmony-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-harmony

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