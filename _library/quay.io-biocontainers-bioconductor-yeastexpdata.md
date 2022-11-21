---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeastexpdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeastexpdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeastexpdata/container.yaml"
updated_at: "2022-11-21 00:51:47.775003"
latest: "0.40.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-yeastexpdata"
aliases:
 - ".bioconductor-yeastexpdata-post-link.sh"
 - ".bioconductor-yeastexpdata-pre-unlink.sh"
versions:
 - "0.40.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-yeastexpdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeastexpdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeastexpdata", "latest": {"0.40.0--r41hdfd78af_1": "sha256:b91cbc19e73158a8903f5b9edd5d86117f8e88e86e277af80ae5dac2e78f1af8"}, "tags": {"0.40.0--r41hdfd78af_1": "sha256:b91cbc19e73158a8903f5b9edd5d86117f8e88e86e277af80ae5dac2e78f1af8"}, "docker": "quay.io/biocontainers/bioconductor-yeastexpdata", "aliases": {".bioconductor-yeastexpdata-post-link.sh": "/usr/local/bin/.bioconductor-yeastexpdata-post-link.sh", ".bioconductor-yeastexpdata-pre-unlink.sh": "/usr/local/bin/.bioconductor-yeastexpdata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeastexpdata.
shpc-registry automated BioContainers addition for bioconductor-yeastexpdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastexpdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastexpdata:0.40.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeastexpdata/0.40.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-yeastexpdata/0.40.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeastexpdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastexpdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastexpdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeastexpdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeastexpdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeastexpdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-yeastexpdata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-yeastexpdata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-yeastexpdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-yeastexpdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-yeastexpdata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-yeastexpdata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-yeastexpdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-yeastexpdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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