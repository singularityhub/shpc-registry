---
layout: container
name:  "quay.io/biocontainers/bioconductor-scate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scate/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scate/container.yaml"
updated_at: "2022-11-02 00:32:41.592539"
latest: "1.4.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scate"
aliases:
 - ".bioconductor-scatedata-post-link.sh"
 - ".bioconductor-scatedata-pre-unlink.sh"
 - "xgboost"
versions:
 - "1.4.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scate"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scate", "latest": {"1.4.0--r41hdfd78af_0": "sha256:d48cc511ae5f2c15d8768bbda2aaeb3ab1f076fbdf57136553a0dd28373bfe6b"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:d48cc511ae5f2c15d8768bbda2aaeb3ab1f076fbdf57136553a0dd28373bfe6b"}, "docker": "quay.io/biocontainers/bioconductor-scate", "aliases": {".bioconductor-scatedata-post-link.sh": "/usr/local/bin/.bioconductor-scatedata-post-link.sh", ".bioconductor-scatedata-pre-unlink.sh": "/usr/local/bin/.bioconductor-scatedata-pre-unlink.sh", "xgboost": "/usr/local/bin/xgboost"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scate.
shpc-registry automated BioContainers addition for bioconductor-scate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scate:1.4.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scate/1.4.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scate/1.4.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-scatedata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-scatedata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-scatedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-scatedata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-scatedata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-scatedata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-scatedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-scatedata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
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