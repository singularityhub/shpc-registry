---
layout: container
name:  "quay.io/biocontainers/bioconductor-debrowser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-debrowser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-debrowser/container.yaml"
updated_at: "2023-07-06 03:13:00.053300"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-debrowser"

versions:
 - "1.22.1--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-debrowser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-debrowser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-debrowser", "latest": {"1.26.0--r42hdfd78af_0": "sha256:44d0daac641eab9fa8f2b5a29866ccc6481108ab5f3d8906ed20d027d6c8700f"}, "tags": {"1.22.1--r41hdfd78af_0": "sha256:c9c185ca8280f2c6ec3b2597614942d0b07a3261d4052c75d8b97017f2f5dede", "1.26.0--r42hdfd78af_0": "sha256:44d0daac641eab9fa8f2b5a29866ccc6481108ab5f3d8906ed20d027d6c8700f"}, "docker": "quay.io/biocontainers/bioconductor-debrowser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-debrowser.
shpc-registry automated BioContainers addition for bioconductor-debrowser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-debrowser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-debrowser:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-debrowser/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-debrowser/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-debrowser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-debrowser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-debrowser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-debrowser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-debrowser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-debrowser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-debrowser

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