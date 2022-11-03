---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsbenchmark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsbenchmark/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsbenchmark/container.yaml"
updated_at: "2022-11-03 00:26:43.466973"
latest: "1.9.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsbenchmark"
aliases:
 - ".bioconductor-gsbenchmark-post-link.sh"
 - ".bioconductor-gsbenchmark-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsbenchmark"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsbenchmark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsbenchmark", "latest": {"1.9.0--r40_0": "sha256:6f52b767b4c53a7a9b208f221f5e1235e787b15dab2f65b9855988eae517599e"}, "tags": {"1.9.0--r40_0": "sha256:6f52b767b4c53a7a9b208f221f5e1235e787b15dab2f65b9855988eae517599e"}, "docker": "quay.io/biocontainers/bioconductor-gsbenchmark", "aliases": {".bioconductor-gsbenchmark-post-link.sh": "/usr/local/bin/.bioconductor-gsbenchmark-post-link.sh", ".bioconductor-gsbenchmark-pre-unlink.sh": "/usr/local/bin/.bioconductor-gsbenchmark-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsbenchmark.
shpc-registry automated BioContainers addition for bioconductor-gsbenchmark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsbenchmark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsbenchmark:1.9.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsbenchmark/1.9.0--r40_0
$ module help quay.io/biocontainers/bioconductor-gsbenchmark/1.9.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsbenchmark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsbenchmark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsbenchmark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsbenchmark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsbenchmark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsbenchmark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-gsbenchmark-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gsbenchmark-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsbenchmark-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsbenchmark-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-gsbenchmark-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-gsbenchmark-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsbenchmark-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-gsbenchmark-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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