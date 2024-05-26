---
layout: container
name:  "quay.io/biocontainers/bioconductor-rmir.hsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rmir.hsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rmir.hsa/container.yaml"
updated_at: "2024-05-26 02:59:49.423346"
latest: "1.0.5--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rmir.hsa"

versions:
 - "1.0.5--r41hdfd78af_9"
 - "1.0.5--r42hdfd78af_10"
 - "1.0.5--r43hdfd78af_11"
 - "1.0.5--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rmir.hsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rmir.hsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rmir.hsa", "latest": {"1.0.5--r43hdfd78af_12": "sha256:e55ab823f5c9c47f5b4ad5ad75074d255c725d639ff5ed939a9eb75cf573a9fe"}, "tags": {"1.0.5--r41hdfd78af_9": "sha256:7a9263ae65f2cd638d4b7b007fe73589f9dd285921f321ec87da2261ae387a1a", "1.0.5--r42hdfd78af_10": "sha256:6ddc6152d350d7f4109718fb47e1f954b24c15db8de5bb10999f9459fc1a5a3d", "1.0.5--r43hdfd78af_11": "sha256:76cfcc607f8600f4307733ff5dcb90f9ae670f4f50056e30809cb9e4851fc36b", "1.0.5--r43hdfd78af_12": "sha256:e55ab823f5c9c47f5b4ad5ad75074d255c725d639ff5ed939a9eb75cf573a9fe"}, "docker": "quay.io/biocontainers/bioconductor-rmir.hsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rmir.hsa.
shpc-registry automated BioContainers addition for bioconductor-rmir.hsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rmir.hsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rmir.hsa:1.0.5--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rmir.hsa/1.0.5--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rmir.hsa/1.0.5--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rmir.hsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmir.hsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rmir.hsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rmir.hsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rmir.hsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rmir.hsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rmir.hsa

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