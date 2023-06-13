---
layout: container
name:  "quay.io/biocontainers/bioconductor-encodexplorerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-encodexplorerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-encodexplorerdata/container.yaml"
updated_at: "2023-06-13 03:11:49.332618"
latest: "0.99.5--r42hdfd78af_6"
container_url: "https://biocontainers.pro/tools/bioconductor-encodexplorerdata"

versions:
 - "0.99.5--r41hdfd78af_5"
 - "0.99.5--r42hdfd78af_6"
description: "shpc-registry automated BioContainers addition for bioconductor-encodexplorerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-encodexplorerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-encodexplorerdata", "latest": {"0.99.5--r42hdfd78af_6": "sha256:947c0aa3ea53f592371a01ee83c711e32b77e4c1fbce397b9c2ce49d688a707e"}, "tags": {"0.99.5--r41hdfd78af_5": "sha256:4474650f03b23a056f473ea7078f5150ee687527468d4a8588a376d230172c7c", "0.99.5--r42hdfd78af_6": "sha256:947c0aa3ea53f592371a01ee83c711e32b77e4c1fbce397b9c2ce49d688a707e"}, "docker": "quay.io/biocontainers/bioconductor-encodexplorerdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-encodexplorerdata.
shpc-registry automated BioContainers addition for bioconductor-encodexplorerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-encodexplorerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-encodexplorerdata:0.99.5--r42hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-encodexplorerdata/0.99.5--r42hdfd78af_6
$ module help quay.io/biocontainers/bioconductor-encodexplorerdata/0.99.5--r42hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-encodexplorerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-encodexplorerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-encodexplorerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-encodexplorerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-encodexplorerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-encodexplorerdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-encodexplorerdata

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