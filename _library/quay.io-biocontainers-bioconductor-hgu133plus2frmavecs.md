---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133plus2frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133plus2frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133plus2frmavecs/container.yaml"
updated_at: "2025-02-25 03:42:12.007284"
latest: "1.5.0--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133plus2frmavecs"

versions:
 - "1.5.0--r41hdfd78af_9"
 - "1.5.0--r42hdfd78af_11"
 - "1.5.0--r43hdfd78af_12"
 - "1.5.0--r43hdfd78af_13"
 - "1.5.0--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133plus2frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133plus2frmavecs", "latest": {"1.5.0--r44hdfd78af_14": "sha256:3ed1ee1f472ab4e81752fa02355ccb2ac9b31d60d34adc8b06ddf5860b7ff481"}, "tags": {"1.5.0--r41hdfd78af_9": "sha256:ed4a30c8389a477e735a1d3614f4a5de2479f1466179210d98a26f2371782ced", "1.5.0--r42hdfd78af_11": "sha256:bf0f4e58c118bad5a3964cb799dc2771486d406cb34ff000990f406c53dfcd9e", "1.5.0--r43hdfd78af_12": "sha256:8a657da21d39cc5c079f029b62b09ec07548ad899b67650dcb9b43dd711183ba", "1.5.0--r43hdfd78af_13": "sha256:7d6cffc88f55a6ce88cf6b57ee61d07ca67f9c6e178ddb2f19ee705d06a2766e", "1.5.0--r44hdfd78af_14": "sha256:3ed1ee1f472ab4e81752fa02355ccb2ac9b31d60d34adc8b06ddf5860b7ff481"}, "docker": "quay.io/biocontainers/bioconductor-hgu133plus2frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133plus2frmavecs.
shpc-registry automated BioContainers addition for bioconductor-hgu133plus2frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133plus2frmavecs:1.5.0--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133plus2frmavecs/1.5.0--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-hgu133plus2frmavecs/1.5.0--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133plus2frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133plus2frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133plus2frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133plus2frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133plus2frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133plus2frmavecs

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