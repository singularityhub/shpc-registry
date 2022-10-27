---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipcomp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipcomp/container.yaml"
updated_at: "2022-10-27 01:12:02.804163"
latest: "1.8.0--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipcomp"
aliases:
 - ".bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh"
 - "BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz"
 - "BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz"
versions:
 - "1.8.0--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipcomp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipcomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipcomp", "latest": {"1.8.0--r3.4.1_0": "sha256:0b04e3775e9354d1d1d6c39c9ec6d62a9cf8c3a6d1b03d041f834d560876cd7c"}, "tags": {"1.8.0--r3.4.1_0": "sha256:0b04e3775e9354d1d1d6c39c9ec6d62a9cf8c3a6d1b03d041f834d560876cd7c"}, "docker": "quay.io/biocontainers/bioconductor-chipcomp", "aliases": {".bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh": "/usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh", "BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz", "BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipcomp.
shpc-registry automated BioContainers addition for bioconductor-chipcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipcomp:1.8.0--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipcomp/1.8.0--r3.4.1_0
$ module help quay.io/biocontainers/bioconductor-chipcomp/1.8.0--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipcomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm9-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BSgenome.Hsapiens.UCSC.hg19_1.4.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BSgenome.Mmusculus.UCSC.mm9_1.4.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
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