---
layout: container
name:  "quay.io/biocontainers/bioconductor-matrixrider"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-matrixrider/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-matrixrider/container.yaml"
updated_at: "2024-10-14 03:30:39.243144"
latest: "1.34.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-matrixrider"

versions:
 - "1.26.0--r41hc0cfd56_2"
 - "1.30.0--r42hc0cfd56_0"
 - "1.30.0--r42ha9d7317_1"
 - "1.32.0--r43ha9d7317_0"
 - "1.34.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-matrixrider"
config: {"url": "https://biocontainers.pro/tools/bioconductor-matrixrider", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-matrixrider", "latest": {"1.34.0--r43ha9d7317_0": "sha256:f94ad9b3c5f9aeadfbdb264489d242d237da6fe3cb707634c0d93a9c07678648"}, "tags": {"1.26.0--r41hc0cfd56_2": "sha256:6bdf7b84239b99e01350e02ab43d120a1e07dcad769e75a89a727f7c1912d838", "1.30.0--r42hc0cfd56_0": "sha256:d11ca7c9ffffe563ce25c712f64b86eb92faafcc8f3e3bf214c5998e9ea2c7a9", "1.30.0--r42ha9d7317_1": "sha256:30d35c273afc3c55407fe28f5d235237dd299ce912bb41329bfe22b6cf2edcd7", "1.32.0--r43ha9d7317_0": "sha256:568c8631228a04149b7c1c265e41b668daaf4f14e1eeeaaf6cefd188816b3bcc", "1.34.0--r43ha9d7317_0": "sha256:f94ad9b3c5f9aeadfbdb264489d242d237da6fe3cb707634c0d93a9c07678648"}, "docker": "quay.io/biocontainers/bioconductor-matrixrider"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-matrixrider.
shpc-registry automated BioContainers addition for bioconductor-matrixrider
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-matrixrider
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-matrixrider:1.34.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-matrixrider/1.34.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-matrixrider/1.34.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-matrixrider-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matrixrider-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-matrixrider-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-matrixrider-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-matrixrider-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-matrixrider-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-matrixrider

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