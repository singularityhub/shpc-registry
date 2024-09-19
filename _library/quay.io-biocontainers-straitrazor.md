---
layout: container
name:  "quay.io/biocontainers/straitrazor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/straitrazor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/straitrazor/container.yaml"
updated_at: "2024-09-19 03:13:01.405675"
latest: "3.0.1--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/straitrazor"
aliases:
 - "str8rzr"
versions:
 - "3.0.1--h9f5acd7_4"
 - "3.0.1--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for straitrazor"
config: {"url": "https://biocontainers.pro/tools/straitrazor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for straitrazor", "latest": {"3.0.1--h4ac6f70_6": "sha256:bb0bb0479c18127414e44f8124531875932a31238279b33baaabb063ff0b097e"}, "tags": {"3.0.1--h9f5acd7_4": "sha256:5b33438bf941d1b8a2d963f1b04342c398d72543c467fdde8aaf8b6f8d41b7f5", "3.0.1--h4ac6f70_6": "sha256:bb0bb0479c18127414e44f8124531875932a31238279b33baaabb063ff0b097e"}, "docker": "quay.io/biocontainers/straitrazor", "aliases": {"str8rzr": "/usr/local/bin/str8rzr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/straitrazor.
shpc-registry automated BioContainers addition for straitrazor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/straitrazor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/straitrazor:3.0.1--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/straitrazor/3.0.1--h4ac6f70_6
$ module help quay.io/biocontainers/straitrazor/3.0.1--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### straitrazor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### straitrazor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### straitrazor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### straitrazor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### straitrazor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### straitrazor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### str8rzr

```bash
$ singularity exec <container> /usr/local/bin/str8rzr
$ podman run --it --rm --entrypoint /usr/local/bin/str8rzr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/str8rzr   -v ${PWD} -w ${PWD} <container> -c " $@"
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