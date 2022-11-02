---
layout: container
name:  "quay.io/biocontainers/bioconductor-dexmadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dexmadata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dexmadata/container.yaml"
updated_at: "2022-11-02 19:40:44.524841"
latest: "1.2.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-dexmadata"
aliases:
 - ".bioconductor-dexmadata-post-link.sh"
 - ".bioconductor-dexmadata-pre-unlink.sh"
versions:
 - "1.2.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-dexmadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dexmadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dexmadata", "latest": {"1.2.0--r41hdfd78af_1": "sha256:0b44750cfadb17adec6a22adf72d816dfbcd56c9ac843c7928b11db610f0e2b7"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:0b44750cfadb17adec6a22adf72d816dfbcd56c9ac843c7928b11db610f0e2b7"}, "docker": "quay.io/biocontainers/bioconductor-dexmadata", "aliases": {".bioconductor-dexmadata-post-link.sh": "/usr/local/bin/.bioconductor-dexmadata-post-link.sh", ".bioconductor-dexmadata-pre-unlink.sh": "/usr/local/bin/.bioconductor-dexmadata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dexmadata.
shpc-registry automated BioContainers addition for bioconductor-dexmadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dexmadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dexmadata:1.2.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dexmadata/1.2.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-dexmadata/1.2.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dexmadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexmadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexmadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dexmadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dexmadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dexmadata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-dexmadata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-dexmadata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-dexmadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-dexmadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-dexmadata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-dexmadata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-dexmadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-dexmadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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