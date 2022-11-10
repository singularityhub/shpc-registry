---
layout: container
name:  "quay.io/biocontainers/bioconductor-varianttoolsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-varianttoolsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-varianttoolsdata/container.yaml"
updated_at: "2022-11-09 23:36:59.525290"
latest: "1.8.0--r36_1"
container_url: "https://biocontainers.pro/tools/bioconductor-varianttoolsdata"
aliases:
 - ".bioconductor-varianttoolsdata-post-link.sh"
 - ".bioconductor-varianttoolsdata-pre-unlink.sh"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-varianttoolsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata", "latest": {"1.8.0--r36_1": "sha256:cc5b0da1cddb5df9031ede5bef86ef5be44d7e7fba6269842fdb87a77cddffca"}, "tags": {"1.8.0--r36_1": "sha256:cc5b0da1cddb5df9031ede5bef86ef5be44d7e7fba6269842fdb87a77cddffca"}, "docker": "quay.io/biocontainers/bioconductor-varianttoolsdata", "aliases": {".bioconductor-varianttoolsdata-post-link.sh": "/usr/local/bin/.bioconductor-varianttoolsdata-post-link.sh", ".bioconductor-varianttoolsdata-pre-unlink.sh": "/usr/local/bin/.bioconductor-varianttoolsdata-pre-unlink.sh", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-varianttoolsdata.
shpc-registry automated BioContainers addition for bioconductor-varianttoolsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttoolsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-varianttoolsdata:1.8.0--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-varianttoolsdata/1.8.0--r36_1
$ module help quay.io/biocontainers/bioconductor-varianttoolsdata/1.8.0--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-varianttoolsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttoolsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varianttoolsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-varianttoolsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-varianttoolsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-varianttoolsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-varianttoolsdata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-varianttoolsdata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-varianttoolsdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-varianttoolsdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-varianttoolsdata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-varianttoolsdata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-varianttoolsdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-varianttoolsdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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