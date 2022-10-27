---
layout: container
name:  "quay.io/biocontainers/bioconductor-genestructuretools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genestructuretools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genestructuretools/container.yaml"
updated_at: "2022-10-27 00:56:53.539069"
latest: "1.8.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genestructuretools"
aliases:
 - ".bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh"
 - ".bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh"
versions:
 - "1.8.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genestructuretools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genestructuretools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genestructuretools", "latest": {"1.8.0--r40_0": "sha256:6667cd7b4df5fb4b4e0fbe5d9e38c11a27069fff76b2914759dde5b5ee6c10ca"}, "tags": {"1.8.0--r40_0": "sha256:6667cd7b4df5fb4b4e0fbe5d9e38c11a27069fff76b2914759dde5b5ee6c10ca"}, "docker": "quay.io/biocontainers/bioconductor-genestructuretools", "aliases": {".bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh": "/usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh", ".bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh": "/usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genestructuretools.
shpc-registry automated BioContainers addition for bioconductor-genestructuretools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genestructuretools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genestructuretools:1.8.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genestructuretools/1.8.0--r40_0
$ module help quay.io/biocontainers/bioconductor-genestructuretools/1.8.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genestructuretools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genestructuretools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genestructuretools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genestructuretools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genestructuretools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genestructuretools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bsgenome.mmusculus.ucsc.mm10-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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