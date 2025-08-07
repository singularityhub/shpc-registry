---
layout: container
name:  "quay.io/biocontainers/bioconductor-topgo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-topgo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-topgo/container.yaml"
updated_at: "2025-08-07 09:57:52.273347"
latest: "2.58.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-topgo"

versions:
 - "2.46.0--r41hdfd78af_0"
 - "2.50.0--r42hdfd78af_0"
 - "2.52.0--r43hdfd78af_0"
 - "2.54.0--r43hdfd78af_0"
 - "2.58.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-topgo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-topgo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-topgo", "latest": {"2.58.0--r44hdfd78af_0": "sha256:c91968b2f290ff7f0c0d2435afe5665b21764679a7e1bda98a2ff5d3d8bdbdc2"}, "tags": {"2.46.0--r41hdfd78af_0": "sha256:1c706236f1c80add883366c6ec0892170db69fc5c3287f90263e3907307aeefa", "2.50.0--r42hdfd78af_0": "sha256:73f89cbd6ac93317a6d7b097903843ea0fae654d22a75f3a1ba69c2075bac694", "2.52.0--r43hdfd78af_0": "sha256:b6990cf8e140832b0017bcb05f48dc17b48ff06f1f006a5cdbf7dcd3614352e6", "2.54.0--r43hdfd78af_0": "sha256:72fca61fa4888b4e71d254e50274a8bd0dae2bce026a450ace5d897d5876f530", "2.58.0--r44hdfd78af_0": "sha256:c91968b2f290ff7f0c0d2435afe5665b21764679a7e1bda98a2ff5d3d8bdbdc2"}, "docker": "quay.io/biocontainers/bioconductor-topgo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-topgo.
shpc-registry automated BioContainers addition for bioconductor-topgo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-topgo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-topgo:2.58.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-topgo/2.58.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-topgo/2.58.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-topgo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-topgo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-topgo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-topgo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-topgo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-topgo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-topgo

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