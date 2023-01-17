---
layout: container
name:  "quay.io/biocontainers/bioconductor-cageminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cageminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cageminer/container.yaml"
updated_at: "2023-01-17 02:58:08.033764"
latest: "1.4.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cageminer"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cageminer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cageminer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cageminer", "latest": {"1.4.0--r42hdfd78af_0": "sha256:d1c857dfd0badba6297b43dedbdae71e24a645cfb5b92aca5ed23404098a88fc"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:f9597950523f7c8c6b5b0e81f5c43f10abfd9e61b8205d6c3be7a76d0f7c03e7", "1.4.0--r42hdfd78af_0": "sha256:d1c857dfd0badba6297b43dedbdae71e24a645cfb5b92aca5ed23404098a88fc"}, "docker": "quay.io/biocontainers/bioconductor-cageminer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cageminer.
shpc-registry automated BioContainers addition for bioconductor-cageminer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cageminer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cageminer:1.4.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cageminer/1.4.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cageminer/1.4.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cageminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cageminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cageminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cageminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cageminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cageminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cageminer

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