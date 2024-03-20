---
layout: container
name:  "quay.io/biocontainers/bioconductor-pharmacogx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pharmacogx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pharmacogx/container.yaml"
updated_at: "2024-03-20 02:47:41.473242"
latest: "3.6.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pharmacogx"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "3.2.0--r42hc247a5b_0"
 - "3.2.0--r42hf17093f_1"
 - "3.4.0--r43hf17093f_0"
 - "3.6.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pharmacogx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pharmacogx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pharmacogx", "latest": {"3.6.0--r43hf17093f_0": "sha256:cd7e24f242e4cbe33ddfc387d2b5d5841c5498b7c8cf5709221b03c7347345ea"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:fde02b3ffff740a521e36be2aa59e97f608bbaf071e1cc2fa757546d3ea57fe2", "3.2.0--r42hc247a5b_0": "sha256:1b7f00f89ed1aff6c74a06a3f6879e93f9ad739474a54264805db8c25cce61dc", "3.2.0--r42hf17093f_1": "sha256:7147f61a0bf7db0c3b097b37fa61f1ea2364558abb750ec49a696eef0fe0b1a0", "3.4.0--r43hf17093f_0": "sha256:5b9d3a8d211fb34379c9fa4fb8e9504f1e33a1fd3b4647e0545361282860c1fc", "3.6.0--r43hf17093f_0": "sha256:cd7e24f242e4cbe33ddfc387d2b5d5841c5498b7c8cf5709221b03c7347345ea"}, "docker": "quay.io/biocontainers/bioconductor-pharmacogx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pharmacogx.
shpc-registry automated BioContainers addition for bioconductor-pharmacogx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pharmacogx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pharmacogx:3.6.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pharmacogx/3.6.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-pharmacogx/3.6.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pharmacogx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pharmacogx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pharmacogx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pharmacogx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pharmacogx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pharmacogx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pharmacogx

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