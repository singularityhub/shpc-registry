---
layout: container
name:  "quay.io/biocontainers/bioconductor-gse13015"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gse13015/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gse13015/container.yaml"
updated_at: "2022-10-27 01:02:54.322642"
latest: "1.2.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-gse13015"
aliases:
 - ".bioconductor-gse13015-post-link.sh"
 - ".bioconductor-gse13015-pre-unlink.sh"
versions:
 - "1.2.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-gse13015"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gse13015", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gse13015", "latest": {"1.2.0--r41hdfd78af_1": "sha256:5b0ebe6c33ace410feb8ab42cf9a48ee04010474ff652095318a93bfa7308cf2"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:5b0ebe6c33ace410feb8ab42cf9a48ee04010474ff652095318a93bfa7308cf2"}, "docker": "quay.io/biocontainers/bioconductor-gse13015", "aliases": {".bioconductor-gse13015-post-link.sh": "/usr/local/bin/.bioconductor-gse13015-post-link.sh", ".bioconductor-gse13015-pre-unlink.sh": "/usr/local/bin/.bioconductor-gse13015-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gse13015.
shpc-registry automated BioContainers addition for bioconductor-gse13015
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gse13015
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gse13015:1.2.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gse13015/1.2.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-gse13015/1.2.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gse13015-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse13015-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse13015-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gse13015-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gse13015-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gse13015-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-gse13015-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gse13015-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gse13015-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gse13015-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-gse13015-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gse13015-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gse13015-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gse13015-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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