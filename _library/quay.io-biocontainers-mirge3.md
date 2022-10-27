---
layout: container
name:  "quay.io/biocontainers/mirge3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirge3/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mirge3/container.yaml"
updated_at: "2022-10-27 01:07:04.140342"
latest: "0.1.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/mirge3"
aliases:
 - "miRge3.0"
versions:
 - "0.1.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for mirge3"
config: {"url": "https://biocontainers.pro/tools/mirge3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirge3", "latest": {"0.1.1--pyh7cba7a3_0": "sha256:d67c441abb353724e1496973852b3ab0b52e1965cd1067d8ee60b634b70c53e4"}, "tags": {"0.1.1--pyh7cba7a3_0": "sha256:d67c441abb353724e1496973852b3ab0b52e1965cd1067d8ee60b634b70c53e4"}, "docker": "quay.io/biocontainers/mirge3", "aliases": {"miRge3.0": "/usr/local/bin/miRge3.0"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirge3.
shpc-registry automated BioContainers addition for mirge3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirge3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirge3:0.1.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirge3/0.1.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/mirge3/0.1.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirge3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirge3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirge3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirge3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirge3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirge3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miRge3.0

```bash
$ singularity exec <container> /usr/local/bin/miRge3.0
$ podman run --it --rm --entrypoint /usr/local/bin/miRge3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miRge3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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