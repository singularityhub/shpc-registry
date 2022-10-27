---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowfit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowfit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowfit/container.yaml"
updated_at: "2022-10-27 00:57:03.426072"
latest: "1.24.0--r36_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowfit"

versions:
 - "1.24.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowfit"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowfit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowfit", "latest": {"1.24.0--r36_0": "sha256:964bd108b617db78fc3f9c5dd8b05f06df7af3fb533856382be6551c3665d8cb"}, "tags": {"1.24.0--r36_0": "sha256:964bd108b617db78fc3f9c5dd8b05f06df7af3fb533856382be6551c3665d8cb"}, "docker": "quay.io/biocontainers/bioconductor-flowfit"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowfit.
shpc-registry automated BioContainers addition for bioconductor-flowfit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowfit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowfit:1.24.0--r36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowfit/1.24.0--r36_0
$ module help quay.io/biocontainers/bioconductor-flowfit/1.24.0--r36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowfit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowfit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowfit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowfit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowfit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowfit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowfit

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