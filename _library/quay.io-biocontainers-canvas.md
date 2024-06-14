---
layout: container
name:  "quay.io/biocontainers/canvas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/canvas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/canvas/container.yaml"
updated_at: "2024-06-14 02:58:24.526709"
latest: "1.35.1.1316--0"
container_url: "https://biocontainers.pro/tools/canvas"
aliases:
 - "Canvas"
 - "EvaluateCNV"
versions:
 - "1.35.1.1316--0"
description: "shpc-registry automated BioContainers addition for canvas"
config: {"url": "https://biocontainers.pro/tools/canvas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for canvas", "latest": {"1.35.1.1316--0": "sha256:451402da5627cab049012dbe0134679a6c0067e3140efd1f91e492dfdf61d940"}, "tags": {"1.35.1.1316--0": "sha256:451402da5627cab049012dbe0134679a6c0067e3140efd1f91e492dfdf61d940"}, "docker": "quay.io/biocontainers/canvas", "aliases": {"Canvas": "/usr/local/bin/Canvas", "EvaluateCNV": "/usr/local/bin/EvaluateCNV"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/canvas.
shpc-registry automated BioContainers addition for canvas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/canvas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/canvas:1.35.1.1316--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/canvas/1.35.1.1316--0
$ module help quay.io/biocontainers/canvas/1.35.1.1316--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### canvas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### canvas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### canvas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### canvas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### canvas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### canvas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Canvas

```bash
$ singularity exec <container> /usr/local/bin/Canvas
$ podman run --it --rm --entrypoint /usr/local/bin/Canvas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Canvas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EvaluateCNV

```bash
$ singularity exec <container> /usr/local/bin/EvaluateCNV
$ podman run --it --rm --entrypoint /usr/local/bin/EvaluateCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EvaluateCNV   -v ${PWD} -w ${PWD} <container> -c " $@"
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