---
layout: container
name:  "quay.io/biocontainers/bioconductor-ricecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ricecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ricecdf/container.yaml"
updated_at: "2023-04-16 03:13:04.468227"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-ricecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-ricecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ricecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ricecdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:43b1d6968b8e7b608d06359b81b9efd617b9b04add165f84c8a1d19f7ee1d548"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:76e10389f9fd63d4f9000f70333800dcd67d374042b6b5df2a4d89ab3876288e", "2.18.0--r42hdfd78af_10": "sha256:43b1d6968b8e7b608d06359b81b9efd617b9b04add165f84c8a1d19f7ee1d548"}, "docker": "quay.io/biocontainers/bioconductor-ricecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ricecdf.
shpc-registry automated BioContainers addition for bioconductor-ricecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ricecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ricecdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ricecdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-ricecdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ricecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ricecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ricecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ricecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ricecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ricecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ricecdf

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