---
layout: container
name:  "quay.io/biocontainers/bioconductor-ggcyto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ggcyto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ggcyto/container.yaml"
updated_at: "2024-02-21 02:45:17.542782"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ggcyto"

versions:
 - "1.8.2--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ggcyto"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ggcyto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ggcyto", "latest": {"1.30.0--r43hdfd78af_0": "sha256:7182467ecdde8c02879f21072c02023c596261fbfa064a8bfc7c799bb97755c0"}, "tags": {"1.8.2--r351_0": "sha256:eeb19f86d21dfddf29982993f3346c89883a325e5e5c923a29c75230ecbfe64b", "1.26.0--r42hdfd78af_0": "sha256:d0066f66e8f0005338c55876ee14456c3bbdc7916e1ef787cf71830932ec6165", "1.22.0--r41hdfd78af_0": "sha256:65f987da1fc57a70364d6e4a4ad2299012d07a91f47252722a340ac408a1daac", "1.20.0--r41hdfd78af_0": "sha256:357e45b7fc73e9230482b61ebcd131d30ed407cfbe1e130bcc16af00f3d2d926", "1.18.0--r40hdfd78af_1": "sha256:06ab331fe0308c9c012cacd896e5541446e3072c324406f7e83e0957a9b17673", "1.16.0--r40_0": "sha256:224ec8d998637f72f63de9b4ab60b1f8bcad340153f70a02cb8331be3cb470ad", "1.28.0--r43hdfd78af_0": "sha256:bade921444d11fed2ca0b2a242c19515b385daec297c6f7726450d9b3752935c", "1.30.0--r43hdfd78af_0": "sha256:7182467ecdde8c02879f21072c02023c596261fbfa064a8bfc7c799bb97755c0"}, "docker": "quay.io/biocontainers/bioconductor-ggcyto"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ggcyto.
shpc-registry automated BioContainers addition for bioconductor-ggcyto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ggcyto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ggcyto:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ggcyto/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ggcyto/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ggcyto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggcyto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggcyto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ggcyto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ggcyto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ggcyto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ggcyto

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