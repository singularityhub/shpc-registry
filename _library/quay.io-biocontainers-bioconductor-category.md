---
layout: container
name:  "quay.io/biocontainers/bioconductor-category"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-category/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-category/container.yaml"
updated_at: "2023-07-10 03:23:28.087601"
latest: "2.64.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-category"

versions:
 - "2.60.0--r41hdfd78af_0"
 - "2.64.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-category"
config: {"url": "https://biocontainers.pro/tools/bioconductor-category", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-category", "latest": {"2.64.0--r42hdfd78af_0": "sha256:b983d6ed36faf0ceb33c0a80055fdd0f65e4a58bfdbc90ddb7711c05fff5daa1"}, "tags": {"2.60.0--r41hdfd78af_0": "sha256:888894204cc6d0660386c8e20c5bb0321556c98197b3a5c342a089995314a657", "2.64.0--r42hdfd78af_0": "sha256:b983d6ed36faf0ceb33c0a80055fdd0f65e4a58bfdbc90ddb7711c05fff5daa1"}, "docker": "quay.io/biocontainers/bioconductor-category"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-category.
shpc-registry automated BioContainers addition for bioconductor-category
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-category
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-category:2.64.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-category/2.64.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-category/2.64.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-category-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-category-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-category-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-category-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-category-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-category-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-category

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