---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathwaysplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathwaysplice/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathwaysplice/container.yaml"
updated_at: "2022-10-27 00:39:24.941913"
latest: "1.8.0--r36_1"
container_url: "https://biocontainers.pro/tools/bioconductor-pathwaysplice"
aliases:
 - ".bioconductor-genelendatabase-post-link.sh"
 - ".bioconductor-genelendatabase-pre-unlink.sh"
 - ".bioconductor-pfam.db-post-link.sh"
 - ".bioconductor-pfam.db-pre-unlink.sh"
versions:
 - "1.8.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-pathwaysplice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathwaysplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathwaysplice", "latest": {"1.8.0--r36_1": "sha256:73b9ae499b7e96a0a747dc4c1ef3610abe7c87fb6b1364c1f481a202167b486f"}, "tags": {"1.8.0--r36_1": "sha256:73b9ae499b7e96a0a747dc4c1ef3610abe7c87fb6b1364c1f481a202167b486f"}, "docker": "quay.io/biocontainers/bioconductor-pathwaysplice", "aliases": {".bioconductor-genelendatabase-post-link.sh": "/usr/local/bin/.bioconductor-genelendatabase-post-link.sh", ".bioconductor-genelendatabase-pre-unlink.sh": "/usr/local/bin/.bioconductor-genelendatabase-pre-unlink.sh", ".bioconductor-pfam.db-post-link.sh": "/usr/local/bin/.bioconductor-pfam.db-post-link.sh", ".bioconductor-pfam.db-pre-unlink.sh": "/usr/local/bin/.bioconductor-pfam.db-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathwaysplice.
shpc-registry automated BioContainers addition for bioconductor-pathwaysplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathwaysplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathwaysplice:1.8.0--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathwaysplice/1.8.0--r36_1
$ module help quay.io/biocontainers/bioconductor-pathwaysplice/1.8.0--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathwaysplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathwaysplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathwaysplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathwaysplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathwaysplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathwaysplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-genelendatabase-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-genelendatabase-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-genelendatabase-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-genelendatabase-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-genelendatabase-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-genelendatabase-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-genelendatabase-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-genelendatabase-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-pfam.db-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-pfam.db-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-pfam.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-pfam.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-pfam.db-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-pfam.db-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-pfam.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-pfam.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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