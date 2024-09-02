---
layout: container
name:  "quay.io/biocontainers/famsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/famsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/famsa/container.yaml"
updated_at: "2024-09-02 04:55:09.701174"
latest: "2.2.2--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/famsa"
aliases:
 - "famsa"
versions:
 - "2.2.2--h9f5acd7_0"
 - "2.2.2--h4ac6f70_2"
 - "2.2.2--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for famsa"
config: {"url": "https://biocontainers.pro/tools/famsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for famsa", "latest": {"2.2.2--h4ac6f70_3": "sha256:ea767b8fb88cc2bc44e448260d4ab0e33a2625af5ba7c25d265f86fc5d9e28b6"}, "tags": {"2.2.2--h9f5acd7_0": "sha256:7ebd3d06ba7e5e2300ebcb17e7c69becc35032257e4d5c9e3861f523c4be6cdf", "2.2.2--h4ac6f70_2": "sha256:ff0191e94c25a2a9f260a84b167a8feb8435ba857f80434e92b7ff56f7f3913a", "2.2.2--h4ac6f70_3": "sha256:ea767b8fb88cc2bc44e448260d4ab0e33a2625af5ba7c25d265f86fc5d9e28b6"}, "docker": "quay.io/biocontainers/famsa", "aliases": {"famsa": "/usr/local/bin/famsa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/famsa.
shpc-registry automated BioContainers addition for famsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/famsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/famsa:2.2.2--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/famsa/2.2.2--h4ac6f70_3
$ module help quay.io/biocontainers/famsa/2.2.2--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### famsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### famsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### famsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### famsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### famsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### famsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### famsa

```bash
$ singularity exec <container> /usr/local/bin/famsa
$ podman run --it --rm --entrypoint /usr/local/bin/famsa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famsa   -v ${PWD} -w ${PWD} <container> -c " $@"
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