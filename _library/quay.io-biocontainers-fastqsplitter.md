---
layout: container
name:  "quay.io/biocontainers/fastqsplitter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastqsplitter/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fastqsplitter/container.yaml"
updated_at: "2022-10-27 00:33:03.710360"
latest: "1.2.0--py38hbff2b2d_3"
container_url: "https://biocontainers.pro/tools/fastqsplitter"
aliases:
 - "fastqsplitter"
versions:
 - "1.2.0--py38hbff2b2d_3"
description: "shpc-registry automated BioContainers addition for fastqsplitter"
config: {"url": "https://biocontainers.pro/tools/fastqsplitter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastqsplitter", "latest": {"1.2.0--py38hbff2b2d_3": "sha256:9bd62e637a0a1f968653282b334a4fba2879fced60855cee971dcfd4ed7fc39a"}, "tags": {"1.2.0--py38hbff2b2d_3": "sha256:9bd62e637a0a1f968653282b334a4fba2879fced60855cee971dcfd4ed7fc39a"}, "docker": "quay.io/biocontainers/fastqsplitter", "aliases": {"fastqsplitter": "/usr/local/bin/fastqsplitter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastqsplitter.
shpc-registry automated BioContainers addition for fastqsplitter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastqsplitter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastqsplitter:1.2.0--py38hbff2b2d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastqsplitter/1.2.0--py38hbff2b2d_3
$ module help quay.io/biocontainers/fastqsplitter/1.2.0--py38hbff2b2d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastqsplitter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastqsplitter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastqsplitter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastqsplitter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastqsplitter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastqsplitter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastqsplitter

```bash
$ singularity exec <container> /usr/local/bin/fastqsplitter
$ podman run --it --rm --entrypoint /usr/local/bin/fastqsplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqsplitter   -v ${PWD} -w ${PWD} <container> -c " $@"
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