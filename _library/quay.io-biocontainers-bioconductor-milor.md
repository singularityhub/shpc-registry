---
layout: container
name:  "quay.io/biocontainers/bioconductor-milor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-milor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-milor/container.yaml"
updated_at: "2023-05-18 03:31:51.482958"
latest: "1.6.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-milor"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-milor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-milor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-milor", "latest": {"1.6.0--r42hdfd78af_0": "sha256:e519f001b7b70cbd0beb8a704f8fe5c52e5ee60fcbedc3df2828b420e894192f"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:70d08972ec1ef8354155354a3047ad441cdb232215da090841a27f37280b62c0", "1.6.0--r42hdfd78af_0": "sha256:e519f001b7b70cbd0beb8a704f8fe5c52e5ee60fcbedc3df2828b420e894192f"}, "docker": "quay.io/biocontainers/bioconductor-milor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-milor.
shpc-registry automated BioContainers addition for bioconductor-milor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-milor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-milor:1.6.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-milor/1.6.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-milor/1.6.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-milor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-milor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-milor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-milor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-milor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-milor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-milor

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