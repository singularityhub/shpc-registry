---
layout: container
name:  "quay.io/biocontainers/bioconductor-branchpointer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-branchpointer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-branchpointer/container.yaml"
updated_at: "2022-10-27 00:45:50.886494"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-branchpointer"
aliases:
 - ".bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh"
 - ".bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh"
versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-branchpointer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-branchpointer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-branchpointer", "latest": {"1.8.0--r351_0": "sha256:44a0bd4c349c2b752b6ee08b1b8fd93da8dbd9019bc555634757a305f271d2fc"}, "tags": {"1.8.0--r351_0": "sha256:44a0bd4c349c2b752b6ee08b1b8fd93da8dbd9019bc555634757a305f271d2fc"}, "docker": "quay.io/biocontainers/bioconductor-branchpointer", "aliases": {".bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh": "/usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh", ".bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh": "/usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-branchpointer.
shpc-registry automated BioContainers addition for bioconductor-branchpointer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-branchpointer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-branchpointer:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-branchpointer/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-branchpointer/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-branchpointer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-branchpointer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-branchpointer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-branchpointer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-branchpointer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-branchpointer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.hsapiens.ucsc.hg38-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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