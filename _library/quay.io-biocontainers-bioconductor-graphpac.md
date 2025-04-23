---
layout: container
name:  "quay.io/biocontainers/bioconductor-graphpac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graphpac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graphpac/container.yaml"
updated_at: "2025-04-23 03:48:58.997758"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-graphpac"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-graphpac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graphpac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graphpac", "latest": {"1.44.0--r43hdfd78af_0": "sha256:57e28da8efc61a274697cfb47a9e9df99bfe7fae3b86bcb9c55b7c57b3d2f4c9"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:3a2ba3fc9dfd1444d07a6fa5e9d1d5b83e4708ff39cc1b792683f7c8671aa98f", "1.40.0--r42hdfd78af_0": "sha256:f8e532076d26f19126f1f7411cd491398ee1c749409701a36aa4a8bd0f6b91b3", "1.42.0--r43hdfd78af_0": "sha256:66b559941aa336ae7db877667f90af5f6cf4f9dee8b704b9d50065b887c4257b", "1.44.0--r43hdfd78af_0": "sha256:57e28da8efc61a274697cfb47a9e9df99bfe7fae3b86bcb9c55b7c57b3d2f4c9"}, "docker": "quay.io/biocontainers/bioconductor-graphpac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graphpac.
shpc-registry automated BioContainers addition for bioconductor-graphpac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graphpac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graphpac:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graphpac/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-graphpac/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graphpac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphpac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphpac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graphpac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graphpac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graphpac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-graphpac

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