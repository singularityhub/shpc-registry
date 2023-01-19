---
layout: container
name:  "quay.io/biocontainers/bioconductor-ptairdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ptairdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ptairdata/container.yaml"
updated_at: "2023-01-19 02:59:54.623063"
latest: "1.5.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ptairdata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.5.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ptairdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ptairdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ptairdata", "latest": {"1.5.0--r42hdfd78af_0": "sha256:e1cce3090b111b674fc46c8588c06a091be072f600d2ccf3fc807b6a72ed7d6e"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:4b42b65d750e09c19f95782e12ae50abe2e624eb1aed5fa03ade9f5abf2eb808", "1.5.0--r42hdfd78af_0": "sha256:e1cce3090b111b674fc46c8588c06a091be072f600d2ccf3fc807b6a72ed7d6e"}, "docker": "quay.io/biocontainers/bioconductor-ptairdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ptairdata.
shpc-registry automated BioContainers addition for bioconductor-ptairdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ptairdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ptairdata:1.5.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ptairdata/1.5.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ptairdata/1.5.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ptairdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ptairdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ptairdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ptairdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ptairdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ptairdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ptairdata

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