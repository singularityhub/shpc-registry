---
layout: container
name:  "quay.io/biocontainers/segmentation-fold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/segmentation-fold/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/segmentation-fold/container.yaml"
updated_at: "2022-10-27 00:47:50.045244"
latest: "1.7.0--py27hc30c61c_4"
container_url: "https://biocontainers.pro/tools/segmentation-fold"
aliases:
 - "segmentation-fold"
 - "segmentation-fold-utils"
versions:
 - "1.7.0--py27hc30c61c_4"
description: "shpc-registry automated BioContainers addition for segmentation-fold"
config: {"url": "https://biocontainers.pro/tools/segmentation-fold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for segmentation-fold", "latest": {"1.7.0--py27hc30c61c_4": "sha256:91b7e28d5b67c44d7246e462e282835dd16a47d723fcf35dcabb94ec455bdf79"}, "tags": {"1.7.0--py27hc30c61c_4": "sha256:91b7e28d5b67c44d7246e462e282835dd16a47d723fcf35dcabb94ec455bdf79"}, "docker": "quay.io/biocontainers/segmentation-fold", "aliases": {"segmentation-fold": "/usr/local/bin/segmentation-fold", "segmentation-fold-utils": "/usr/local/bin/segmentation-fold-utils"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/segmentation-fold.
shpc-registry automated BioContainers addition for segmentation-fold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/segmentation-fold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/segmentation-fold:1.7.0--py27hc30c61c_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/segmentation-fold/1.7.0--py27hc30c61c_4
$ module help quay.io/biocontainers/segmentation-fold/1.7.0--py27hc30c61c_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### segmentation-fold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### segmentation-fold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### segmentation-fold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### segmentation-fold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### segmentation-fold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### segmentation-fold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### segmentation-fold

```bash
$ singularity exec <container> /usr/local/bin/segmentation-fold
$ podman run --it --rm --entrypoint /usr/local/bin/segmentation-fold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentation-fold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segmentation-fold-utils

```bash
$ singularity exec <container> /usr/local/bin/segmentation-fold-utils
$ podman run --it --rm --entrypoint /usr/local/bin/segmentation-fold-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segmentation-fold-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
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