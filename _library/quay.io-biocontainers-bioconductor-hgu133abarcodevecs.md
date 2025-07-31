---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133abarcodevecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133abarcodevecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133abarcodevecs/container.yaml"
updated_at: "2025-07-31 11:51:10.297831"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133abarcodevecs"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133abarcodevecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133abarcodevecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133abarcodevecs", "latest": {"1.44.0--r44hdfd78af_0": "sha256:ec099db02c5c0b3600c559fcc5f8752de2634645058e87956a41cdecceb35c90"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:14fb5299d23a9925615a261df342468fe24fe6e7f855d8b4a98d66f9a1ac873a", "1.35.0--r42hdfd78af_0": "sha256:bd360ffb2d89c43f0fe82047b4a4c10d6ad7ba1df9edac8e7dd4391dccff5c02", "1.38.0--r43hdfd78af_0": "sha256:244b55ea32c60e30c2295d12361f8f25c50d2a7c70375e066d2e6bab73c58046", "1.40.0--r43hdfd78af_0": "sha256:22278fa350d417307af7f14da4967973014d7ced8d048121e6157854c8488597", "1.44.0--r44hdfd78af_0": "sha256:ec099db02c5c0b3600c559fcc5f8752de2634645058e87956a41cdecceb35c90"}, "docker": "quay.io/biocontainers/bioconductor-hgu133abarcodevecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133abarcodevecs.
shpc-registry automated BioContainers addition for bioconductor-hgu133abarcodevecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133abarcodevecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133abarcodevecs:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133abarcodevecs/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hgu133abarcodevecs/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133abarcodevecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133abarcodevecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133abarcodevecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133abarcodevecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133abarcodevecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133abarcodevecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133abarcodevecs

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