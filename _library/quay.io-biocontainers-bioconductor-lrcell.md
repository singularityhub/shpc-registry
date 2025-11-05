---
layout: container
name:  "quay.io/biocontainers/bioconductor-lrcell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lrcell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lrcell/container.yaml"
updated_at: "2025-11-05 03:24:59.348809"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lrcell"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lrcell"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lrcell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lrcell", "latest": {"1.14.0--r44hdfd78af_0": "sha256:f0534ec5579da18605ad20d6253e39b590691ac0c8528912203f2d6c35c1f7bb"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a3319f51993669b37a887e58b18eb6c93db89b8cd9c727e531916287d8d27c83", "1.6.0--r42hdfd78af_0": "sha256:bc96cc3f942962b66ede8e2aae87339cf31b464627f2a90cd48426752cb978f1", "1.8.0--r43hdfd78af_0": "sha256:901ee05629d7dbf745370903e4b0f107af407a29af7c80761c1c4724d30541db", "1.10.0--r43hdfd78af_0": "sha256:25ac0a99eb3f678c90ed720892b013611117fa21e323cb0720490d19380efce4", "1.14.0--r44hdfd78af_0": "sha256:f0534ec5579da18605ad20d6253e39b590691ac0c8528912203f2d6c35c1f7bb"}, "docker": "quay.io/biocontainers/bioconductor-lrcell"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lrcell.
shpc-registry automated BioContainers addition for bioconductor-lrcell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lrcell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lrcell:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lrcell/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lrcell/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lrcell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrcell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lrcell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lrcell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lrcell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lrcell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lrcell

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