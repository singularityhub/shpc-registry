---
layout: container
name:  "quay.io/biocontainers/bioconductor-sictools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sictools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sictools/container.yaml"
updated_at: "2024-08-05 02:47:08.194398"
latest: "1.30.0--r43h54b6a8d_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sictools"

versions:
 - "1.24.0--r41h2e7e3aa_2"
 - "1.28.0--r42h2e7e3aa_0"
 - "1.28.0--r42h54b6a8d_1"
 - "1.30.0--r43h54b6a8d_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sictools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sictools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sictools", "latest": {"1.30.0--r43h54b6a8d_0": "sha256:042672110e0218e4b490d4960ff223e2dbda9dff41b66298dacb7dff7777eb99"}, "tags": {"1.24.0--r41h2e7e3aa_2": "sha256:67234c0323f65d7bf968da225b9f8bbba80f275e494ee1d4c95f9d86017e1292", "1.28.0--r42h2e7e3aa_0": "sha256:483bbcd0b8320523cbf0a97ad732e2b4fb8ca1c5f61e77945d9f8b3ab83dc123", "1.28.0--r42h54b6a8d_1": "sha256:1fc053ac6bdb907e413c5d5163eb5602ea3f66472386e04985a9cff0263e5e4d", "1.30.0--r43h54b6a8d_0": "sha256:042672110e0218e4b490d4960ff223e2dbda9dff41b66298dacb7dff7777eb99"}, "docker": "quay.io/biocontainers/bioconductor-sictools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sictools.
shpc-registry automated BioContainers addition for bioconductor-sictools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sictools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sictools:1.30.0--r43h54b6a8d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sictools/1.30.0--r43h54b6a8d_0
$ module help quay.io/biocontainers/bioconductor-sictools/1.30.0--r43h54b6a8d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sictools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sictools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sictools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sictools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sictools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sictools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sictools

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