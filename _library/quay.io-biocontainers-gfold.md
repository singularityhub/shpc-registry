---
layout: container
name:  "quay.io/biocontainers/gfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfold/container.yaml"
updated_at: "2023-11-17 02:37:18.700754"
latest: "1.1.4--gsl2.2_2"
container_url: "https://biocontainers.pro/tools/gfold"
aliases:
 - "gfold"
versions:
 - "1.1.4--gsl2.2_2"
description: "shpc-registry automated BioContainers addition for gfold"
config: {"url": "https://biocontainers.pro/tools/gfold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gfold", "latest": {"1.1.4--gsl2.2_2": "sha256:45631bb47bd1213148e147edab18b2413b8bb9da1c17358a0b743313fbc3c962"}, "tags": {"1.1.4--gsl2.2_2": "sha256:45631bb47bd1213148e147edab18b2413b8bb9da1c17358a0b743313fbc3c962"}, "docker": "quay.io/biocontainers/gfold", "aliases": {"gfold": "/usr/local/bin/gfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfold.
shpc-registry automated BioContainers addition for gfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfold:1.1.4--gsl2.2_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfold/1.1.4--gsl2.2_2
$ module help quay.io/biocontainers/gfold/1.1.4--gsl2.2_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfold

```bash
$ singularity exec <container> /usr/local/bin/gfold
$ podman run --it --rm --entrypoint /usr/local/bin/gfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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