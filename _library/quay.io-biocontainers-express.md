---
layout: container
name:  "quay.io/biocontainers/express"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/express/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/express/container.yaml"
updated_at: "2024-02-12 02:58:58.303166"
latest: "1.5.1--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/express"
aliases:
 - "express"
versions:
 - "1.5.1--h9f5acd7_4"
 - "1.5.1--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for express"
config: {"url": "https://biocontainers.pro/tools/express", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for express", "latest": {"1.5.1--h4ac6f70_5": "sha256:46117ecce1459271890c1095a8bea2293abd8ed0cbd44f9d8e981e6bdd6a0dd8"}, "tags": {"1.5.1--h9f5acd7_4": "sha256:47689fffe3e46a7195ad0d4784732e37840f78d23f1d10b86c99d4edc68a15a6", "1.5.1--h4ac6f70_5": "sha256:46117ecce1459271890c1095a8bea2293abd8ed0cbd44f9d8e981e6bdd6a0dd8"}, "docker": "quay.io/biocontainers/express", "aliases": {"express": "/usr/local/bin/express"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/express.
shpc-registry automated BioContainers addition for express
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/express
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/express:1.5.1--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/express/1.5.1--h4ac6f70_5
$ module help quay.io/biocontainers/express/1.5.1--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### express-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### express-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### express-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### express-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### express-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### express-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### express

```bash
$ singularity exec <container> /usr/local/bin/express
$ podman run --it --rm --entrypoint /usr/local/bin/express   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/express   -v ${PWD} -w ${PWD} <container> -c " $@"
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