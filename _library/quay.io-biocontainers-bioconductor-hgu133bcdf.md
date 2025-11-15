---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133bcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133bcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133bcdf/container.yaml"
updated_at: "2025-11-15 03:38:21.991473"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133bcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133bcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133bcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133bcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:f954ae2e265b7fc116183df25747184f6ae6da9cb051ddd77ab9eeb9715f5757"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:7e033743b50d41dc4f7208646767d6ee2c69c38bb82c8f0068624385a6bef16c", "2.18.0--r42hdfd78af_10": "sha256:a08c747f2d16c0dda704d6073d10944c7f5817ccf794c8e6969ae70698609b3e", "2.18.0--r43hdfd78af_11": "sha256:780b45893f52864fd3c296196cb54f35ba51abae2aa4d4d78f1a9aa95b8a0388", "2.18.0--r43hdfd78af_12": "sha256:6a222bbfe2648591a650c5339c7d6ceb6a044e0cf2d63d65a64e932c5fcbccb6", "2.18.0--r44hdfd78af_13": "sha256:f954ae2e265b7fc116183df25747184f6ae6da9cb051ddd77ab9eeb9715f5757"}, "docker": "quay.io/biocontainers/bioconductor-hgu133bcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133bcdf.
shpc-registry automated BioContainers addition for bioconductor-hgu133bcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133bcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133bcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133bcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu133bcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133bcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133bcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133bcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133bcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133bcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133bcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133bcdf

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