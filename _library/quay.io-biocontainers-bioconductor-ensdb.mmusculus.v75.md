---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75/container.yaml"
updated_at: "2023-03-29 00:49:05.582166"
latest: "2.99.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.mmusculus.v75"

versions:
 - "2.99.0--r41hdfd78af_9"
 - "2.99.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v75"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.mmusculus.v75", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v75", "latest": {"2.99.0--r42hdfd78af_10": "sha256:4eaccdeeafcc2782ff4ddc5a097ad6250b9f6a9e1d4e2ce5aa8123a44debb2b5"}, "tags": {"2.99.0--r41hdfd78af_9": "sha256:3ddd9af7758e998427700830c3c879b6f5db03804cf004c6b88ebd1a1600e414", "2.99.0--r42hdfd78af_10": "sha256:4eaccdeeafcc2782ff4ddc5a097ad6250b9f6a9e1d4e2ce5aa8123a44debb2b5"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75.
shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v75
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75:2.99.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75/2.99.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-ensdb.mmusculus.v75/2.99.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.mmusculus.v75-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.mmusculus.v75-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.mmusculus.v75-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.mmusculus.v75-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.mmusculus.v75-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.mmusculus.v75-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensdb.mmusculus.v75

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