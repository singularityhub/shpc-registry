---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosophila2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosophila2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosophila2cdf/container.yaml"
updated_at: "2025-03-12 03:40:52.836977"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-drosophila2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-drosophila2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosophila2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosophila2cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:0e06bed9ba892c1f90504137924ee08fcb7f10b0406bc6d37d326f5df9a9d28e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:11452b0f23ea09fcb3534a72f9ddad646d0281a6c2c8030fe82a1c2ea92d4014", "2.18.0--r42hdfd78af_10": "sha256:ae7a6cf490a433bf42385f02d813c857e28aedb8ebc36765b260e998973e6d28", "2.18.0--r43hdfd78af_11": "sha256:4efd3a164977b1df505f8a314ef5c21d13c5784815d8f24a7a99749b6d96f28c", "2.18.0--r43hdfd78af_12": "sha256:07a5a869c6a8592abede3edd2fd4f855f28f219927472dd13e4033ef34b08fbb", "2.18.0--r44hdfd78af_13": "sha256:0e06bed9ba892c1f90504137924ee08fcb7f10b0406bc6d37d326f5df9a9d28e"}, "docker": "quay.io/biocontainers/bioconductor-drosophila2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosophila2cdf.
shpc-registry automated BioContainers addition for bioconductor-drosophila2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosophila2cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosophila2cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-drosophila2cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosophila2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosophila2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosophila2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosophila2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosophila2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-drosophila2cdf

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