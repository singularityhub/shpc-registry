---
layout: container
name:  "quay.io/biocontainers/bioconductor-spacepac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spacepac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spacepac/container.yaml"
updated_at: "2025-10-07 03:11:37.783074"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spacepac"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spacepac"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spacepac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spacepac", "latest": {"1.40.0--r43hdfd78af_0": "sha256:0c2858ffd481a8f98eb5ce883cf707549b7607c6a13d7988859dbb29baae89ea"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:78fec7f5e3c6f18f2dc6c8a30e253e50e0b1c798e04f8aab79022098f4679d7e", "1.36.0--r42hdfd78af_0": "sha256:27d8896b967474b93be0260ef50028d468a9b6fb6df1e9b932dfc93b8537cc72", "1.38.0--r43hdfd78af_0": "sha256:3ac6b2a1d5ae4b9006acd62f70c45fccb36fef2c065f5085aae2ccc147a1b563", "1.40.0--r43hdfd78af_0": "sha256:0c2858ffd481a8f98eb5ce883cf707549b7607c6a13d7988859dbb29baae89ea"}, "docker": "quay.io/biocontainers/bioconductor-spacepac"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spacepac.
shpc-registry automated BioContainers addition for bioconductor-spacepac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spacepac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spacepac:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spacepac/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spacepac/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spacepac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spacepac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spacepac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spacepac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spacepac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spacepac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spacepac

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