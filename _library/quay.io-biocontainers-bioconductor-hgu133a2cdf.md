---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133a2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133a2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133a2cdf/container.yaml"
updated_at: "2023-10-05 02:42:11.420161"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133a2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133a2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133a2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133a2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:8d04544d90d4828291d114d7735df35d343dae3c985e70f0214edf4d4e60e969"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:36ddd35ffc5bd22718b00ac2625c39911fb993619ba37ebf43ab4ac7fd5f5aef", "2.18.0--r41hdfd78af_10": "sha256:adce5c2ea57834d9e314f64da48d4cb751964cc5d6e4f6c6ff8d6d5517ab85a5", "2.18.0--r42hdfd78af_11": "sha256:ce6fbdfa8ba531ecd91ce97e8ede3f982e1999e727cea0b78843b946ec8ac397", "2.18.0--r43hdfd78af_12": "sha256:8d04544d90d4828291d114d7735df35d343dae3c985e70f0214edf4d4e60e969"}, "docker": "quay.io/biocontainers/bioconductor-hgu133a2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133a2cdf.
shpc-registry automated BioContainers addition for bioconductor-hgu133a2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133a2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133a2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu133a2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133a2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133a2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133a2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133a2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133a2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133a2cdf

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