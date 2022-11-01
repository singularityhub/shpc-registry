---
layout: container
name:  "quay.io/biocontainers/bioconductor-brgedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-brgedata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-brgedata/container.yaml"
updated_at: "2022-11-01 03:55:13.638120"
latest: "1.8.0--r36_0"
container_url: "https://biocontainers.pro/tools/bioconductor-brgedata"
aliases:
 - ".bioconductor-brgedata-post-link.sh"
 - ".bioconductor-brgedata-pre-unlink.sh"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-brgedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-brgedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-brgedata", "latest": {"1.8.0--r36_0": "sha256:d5f8d6876a50dfd0a72b1758edee58dbf20aa2b626f369f161350da4676aba16"}, "tags": {"1.8.0--r36_0": "sha256:d5f8d6876a50dfd0a72b1758edee58dbf20aa2b626f369f161350da4676aba16"}, "docker": "quay.io/biocontainers/bioconductor-brgedata", "aliases": {".bioconductor-brgedata-post-link.sh": "/usr/local/bin/.bioconductor-brgedata-post-link.sh", ".bioconductor-brgedata-pre-unlink.sh": "/usr/local/bin/.bioconductor-brgedata-pre-unlink.sh", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-brgedata.
shpc-registry automated BioContainers addition for bioconductor-brgedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-brgedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-brgedata:1.8.0--r36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-brgedata/1.8.0--r36_0
$ module help quay.io/biocontainers/bioconductor-brgedata/1.8.0--r36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-brgedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brgedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brgedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-brgedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-brgedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-brgedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-brgedata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-brgedata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-brgedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-brgedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-brgedata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-brgedata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-brgedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-brgedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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