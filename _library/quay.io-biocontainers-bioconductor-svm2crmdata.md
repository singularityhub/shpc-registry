---
layout: container
name:  "quay.io/biocontainers/bioconductor-svm2crmdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-svm2crmdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-svm2crmdata/container.yaml"
updated_at: "2022-11-11 00:34:56.672913"
latest: "1.26.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-svm2crmdata"
aliases:
 - ".bioconductor-svm2crmdata-post-link.sh"
 - ".bioconductor-svm2crmdata-pre-unlink.sh"
versions:
 - "1.26.0--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-svm2crmdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-svm2crmdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-svm2crmdata", "latest": {"1.26.0--r41hdfd78af_1": "sha256:8fdc532945c19b531a400ff8ca15c7f1885bd8c494c387e5bdbde36d14fd045a"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:8fdc532945c19b531a400ff8ca15c7f1885bd8c494c387e5bdbde36d14fd045a"}, "docker": "quay.io/biocontainers/bioconductor-svm2crmdata", "aliases": {".bioconductor-svm2crmdata-post-link.sh": "/usr/local/bin/.bioconductor-svm2crmdata-post-link.sh", ".bioconductor-svm2crmdata-pre-unlink.sh": "/usr/local/bin/.bioconductor-svm2crmdata-pre-unlink.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-svm2crmdata.
shpc-registry automated BioContainers addition for bioconductor-svm2crmdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-svm2crmdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-svm2crmdata:1.26.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-svm2crmdata/1.26.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-svm2crmdata/1.26.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-svm2crmdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svm2crmdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svm2crmdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-svm2crmdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-svm2crmdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-svm2crmdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-svm2crmdata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-svm2crmdata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-svm2crmdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-svm2crmdata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-svm2crmdata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-svm2crmdata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-svm2crmdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-svm2crmdata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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