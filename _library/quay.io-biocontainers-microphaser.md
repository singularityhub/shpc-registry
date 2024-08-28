---
layout: container
name:  "quay.io/biocontainers/microphaser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/microphaser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/microphaser/container.yaml"
updated_at: "2024-08-28 03:01:47.068802"
latest: "0.8.0--hdc3fcad_2"
container_url: "https://biocontainers.pro/tools/microphaser"
aliases:
 - "microphaser"
versions:
 - "0.7.0--h33b3098_1"
 - "0.8.0--h33b3098_0"
 - "0.8.0--hdc3fcad_2"
description: "shpc-registry automated BioContainers addition for microphaser"
config: {"url": "https://biocontainers.pro/tools/microphaser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for microphaser", "latest": {"0.8.0--hdc3fcad_2": "sha256:f32bdddbe1ccedac81990eb3a0c730ab102905807ae66a0fc25d6fb6c888edf1"}, "tags": {"0.7.0--h33b3098_1": "sha256:f8efebb325c85230d3c71fbf1308af512e2926bb6f2aa45f0c34e5e1b42f6b2a", "0.8.0--h33b3098_0": "sha256:b4274fcad623e4397ec2d237f5fb3a5b437fdccf3f99a987ad22a56acfecd394", "0.8.0--hdc3fcad_2": "sha256:f32bdddbe1ccedac81990eb3a0c730ab102905807ae66a0fc25d6fb6c888edf1"}, "docker": "quay.io/biocontainers/microphaser", "aliases": {"microphaser": "/usr/local/bin/microphaser"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/microphaser.
shpc-registry automated BioContainers addition for microphaser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/microphaser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/microphaser:0.8.0--hdc3fcad_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/microphaser/0.8.0--hdc3fcad_2
$ module help quay.io/biocontainers/microphaser/0.8.0--hdc3fcad_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### microphaser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### microphaser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### microphaser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### microphaser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### microphaser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### microphaser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### microphaser

```bash
$ singularity exec <container> /usr/local/bin/microphaser
$ podman run --it --rm --entrypoint /usr/local/bin/microphaser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/microphaser   -v ${PWD} -w ${PWD} <container> -c " $@"
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