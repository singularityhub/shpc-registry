---
layout: container
name:  "quay.io/biocontainers/isoplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isoplot/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/isoplot/container.yaml"
updated_at: "2022-10-27 01:11:46.947619"
latest: "1.3.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/isoplot"
aliases:
 - "colorcet"
 - "isoplot"
versions:
 - "1.3.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for isoplot"
config: {"url": "https://biocontainers.pro/tools/isoplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isoplot", "latest": {"1.3.1--pyh5e36f6f_0": "sha256:0bb7ac6f3617ff2c64405e3da2458ebf71be25b26ece2b817c1376b425ac90d7"}, "tags": {"1.3.1--pyh5e36f6f_0": "sha256:0bb7ac6f3617ff2c64405e3da2458ebf71be25b26ece2b817c1376b425ac90d7"}, "docker": "quay.io/biocontainers/isoplot", "aliases": {"colorcet": "/usr/local/bin/colorcet", "isoplot": "/usr/local/bin/isoplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isoplot.
shpc-registry automated BioContainers addition for isoplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isoplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isoplot:1.3.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isoplot/1.3.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/isoplot/1.3.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isoplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isoplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isoplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isoplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isoplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isoplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### colorcet

```bash
$ singularity exec <container> /usr/local/bin/colorcet
$ podman run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isoplot

```bash
$ singularity exec <container> /usr/local/bin/isoplot
$ podman run --it --rm --entrypoint /usr/local/bin/isoplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isoplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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