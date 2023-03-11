---
layout: container
name:  "quay.io/biocontainers/pp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pp/container.yaml"
updated_at: "2023-03-11 20:45:25.388147"
latest: "1.6.5--py_2"
container_url: "https://biocontainers.pro/tools/pp"

versions:
 - "1.6.5--py_2"
description: "shpc-registry automated BioContainers addition for pp"
config: {"url": "https://biocontainers.pro/tools/pp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pp", "latest": {"1.6.5--py_2": "sha256:38d77ea9504239cd97e9f26d864db46c5dc0ff684c6afc5dd74cce1d0ba3fc21"}, "tags": {"1.6.5--py_2": "sha256:38d77ea9504239cd97e9f26d864db46c5dc0ff684c6afc5dd74cce1d0ba3fc21"}, "docker": "quay.io/biocontainers/pp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pp.
shpc-registry automated BioContainers addition for pp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pp:1.6.5--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pp/1.6.5--py_2
$ module help quay.io/biocontainers/pp/1.6.5--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pp

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