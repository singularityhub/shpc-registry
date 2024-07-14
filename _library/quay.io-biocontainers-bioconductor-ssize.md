---
layout: container
name:  "quay.io/biocontainers/bioconductor-ssize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ssize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ssize/container.yaml"
updated_at: "2024-07-14 03:24:41.644134"
latest: "1.76.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-ssize"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.76.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-ssize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ssize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ssize", "latest": {"1.76.0--r43hdfd78af_1": "sha256:44597e3221661c584e7a9a206483a0be426bf254877a17520f0f46f54aeba53a"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:2a2188e16ff66d1af410cd4fa03bb81728b802d19665649487b4f5ccedbdb07a", "1.72.0--r42hdfd78af_0": "sha256:df8e4f84ab3381a1197dc2bd37f62c2c97859496a0d2f04edc91b094de0a904a", "1.74.0--r43hdfd78af_0": "sha256:e36fbec4a78c070b8d1bac978aca67be323b4ea8330408b01fddd17616bd4130", "1.76.0--r43hdfd78af_1": "sha256:44597e3221661c584e7a9a206483a0be426bf254877a17520f0f46f54aeba53a"}, "docker": "quay.io/biocontainers/bioconductor-ssize"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ssize.
shpc-registry automated BioContainers addition for bioconductor-ssize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ssize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ssize:1.76.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ssize/1.76.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-ssize/1.76.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ssize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ssize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ssize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ssize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ssize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ssize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ssize

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