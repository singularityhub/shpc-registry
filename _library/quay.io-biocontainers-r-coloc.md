---
layout: container
name:  "quay.io/biocontainers/r-coloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-coloc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-coloc/container.yaml"
updated_at: "2024-04-27 02:45:37.674211"
latest: "5.1.0.1--r42h3121a25_1"
container_url: "https://biocontainers.pro/tools/r-coloc"

versions:
 - "5.1.0.1--r41h3121a25_0"
 - "5.1.0.1--r42h3121a25_1"
description: "shpc-registry automated BioContainers addition for r-coloc"
config: {"url": "https://biocontainers.pro/tools/r-coloc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-coloc", "latest": {"5.1.0.1--r42h3121a25_1": "sha256:4ed42bea4160cec7d17e70de36aac06c969182312a7e7b6bcd69dbd43d051388"}, "tags": {"5.1.0.1--r41h3121a25_0": "sha256:b918debc1782cd40458208db7e6d7a86d3ed720c8f90c6feb44590abd76db137", "5.1.0.1--r42h3121a25_1": "sha256:4ed42bea4160cec7d17e70de36aac06c969182312a7e7b6bcd69dbd43d051388"}, "docker": "quay.io/biocontainers/r-coloc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-coloc.
shpc-registry automated BioContainers addition for r-coloc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-coloc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-coloc:5.1.0.1--r42h3121a25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-coloc/5.1.0.1--r42h3121a25_1
$ module help quay.io/biocontainers/r-coloc/5.1.0.1--r42h3121a25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-coloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-coloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-coloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-coloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-coloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-coloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-coloc

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