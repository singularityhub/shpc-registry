---
layout: container
name:  "quay.io/biocontainers/bioconductor-rchyoptimyx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rchyoptimyx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rchyoptimyx/container.yaml"
updated_at: "2024-05-27 03:45:17.065097"
latest: "2.28.0--r40h5f743cb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rchyoptimyx"

versions:
 - "2.28.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rchyoptimyx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rchyoptimyx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rchyoptimyx", "latest": {"2.28.0--r40h5f743cb_0": "sha256:a01c7e36ca059985b0932509f9691ab75df8d65017f79cb54bd5a326df13d401"}, "tags": {"2.28.0--r40h5f743cb_0": "sha256:a01c7e36ca059985b0932509f9691ab75df8d65017f79cb54bd5a326df13d401"}, "docker": "quay.io/biocontainers/bioconductor-rchyoptimyx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rchyoptimyx.
shpc-registry automated BioContainers addition for bioconductor-rchyoptimyx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rchyoptimyx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rchyoptimyx:2.28.0--r40h5f743cb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rchyoptimyx/2.28.0--r40h5f743cb_0
$ module help quay.io/biocontainers/bioconductor-rchyoptimyx/2.28.0--r40h5f743cb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rchyoptimyx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rchyoptimyx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rchyoptimyx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rchyoptimyx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rchyoptimyx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rchyoptimyx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rchyoptimyx

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