---
layout: container
name:  "quay.io/biocontainers/ideas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ideas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ideas/container.yaml"
updated_at: "2023-05-11 02:51:42.164559"
latest: "1.20--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/ideas"
aliases:
 - "ideas"
 - "prepMat"
versions:
 - "1.20--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for ideas"
config: {"url": "https://biocontainers.pro/tools/ideas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ideas", "latest": {"1.20--h9f5acd7_4": "sha256:0d28666a469afe3c471c642cd4d6768de4bda0f7a754af5e0a7bfdcb3bbc8ba5"}, "tags": {"1.20--h9f5acd7_4": "sha256:0d28666a469afe3c471c642cd4d6768de4bda0f7a754af5e0a7bfdcb3bbc8ba5"}, "docker": "quay.io/biocontainers/ideas", "aliases": {"ideas": "/usr/local/bin/ideas", "prepMat": "/usr/local/bin/prepMat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ideas.
shpc-registry automated BioContainers addition for ideas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ideas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ideas:1.20--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ideas/1.20--h9f5acd7_4
$ module help quay.io/biocontainers/ideas/1.20--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ideas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ideas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ideas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ideas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ideas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ideas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ideas

```bash
$ singularity exec <container> /usr/local/bin/ideas
$ podman run --it --rm --entrypoint /usr/local/bin/ideas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ideas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepMat

```bash
$ singularity exec <container> /usr/local/bin/prepMat
$ podman run --it --rm --entrypoint /usr/local/bin/prepMat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepMat   -v ${PWD} -w ${PWD} <container> -c " $@"
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