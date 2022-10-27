---
layout: container
name:  "quay.io/biocontainers/xpressplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xpressplot/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/xpressplot/container.yaml"
updated_at: "2022-10-27 00:27:22.177947"
latest: "0.2.5--pyh4c3bd37_1"
container_url: "https://biocontainers.pro/tools/xpressplot"

versions:
 - "0.2.5--pyh4c3bd37_1"
description: "shpc-registry automated BioContainers addition for xpressplot"
config: {"url": "https://biocontainers.pro/tools/xpressplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xpressplot", "latest": {"0.2.5--pyh4c3bd37_1": "sha256:51b3684c13d6205e7d6981377039f7a19f324e9efe9f90ef6fb6f8a5c7d1b378"}, "tags": {"0.2.5--pyh4c3bd37_1": "sha256:51b3684c13d6205e7d6981377039f7a19f324e9efe9f90ef6fb6f8a5c7d1b378"}, "docker": "quay.io/biocontainers/xpressplot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/xpressplot.
shpc-registry automated BioContainers addition for xpressplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xpressplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xpressplot:0.2.5--pyh4c3bd37_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xpressplot/0.2.5--pyh4c3bd37_1
$ module help quay.io/biocontainers/xpressplot/0.2.5--pyh4c3bd37_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xpressplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xpressplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xpressplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xpressplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xpressplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xpressplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### xpressplot

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