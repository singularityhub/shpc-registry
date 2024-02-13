---
layout: container
name:  "quay.io/biocontainers/bioconductor-repitools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-repitools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-repitools/container.yaml"
updated_at: "2024-02-13 02:23:59.366547"
latest: "1.48.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-repitools"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.46.0--r43ha9d7317_0"
 - "1.48.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-repitools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-repitools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-repitools", "latest": {"1.48.0--r43ha9d7317_0": "sha256:1d348a3aaec77da3b5ba5a1af4ca57feb1855c570e43ff7f2cd081329d440749"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:ca8971cc74d7e27b9d32ec0d4190332b25ad841407d8d9af493da7ebf366841d", "1.44.0--r42hc0cfd56_0": "sha256:106848a72d64fd1580aa3f3408b821ed8d3095018c5aafc87ed5595b4cac8749", "1.44.0--r42ha9d7317_1": "sha256:411f8e872bfa4f245f6f79bea16817c3f5581f632141bf6e805e4ef984c8d2b9", "1.46.0--r43ha9d7317_0": "sha256:c320451454a518e1c375fb51c7f3f0e9949e98375d8a76165fe5803a92b17642", "1.48.0--r43ha9d7317_0": "sha256:1d348a3aaec77da3b5ba5a1af4ca57feb1855c570e43ff7f2cd081329d440749"}, "docker": "quay.io/biocontainers/bioconductor-repitools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-repitools.
shpc-registry automated BioContainers addition for bioconductor-repitools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-repitools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-repitools:1.48.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-repitools/1.48.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-repitools/1.48.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-repitools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-repitools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-repitools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-repitools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-repitools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-repitools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-repitools

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