---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocbaseutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocbaseutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocbaseutils/container.yaml"
updated_at: "2025-08-29 03:46:20.235266"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocbaseutils"

versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-biocbaseutils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocbaseutils", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-biocbaseutils", "latest": {"1.8.0--r44hdfd78af_0": "sha256:b55cbfd5f824472414c571f7d0830bf8902e1faa62b56f0459eb6fd82a787594"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:54a7f4d107d7b88a4d2594eaafdbb86470bf81d00fa5d2f8d4b213722dcd9e3c", "1.2.0--r43hdfd78af_0": "sha256:29556fe0119bd2e7fd1624968f47cf89a7cab915e9896e116dfa471c50e6d065", "1.4.0--r43hdfd78af_0": "sha256:28857c5d92405d00d642c1d1a53d7ec6b13a7e4a87bacb9782447946faef9087", "1.8.0--r44hdfd78af_0": "sha256:b55cbfd5f824472414c571f7d0830bf8902e1faa62b56f0459eb6fd82a787594"}, "docker": "quay.io/biocontainers/bioconductor-biocbaseutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocbaseutils.
singularity registry hpc automated addition for bioconductor-biocbaseutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocbaseutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocbaseutils:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocbaseutils/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocbaseutils/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocbaseutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocbaseutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocbaseutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocbaseutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocbaseutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocbaseutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocbaseutils

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