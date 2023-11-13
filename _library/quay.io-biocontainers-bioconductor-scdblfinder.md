---
layout: container
name:  "quay.io/biocontainers/bioconductor-scdblfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scdblfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scdblfinder/container.yaml"
updated_at: "2023-11-13 02:30:41.019729"
latest: "1.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scdblfinder"
aliases:
 - "xgboost"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scdblfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scdblfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scdblfinder", "latest": {"1.12.0--r42hdfd78af_0": "sha256:57fa2d191b6e48dfa047a0cd304ae9f85a5045ec3cf55069bab652f0f686d032"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:0adcef7f4ef4a4399eb2d2ae9f8731aaae0bb532c6edf02df98a1005be39c158", "1.12.0--r42hdfd78af_0": "sha256:57fa2d191b6e48dfa047a0cd304ae9f85a5045ec3cf55069bab652f0f686d032"}, "docker": "quay.io/biocontainers/bioconductor-scdblfinder", "aliases": {"xgboost": "/usr/local/bin/xgboost"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scdblfinder.
shpc-registry automated BioContainers addition for bioconductor-scdblfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scdblfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scdblfinder:1.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scdblfinder/1.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scdblfinder/1.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scdblfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdblfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scdblfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scdblfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scdblfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scdblfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
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