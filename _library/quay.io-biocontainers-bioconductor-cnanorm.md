---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnanorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnanorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnanorm/container.yaml"
updated_at: "2023-08-12 02:50:50.433928"
latest: "1.46.1--r43h9913872_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnanorm"

versions:
 - "1.40.0--r41hefde4a7_2"
 - "1.44.0--r42hefde4a7_0"
 - "1.44.0--r42h9913872_1"
 - "1.46.1--r43h9913872_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnanorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnanorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnanorm", "latest": {"1.46.1--r43h9913872_0": "sha256:6e9bbdc0db302d1f25923fb30a01da13dc4620640a20062cf8758551e4eb5000"}, "tags": {"1.40.0--r41hefde4a7_2": "sha256:bd38274857fba5b73c47b49db298bfda396f676e285310a6d0eb281f1dcdd84e", "1.44.0--r42hefde4a7_0": "sha256:eab40517346845958da202a5ee78441104c58c1fb74b25c4391400e761a5f2df", "1.44.0--r42h9913872_1": "sha256:7577124d3175a176bf048375b3d7e9d9de4a3687f39e1cd7d64755c2753243e1", "1.46.1--r43h9913872_0": "sha256:6e9bbdc0db302d1f25923fb30a01da13dc4620640a20062cf8758551e4eb5000"}, "docker": "quay.io/biocontainers/bioconductor-cnanorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnanorm.
shpc-registry automated BioContainers addition for bioconductor-cnanorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnanorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnanorm:1.46.1--r43h9913872_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnanorm/1.46.1--r43h9913872_0
$ module help quay.io/biocontainers/bioconductor-cnanorm/1.46.1--r43h9913872_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnanorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnanorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnanorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnanorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnanorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnanorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cnanorm

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