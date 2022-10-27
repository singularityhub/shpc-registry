---
layout: container
name:  "quay.io/biocontainers/cpinsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cpinsim/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cpinsim/container.yaml"
updated_at: "2022-10-27 00:52:20.048317"
latest: "0.5.2--py_2"
container_url: "https://biocontainers.pro/tools/cpinsim"
aliases:
 - "cpinsim"
versions:
 - "0.5.2--py_2"
description: "shpc-registry automated BioContainers addition for cpinsim"
config: {"url": "https://biocontainers.pro/tools/cpinsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cpinsim", "latest": {"0.5.2--py_2": "sha256:ce61043401f83e0b0ad79d35809a78ce0c2454173980de3b49e79a6541b8cd83"}, "tags": {"0.5.2--py_2": "sha256:ce61043401f83e0b0ad79d35809a78ce0c2454173980de3b49e79a6541b8cd83"}, "docker": "quay.io/biocontainers/cpinsim", "aliases": {"cpinsim": "/usr/local/bin/cpinsim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cpinsim.
shpc-registry automated BioContainers addition for cpinsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cpinsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cpinsim:0.5.2--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cpinsim/0.5.2--py_2
$ module help quay.io/biocontainers/cpinsim/0.5.2--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cpinsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cpinsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cpinsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cpinsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cpinsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cpinsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpinsim

```bash
$ singularity exec <container> /usr/local/bin/cpinsim
$ podman run --it --rm --entrypoint /usr/local/bin/cpinsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpinsim   -v ${PWD} -w ${PWD} <container> -c " $@"
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