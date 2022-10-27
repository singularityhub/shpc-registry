---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/container.yaml"
updated_at: "2022-10-27 00:35:52.589830"
latest: "3.4.0--r40_9"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
aliases:
 - ".bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh"
 - ".bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh"
versions:
 - "3.4.0--r40_9"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "latest": {"3.4.0--r40_9": "sha256:b87d48cf341dba877002e1d819a519170e1e2163597a24fd8e380ee0035579e2"}, "tags": {"3.4.0--r40_9": "sha256:b87d48cf341dba877002e1d819a519170e1e2163597a24fd8e380ee0035579e2"}, "docker": "quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene", "aliases": {".bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh": "/usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh", ".bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh": "/usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.mmusculus.ucsc.mm10.ensgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene:3.4.0--r40_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/3.4.0--r40_9
$ module help quay.io/biocontainers/bioconductor-txdb.mmusculus.ucsc.mm10.ensgene/3.4.0--r40_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-txdb.mmusculus.ucsc.mm10.ensgene-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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