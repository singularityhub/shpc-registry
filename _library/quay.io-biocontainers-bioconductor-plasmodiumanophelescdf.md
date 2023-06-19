---
layout: container
name:  "quay.io/biocontainers/bioconductor-plasmodiumanophelescdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plasmodiumanophelescdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plasmodiumanophelescdf/container.yaml"
updated_at: "2023-06-19 03:09:12.782879"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-plasmodiumanophelescdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelescdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plasmodiumanophelescdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelescdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:1787ace18dd030c9e3fc54c853f82135bfc265c8dc5549bae5ef6611f17453c3"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c541a2a447b82ff72c7f6f4cd50b0dfb6ace7902152a8b19856b54de695e5f81", "2.18.0--r42hdfd78af_10": "sha256:1787ace18dd030c9e3fc54c853f82135bfc265c8dc5549bae5ef6611f17453c3"}, "docker": "quay.io/biocontainers/bioconductor-plasmodiumanophelescdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plasmodiumanophelescdf.
shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelescdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plasmodiumanophelescdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plasmodiumanophelescdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plasmodiumanophelescdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-plasmodiumanophelescdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plasmodiumanophelescdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plasmodiumanophelescdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plasmodiumanophelescdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plasmodiumanophelescdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plasmodiumanophelescdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plasmodiumanophelescdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plasmodiumanophelescdf

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