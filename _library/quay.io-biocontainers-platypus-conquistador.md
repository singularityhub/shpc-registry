---
layout: container
name:  "quay.io/biocontainers/platypus-conquistador"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/platypus-conquistador/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/platypus-conquistador/container.yaml"
updated_at: "2022-10-27 01:04:49.005289"
latest: "0.9.0--py_3"
container_url: "https://biocontainers.pro/tools/platypus-conquistador"
aliases:
 - "iptest2"
 - "ipython2"
 - "platypus"
versions:
 - "0.9.0--py_3"
description: "shpc-registry automated BioContainers addition for platypus-conquistador"
config: {"url": "https://biocontainers.pro/tools/platypus-conquistador", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for platypus-conquistador", "latest": {"0.9.0--py_3": "sha256:f42b19b89a5148a24001db71c20333a2dd6e7283e7c9e1d99d06a6d55a6ebed0"}, "tags": {"0.9.0--py_3": "sha256:f42b19b89a5148a24001db71c20333a2dd6e7283e7c9e1d99d06a6d55a6ebed0"}, "docker": "quay.io/biocontainers/platypus-conquistador", "aliases": {"iptest2": "/usr/local/bin/iptest2", "ipython2": "/usr/local/bin/ipython2", "platypus": "/usr/local/bin/platypus"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/platypus-conquistador.
shpc-registry automated BioContainers addition for platypus-conquistador
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/platypus-conquistador
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/platypus-conquistador:0.9.0--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/platypus-conquistador/0.9.0--py_3
$ module help quay.io/biocontainers/platypus-conquistador/0.9.0--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### platypus-conquistador-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### platypus-conquistador-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### platypus-conquistador-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### platypus-conquistador-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### platypus-conquistador-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### platypus-conquistador-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iptest2

```bash
$ singularity exec <container> /usr/local/bin/iptest2
$ podman run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython2

```bash
$ singularity exec <container> /usr/local/bin/ipython2
$ podman run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### platypus

```bash
$ singularity exec <container> /usr/local/bin/platypus
$ podman run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
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