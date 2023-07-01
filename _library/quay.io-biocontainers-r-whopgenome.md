---
layout: container
name:  "quay.io/biocontainers/r-whopgenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-whopgenome/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-whopgenome/container.yaml"
updated_at: "2023-07-01 03:40:38.764198"
latest: "0.9.7--r42h21a89ab_8"
container_url: "https://biocontainers.pro/tools/r-whopgenome"

versions:
 - "0.9.7--r41hecf12ef_6"
 - "0.9.7--r42hecf12ef_7"
 - "0.9.7--r42h21a89ab_8"
description: "shpc-registry automated BioContainers addition for r-whopgenome"
config: {"url": "https://biocontainers.pro/tools/r-whopgenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-whopgenome", "latest": {"0.9.7--r42h21a89ab_8": "sha256:71f763694008a02289f03032037de57f8cd1b1bb6e6f24741bdeef1992c79f34"}, "tags": {"0.9.7--r41hecf12ef_6": "sha256:4cd432591ab478c4b526e4b7e92e06ef32339ca1c11fc0211a792553f109af09", "0.9.7--r42hecf12ef_7": "sha256:8e1dfe2a78dbfbe1b4383706f50f1bc1813c91fbde4ca5889926daf3b2d5eb2b", "0.9.7--r42h21a89ab_8": "sha256:71f763694008a02289f03032037de57f8cd1b1bb6e6f24741bdeef1992c79f34"}, "docker": "quay.io/biocontainers/r-whopgenome"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-whopgenome.
shpc-registry automated BioContainers addition for r-whopgenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-whopgenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-whopgenome:0.9.7--r42h21a89ab_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-whopgenome/0.9.7--r42h21a89ab_8
$ module help quay.io/biocontainers/r-whopgenome/0.9.7--r42h21a89ab_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-whopgenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-whopgenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-whopgenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-whopgenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-whopgenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-whopgenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-whopgenome

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