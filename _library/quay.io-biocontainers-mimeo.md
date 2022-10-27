---
layout: container
name:  "quay.io/biocontainers/mimeo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mimeo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mimeo/container.yaml"
updated_at: "2022-10-27 01:07:08.077020"
latest: "1.1.1--py_2"
container_url: "https://biocontainers.pro/tools/mimeo"
aliases:
 - "mimeo-filter"
 - "mimeo-map"
 - "mimeo-self"
 - "mimeo-x"
versions:
 - "1.1.1--py_2"
description: "shpc-registry automated BioContainers addition for mimeo"
config: {"url": "https://biocontainers.pro/tools/mimeo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mimeo", "latest": {"1.1.1--py_2": "sha256:4776e95a6b2610efb94a1bafb21ec75b8e02ecc726404116b1130fe80a8a666e"}, "tags": {"1.1.1--py_2": "sha256:4776e95a6b2610efb94a1bafb21ec75b8e02ecc726404116b1130fe80a8a666e"}, "docker": "quay.io/biocontainers/mimeo", "aliases": {"mimeo-filter": "/usr/local/bin/mimeo-filter", "mimeo-map": "/usr/local/bin/mimeo-map", "mimeo-self": "/usr/local/bin/mimeo-self", "mimeo-x": "/usr/local/bin/mimeo-x"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mimeo.
shpc-registry automated BioContainers addition for mimeo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mimeo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mimeo:1.1.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mimeo/1.1.1--py_2
$ module help quay.io/biocontainers/mimeo/1.1.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mimeo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mimeo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mimeo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mimeo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mimeo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mimeo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mimeo-filter

```bash
$ singularity exec <container> /usr/local/bin/mimeo-filter
$ podman run --it --rm --entrypoint /usr/local/bin/mimeo-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimeo-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimeo-map

```bash
$ singularity exec <container> /usr/local/bin/mimeo-map
$ podman run --it --rm --entrypoint /usr/local/bin/mimeo-map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimeo-map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimeo-self

```bash
$ singularity exec <container> /usr/local/bin/mimeo-self
$ podman run --it --rm --entrypoint /usr/local/bin/mimeo-self   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimeo-self   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mimeo-x

```bash
$ singularity exec <container> /usr/local/bin/mimeo-x
$ podman run --it --rm --entrypoint /usr/local/bin/mimeo-x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mimeo-x   -v ${PWD} -w ${PWD} <container> -c " $@"
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