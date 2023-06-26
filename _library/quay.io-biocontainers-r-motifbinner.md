---
layout: container
name:  "quay.io/biocontainers/r-motifbinner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-motifbinner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-motifbinner/container.yaml"
updated_at: "2023-06-26 03:32:21.196481"
latest: "2.0.0--r42hdbdd923_6"
container_url: "https://biocontainers.pro/tools/r-motifbinner"
aliases:
 - "pandoc"
versions:
 - "2.0.0--r41h87f3376_4"
 - "2.0.0--r42h87f3376_5"
 - "2.0.0--r42hdbdd923_6"
description: "shpc-registry automated BioContainers addition for r-motifbinner"
config: {"url": "https://biocontainers.pro/tools/r-motifbinner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-motifbinner", "latest": {"2.0.0--r42hdbdd923_6": "sha256:cf8b1a0c98dc8dd390d05b342e660ec8092b2c039834662ccf8e01d51b013ae1"}, "tags": {"2.0.0--r41h87f3376_4": "sha256:39e936c5c61df4bdd277a6170ab303e07f9ad602a5c6d2c13ac7572b186db362", "2.0.0--r42h87f3376_5": "sha256:6588d623e3d13f12d0d9a9f3c32c2f7b13f9a36e63e73e6a73e6b05c7dd6f216", "2.0.0--r42hdbdd923_6": "sha256:cf8b1a0c98dc8dd390d05b342e660ec8092b2c039834662ccf8e01d51b013ae1"}, "docker": "quay.io/biocontainers/r-motifbinner", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-motifbinner.
shpc-registry automated BioContainers addition for r-motifbinner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-motifbinner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-motifbinner:2.0.0--r42hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-motifbinner/2.0.0--r42hdbdd923_6
$ module help quay.io/biocontainers/r-motifbinner/2.0.0--r42hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-motifbinner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-motifbinner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-motifbinner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-motifbinner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-motifbinner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-motifbinner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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