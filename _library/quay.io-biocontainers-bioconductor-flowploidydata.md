---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowploidydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowploidydata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowploidydata/container.yaml"
updated_at: "2022-10-29 08:18:45.081256"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowploidydata"
aliases:
 - ".bioconductor-flowploidydata-post-link.sh"
 - ".bioconductor-flowploidydata-pre-unlink.sh"
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowploidydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowploidydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowploidydata", "latest": {"1.8.0--r351_0": "sha256:bec36b6640bc91bf66d4c2c6e9a2171400fd6fe04e84a0145ccab00edad21745"}, "tags": {"1.8.0--r351_0": "sha256:bec36b6640bc91bf66d4c2c6e9a2171400fd6fe04e84a0145ccab00edad21745"}, "docker": "quay.io/biocontainers/bioconductor-flowploidydata", "aliases": {".bioconductor-flowploidydata-post-link.sh": "/usr/local/bin/.bioconductor-flowploidydata-post-link.sh", ".bioconductor-flowploidydata-pre-unlink.sh": "/usr/local/bin/.bioconductor-flowploidydata-pre-unlink.sh", "wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowploidydata.
shpc-registry automated BioContainers addition for bioconductor-flowploidydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowploidydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowploidydata:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowploidydata/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-flowploidydata/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowploidydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowploidydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowploidydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowploidydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowploidydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowploidydata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-flowploidydata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-flowploidydata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowploidydata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowploidydata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-flowploidydata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-flowploidydata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowploidydata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-flowploidydata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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