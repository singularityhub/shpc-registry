---
layout: container
name:  "quay.io/biocontainers/cogtriangles"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cogtriangles/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cogtriangles/container.yaml"
updated_at: "2025-04-10 03:25:56.484759"
latest: "2012.04--h9948957_3"
container_url: "https://biocontainers.pro/tools/cogtriangles"
aliases:
 - "COGcognitor"
 - "COGlse"
 - "COGmakehash"
 - "COGreadblast"
 - "COGtriangles"
versions:
 - "2012.04--h9f5acd7_0"
 - "2012.04--h4ac6f70_2"
 - "2012.04--h9948957_3"
description: "singularity registry hpc automated addition for cogtriangles"
config: {"url": "https://biocontainers.pro/tools/cogtriangles", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cogtriangles", "latest": {"2012.04--h9948957_3": "sha256:9c261b22cd5a72bc6a1de716da12db30d53d7e18f1cb1232bfe89f5614e27821"}, "tags": {"2012.04--h9f5acd7_0": "sha256:5866743f34c05d57a7f1d3f3b9192d655a9ed3484be33c9a5613b10eea15f0c6", "2012.04--h4ac6f70_2": "sha256:f8085f47ce8b332340520c695ad1faf5113d2655d6cc9526244d672504139770", "2012.04--h9948957_3": "sha256:9c261b22cd5a72bc6a1de716da12db30d53d7e18f1cb1232bfe89f5614e27821"}, "docker": "quay.io/biocontainers/cogtriangles", "aliases": {"COGcognitor": "/usr/local/bin/COGcognitor", "COGlse": "/usr/local/bin/COGlse", "COGmakehash": "/usr/local/bin/COGmakehash", "COGreadblast": "/usr/local/bin/COGreadblast", "COGtriangles": "/usr/local/bin/COGtriangles"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cogtriangles.
singularity registry hpc automated addition for cogtriangles
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cogtriangles
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cogtriangles:2012.04--h9948957_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cogtriangles/2012.04--h9948957_3
$ module help quay.io/biocontainers/cogtriangles/2012.04--h9948957_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cogtriangles-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cogtriangles-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cogtriangles-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cogtriangles-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cogtriangles-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cogtriangles-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### COGcognitor

```bash
$ singularity exec <container> /usr/local/bin/COGcognitor
$ podman run --it --rm --entrypoint /usr/local/bin/COGcognitor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGcognitor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COGlse

```bash
$ singularity exec <container> /usr/local/bin/COGlse
$ podman run --it --rm --entrypoint /usr/local/bin/COGlse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGlse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COGmakehash

```bash
$ singularity exec <container> /usr/local/bin/COGmakehash
$ podman run --it --rm --entrypoint /usr/local/bin/COGmakehash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGmakehash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COGreadblast

```bash
$ singularity exec <container> /usr/local/bin/COGreadblast
$ podman run --it --rm --entrypoint /usr/local/bin/COGreadblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGreadblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COGtriangles

```bash
$ singularity exec <container> /usr/local/bin/COGtriangles
$ podman run --it --rm --entrypoint /usr/local/bin/COGtriangles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COGtriangles   -v ${PWD} -w ${PWD} <container> -c " $@"
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