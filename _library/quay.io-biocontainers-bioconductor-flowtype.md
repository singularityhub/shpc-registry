---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowtype"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowtype/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowtype/container.yaml"
updated_at: "2023-06-06 03:14:58.021715"
latest: "2.25.0--r40h5f743cb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowtype"

versions:
 - "2.25.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowtype"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowtype", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowtype", "latest": {"2.25.0--r40h5f743cb_0": "sha256:520dc183d1b669f27041b5fbc91dd86a5ab6c23f2b47a0edf671b4316a543f76"}, "tags": {"2.25.0--r40h5f743cb_0": "sha256:520dc183d1b669f27041b5fbc91dd86a5ab6c23f2b47a0edf671b4316a543f76"}, "docker": "quay.io/biocontainers/bioconductor-flowtype"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowtype.
shpc-registry automated BioContainers addition for bioconductor-flowtype
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtype
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtype:2.25.0--r40h5f743cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowtype/2.25.0--r40h5f743cb_0
$ module help quay.io/biocontainers/bioconductor-flowtype/2.25.0--r40h5f743cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowtype-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtype-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtype-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowtype-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowtype-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowtype-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowtype

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