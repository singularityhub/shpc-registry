---
layout: container
name:  "quay.io/biocontainers/proda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proda/container.yaml"
updated_at: "2023-07-24 02:53:56.723820"
latest: "1.0--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/proda"
aliases:
 - "proda"
versions:
 - "1.0--h87f3376_3"
 - "1.0--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for proda"
config: {"url": "https://biocontainers.pro/tools/proda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proda", "latest": {"1.0--hdbdd923_5": "sha256:bad866f9cd7786eaffe8e3b0b47cc3daa5a77c5280378f7bb45cccbf37556d18"}, "tags": {"1.0--h87f3376_3": "sha256:b4788dd0b42ed61d31a252d006ceaafa5c37c3f987ff4d2f552cfd633cad6677", "1.0--hdbdd923_5": "sha256:bad866f9cd7786eaffe8e3b0b47cc3daa5a77c5280378f7bb45cccbf37556d18"}, "docker": "quay.io/biocontainers/proda", "aliases": {"proda": "/usr/local/bin/proda"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proda.
shpc-registry automated BioContainers addition for proda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proda:1.0--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proda/1.0--hdbdd923_5
$ module help quay.io/biocontainers/proda/1.0--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proda

```bash
$ singularity exec <container> /usr/local/bin/proda
$ podman run --it --rm --entrypoint /usr/local/bin/proda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proda   -v ${PWD} -w ${PWD} <container> -c " $@"
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