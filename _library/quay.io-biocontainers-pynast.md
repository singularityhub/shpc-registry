---
layout: container
name:  "quay.io/biocontainers/pynast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pynast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pynast/container.yaml"
updated_at: "2022-10-27 00:19:54.085470"
latest: "1.2.2--py_2"
container_url: "https://biocontainers.pro/tools/pynast"
aliases:
 - "pynast"
versions:
 - "1.2.2--py_2"
description: "shpc-registry automated BioContainers addition for pynast"
config: {"url": "https://biocontainers.pro/tools/pynast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pynast", "latest": {"1.2.2--py_2": "sha256:f37a0932d07dd33286e49504a97dd1c339f8c3e62f6a6dc65ea1ec4e6569f8a9"}, "tags": {"1.2.2--py_2": "sha256:f37a0932d07dd33286e49504a97dd1c339f8c3e62f6a6dc65ea1ec4e6569f8a9"}, "docker": "quay.io/biocontainers/pynast", "aliases": {"pynast": "/usr/local/bin/pynast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pynast.
shpc-registry automated BioContainers addition for pynast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pynast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pynast:1.2.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pynast/1.2.2--py_2
$ module help quay.io/biocontainers/pynast/1.2.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pynast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pynast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pynast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pynast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pynast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pynast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pynast

```bash
$ singularity exec <container> /usr/local/bin/pynast
$ podman run --it --rm --entrypoint /usr/local/bin/pynast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pynast   -v ${PWD} -w ${PWD} <container> -c " $@"
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