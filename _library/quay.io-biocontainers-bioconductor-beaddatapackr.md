---
layout: container
name:  "quay.io/biocontainers/bioconductor-beaddatapackr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beaddatapackr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beaddatapackr/container.yaml"
updated_at: "2024-01-26 03:07:21.569319"
latest: "1.54.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beaddatapackr"

versions:
 - "1.46.0--r41hc0cfd56_2"
 - "1.50.0--r42hc0cfd56_0"
 - "1.50.0--r42ha9d7317_2"
 - "1.52.0--r43ha9d7317_0"
 - "1.54.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beaddatapackr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beaddatapackr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beaddatapackr", "latest": {"1.54.0--r43ha9d7317_0": "sha256:153bfeea12df8656de550af7ab00a9a1560f474f34644138ae5d9026b1d893b7"}, "tags": {"1.46.0--r41hc0cfd56_2": "sha256:5b38e003be90ae8fcd4e39b816476d86e9aca1f165a56cf627610b14c15eaad7", "1.50.0--r42hc0cfd56_0": "sha256:88132f206bba6bf9a1f27485292f8aacf0b56db1be3d2f94cd8a1716cb329b44", "1.50.0--r42ha9d7317_2": "sha256:855db12ec5317823fddf33caae726080144637c325f251765fd39779d4b9bdaf", "1.52.0--r43ha9d7317_0": "sha256:a8d69b4ca945b1695a746f5ddf097c3c259b0fbdb9bbfb94b62d6223453122d4", "1.54.0--r43ha9d7317_0": "sha256:153bfeea12df8656de550af7ab00a9a1560f474f34644138ae5d9026b1d893b7"}, "docker": "quay.io/biocontainers/bioconductor-beaddatapackr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beaddatapackr.
shpc-registry automated BioContainers addition for bioconductor-beaddatapackr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beaddatapackr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beaddatapackr:1.54.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beaddatapackr/1.54.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-beaddatapackr/1.54.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beaddatapackr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beaddatapackr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beaddatapackr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beaddatapackr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beaddatapackr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beaddatapackr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beaddatapackr

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