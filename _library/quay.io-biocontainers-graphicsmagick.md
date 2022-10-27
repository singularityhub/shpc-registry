---
layout: container
name:  "quay.io/biocontainers/graphicsmagick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphicsmagick/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/graphicsmagick/container.yaml"
updated_at: "2022-10-27 00:50:10.884878"
latest: "1.3.31"
container_url: "https://biocontainers.pro/tools/graphicsmagick"
aliases:
 - "GraphicsMagick++-config"
 - "GraphicsMagick-config"
 - "GraphicsMagickWand-config"
 - "gm"
versions:
 - "1.3.31"
description: "shpc-registry automated BioContainers addition for graphicsmagick"
config: {"url": "https://biocontainers.pro/tools/graphicsmagick", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphicsmagick", "latest": {"1.3.31": "sha256:bcaebffbf74e0f876cef6389016aa87ae62f58d6f0c09508fba62361f610c87e"}, "tags": {"1.3.31": "sha256:bcaebffbf74e0f876cef6389016aa87ae62f58d6f0c09508fba62361f610c87e"}, "docker": "quay.io/biocontainers/graphicsmagick", "aliases": {"GraphicsMagick++-config": "/usr/local/bin/GraphicsMagick++-config", "GraphicsMagick-config": "/usr/local/bin/GraphicsMagick-config", "GraphicsMagickWand-config": "/usr/local/bin/GraphicsMagickWand-config", "gm": "/usr/local/bin/gm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphicsmagick.
shpc-registry automated BioContainers addition for graphicsmagick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphicsmagick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphicsmagick:1.3.31
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphicsmagick/1.3.31
$ module help quay.io/biocontainers/graphicsmagick/1.3.31
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphicsmagick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphicsmagick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphicsmagick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphicsmagick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphicsmagick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphicsmagick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GraphicsMagick++-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagick-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagick-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagick-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GraphicsMagickWand-config

```bash
$ singularity exec <container> /usr/local/bin/GraphicsMagickWand-config
$ podman run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GraphicsMagickWand-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gm

```bash
$ singularity exec <container> /usr/local/bin/gm
$ podman run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gm   -v ${PWD} -w ${PWD} <container> -c " $@"
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