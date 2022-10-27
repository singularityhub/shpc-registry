---
layout: container
name:  "quay.io/biocontainers/bioconductor-srnadiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-srnadiff/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-srnadiff/container.yaml"
updated_at: "2022-10-27 00:32:27.458512"
latest: "1.8.0--r40h5f743cb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-srnadiff"

versions:
 - "1.8.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-srnadiff"
config: {"url": "https://biocontainers.pro/tools/bioconductor-srnadiff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-srnadiff", "latest": {"1.8.0--r40h5f743cb_0": "sha256:89ea9f33aa6fbf9cf90faee540f9da52134e2242b9e1760d180a7b79875b71cf"}, "tags": {"1.8.0--r40h5f743cb_0": "sha256:89ea9f33aa6fbf9cf90faee540f9da52134e2242b9e1760d180a7b79875b71cf"}, "docker": "quay.io/biocontainers/bioconductor-srnadiff"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-srnadiff.
shpc-registry automated BioContainers addition for bioconductor-srnadiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-srnadiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-srnadiff:1.8.0--r40h5f743cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-srnadiff/1.8.0--r40h5f743cb_0
$ module help quay.io/biocontainers/bioconductor-srnadiff/1.8.0--r40h5f743cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-srnadiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srnadiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-srnadiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-srnadiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-srnadiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-srnadiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-srnadiff

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