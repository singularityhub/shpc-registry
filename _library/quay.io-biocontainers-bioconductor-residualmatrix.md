---
layout: container
name:  "quay.io/biocontainers/bioconductor-residualmatrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-residualmatrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-residualmatrix/container.yaml"
updated_at: "2023-10-13 03:16:21.366833"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-residualmatrix"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-residualmatrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-residualmatrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-residualmatrix", "latest": {"1.10.0--r43hdfd78af_0": "sha256:128c4bfa55f0bccda2484e9fd8b1e3925a63c3310dd4ba2034d402e2705a8b27"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:e4a5bb7e77511b76496304f57de9f06f529fae1765d88c13a8f8c1884e0b5c8c", "1.8.0--r42hdfd78af_0": "sha256:60f909fee719423873aa6b7560de05b1874afb8e2c163461e11fc890229fd60e", "1.10.0--r43hdfd78af_0": "sha256:128c4bfa55f0bccda2484e9fd8b1e3925a63c3310dd4ba2034d402e2705a8b27"}, "docker": "quay.io/biocontainers/bioconductor-residualmatrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-residualmatrix.
shpc-registry automated BioContainers addition for bioconductor-residualmatrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-residualmatrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-residualmatrix:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-residualmatrix/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-residualmatrix/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-residualmatrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-residualmatrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-residualmatrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-residualmatrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-residualmatrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-residualmatrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-residualmatrix

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