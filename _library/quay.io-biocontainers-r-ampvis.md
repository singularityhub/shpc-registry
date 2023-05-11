---
layout: container
name:  "quay.io/biocontainers/r-ampvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ampvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ampvis/container.yaml"
updated_at: "2023-05-11 03:29:52.632073"
latest: "1.27.0--r42h9ee0642_5"
container_url: "https://biocontainers.pro/tools/r-ampvis"

versions:
 - "1.27.0--r41h9ee0642_4"
 - "1.27.0--r42h9ee0642_5"
description: "shpc-registry automated BioContainers addition for r-ampvis"
config: {"url": "https://biocontainers.pro/tools/r-ampvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ampvis", "latest": {"1.27.0--r42h9ee0642_5": "sha256:b27ef38ca5c43156ecf172daea440effb2574ffa13830c2ca6575201dd4cbea7"}, "tags": {"1.27.0--r41h9ee0642_4": "sha256:1973dfdc21e256b0bcff8db72d413e083384f3dd3aa17771409a9f9ffa567dd4", "1.27.0--r42h9ee0642_5": "sha256:b27ef38ca5c43156ecf172daea440effb2574ffa13830c2ca6575201dd4cbea7"}, "docker": "quay.io/biocontainers/r-ampvis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ampvis.
shpc-registry automated BioContainers addition for r-ampvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ampvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ampvis:1.27.0--r42h9ee0642_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ampvis/1.27.0--r42h9ee0642_5
$ module help quay.io/biocontainers/r-ampvis/1.27.0--r42h9ee0642_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ampvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ampvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ampvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ampvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ampvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ampvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ampvis

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