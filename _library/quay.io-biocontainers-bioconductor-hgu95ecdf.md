---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95ecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95ecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95ecdf/container.yaml"
updated_at: "2026-01-26 04:33:02.599528"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95ecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95ecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95ecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95ecdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:937b405327f88ce04ba948550770900dd439a710270c6ad9625e2d3fcf86ae77"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5cb4bacfeed5c292b320a633d0cd3674ab3c525ef569e057ae7d0c699cbe9eab", "2.18.0--r42hdfd78af_10": "sha256:d2f0d7915affb2fa22049eaeab7313de19c51416c0db5fc9c451ca8a40c7d3e1", "2.18.0--r43hdfd78af_11": "sha256:6422b71d5db7521c384c2d5ae4d53970e5483abe8fe5b48390dbdfd742eb2bab", "2.18.0--r43hdfd78af_12": "sha256:7efa1c858c941b9b3379ac4dbf0b420e6f5f522b8b82a41d31d3c37df8a2ff6e", "2.18.0--r44hdfd78af_13": "sha256:937b405327f88ce04ba948550770900dd439a710270c6ad9625e2d3fcf86ae77"}, "docker": "quay.io/biocontainers/bioconductor-hgu95ecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95ecdf.
shpc-registry automated BioContainers addition for bioconductor-hgu95ecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95ecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95ecdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95ecdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu95ecdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95ecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95ecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95ecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95ecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95ecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95ecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95ecdf

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