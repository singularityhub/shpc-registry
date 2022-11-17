---
layout: container
name:  "quay.io/biocontainers/bioconductor-pkgdeptools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pkgdeptools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pkgdeptools/container.yaml"
updated_at: "2022-11-17 02:59:49.869783"
latest: "1.63.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pkgdeptools"

versions:
 - "1.60.0--r41hdfd78af_0"
 - "1.63.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pkgdeptools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pkgdeptools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pkgdeptools", "latest": {"1.63.0--r42hdfd78af_0": "sha256:5b888488a8053ff835e7de01213be1a213917b7fb8e0e577857cfff0bf5e6a2e"}, "tags": {"1.60.0--r41hdfd78af_0": "sha256:4c130b5681ade014f54b17ddea950c239b6c883604fbf061ed3f5e2a46a4075f", "1.63.0--r42hdfd78af_0": "sha256:5b888488a8053ff835e7de01213be1a213917b7fb8e0e577857cfff0bf5e6a2e"}, "docker": "quay.io/biocontainers/bioconductor-pkgdeptools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pkgdeptools.
shpc-registry automated BioContainers addition for bioconductor-pkgdeptools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pkgdeptools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pkgdeptools:1.63.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pkgdeptools/1.63.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pkgdeptools/1.63.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pkgdeptools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pkgdeptools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pkgdeptools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pkgdeptools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pkgdeptools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pkgdeptools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pkgdeptools

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