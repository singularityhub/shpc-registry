---
layout: container
name:  "quay.io/biocontainers/rmats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rmats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rmats/container.yaml"
updated_at: "2023-03-15 03:13:45.814693"
latest: "4.1.2--py27ha9cf2de_4"
container_url: "https://biocontainers.pro/tools/rmats"

versions:
 - "4.1.2--py27ha9cf2de_4"
description: "shpc-registry automated BioContainers addition for rmats"
config: {"url": "https://biocontainers.pro/tools/rmats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rmats", "latest": {"4.1.2--py27ha9cf2de_4": "sha256:fa9c99eee212bbb11275d6c19cb9a77667dcec12b70e46f39eef488b80007b41"}, "tags": {"4.1.2--py27ha9cf2de_4": "sha256:fa9c99eee212bbb11275d6c19cb9a77667dcec12b70e46f39eef488b80007b41"}, "docker": "quay.io/biocontainers/rmats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/rmats.
shpc-registry automated BioContainers addition for rmats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rmats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rmats:4.1.2--py27ha9cf2de_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rmats/4.1.2--py27ha9cf2de_4
$ module help quay.io/biocontainers/rmats/4.1.2--py27ha9cf2de_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rmats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rmats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rmats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rmats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rmats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rmats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### rmats

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