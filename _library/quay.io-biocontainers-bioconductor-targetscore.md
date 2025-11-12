---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetscore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetscore/container.yaml"
updated_at: "2025-11-12 03:19:09.298587"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-targetscore"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-targetscore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetscore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetscore", "latest": {"1.44.0--r44hdfd78af_0": "sha256:a9f8651baeb23a47067917a668c73c6b30774f8c17aa809cdc309ab2b19ac082"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:43526defda0d2c24f2d3ea9768db8aa2a7b41a41572da96ec7d06b1f26f42f7d", "1.36.0--r42hdfd78af_0": "sha256:242e291f3868f723729252010c97e41dbd5b0245cf50c733822e1c4fbbc27ee4", "1.38.0--r43hdfd78af_0": "sha256:97b1f6fe9dc0b2febcd62d9220edc4c7a74ae666a99f0cf8cf948c478e192a39", "1.40.0--r43hdfd78af_0": "sha256:c8f2ac838f58ac0c24a3395bce5378bf44611c16939e16768008f7f1a291fb56", "1.44.0--r44hdfd78af_0": "sha256:a9f8651baeb23a47067917a668c73c6b30774f8c17aa809cdc309ab2b19ac082"}, "docker": "quay.io/biocontainers/bioconductor-targetscore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetscore.
shpc-registry automated BioContainers addition for bioconductor-targetscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetscore:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetscore/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-targetscore/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-targetscore

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