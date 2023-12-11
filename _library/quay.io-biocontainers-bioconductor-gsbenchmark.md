---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsbenchmark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsbenchmark/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsbenchmark/container.yaml"
updated_at: "2023-12-11 02:49:58.473927"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsbenchmark"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsbenchmark"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsbenchmark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsbenchmark", "latest": {"1.20.0--r43hdfd78af_0": "sha256:8359af9e7ca7aa45afc05fd9947896be7a64ae3ed7b8e20f98a76daa835ffac6"}, "tags": {"1.9.0--r40_0": "sha256:6f52b767b4c53a7a9b208f221f5e1235e787b15dab2f65b9855988eae517599e", "1.18.0--r42hdfd78af_0": "sha256:fa96bbd5cd60b4b65ae7aa76a321a31be3c33a93f06d3d4ea0771d65f7084462", "1.14.0--r41hdfd78af_1": "sha256:5267f1a93e3a9deaf38c485d12b36dbf6ffc2c1d6e33771f0a7988010e05c094", "1.12.0--r41hdfd78af_0": "sha256:b297974351d2efd24f67feb1ecd40fc72c71798fd0509727efd7b72d31f5a85e", "1.10.0--r40hdfd78af_1": "sha256:57959ac51618d3f02b971defbb0c9219143514a39bb4bd5f322ee4d6f55a7baa", "1.20.0--r43hdfd78af_0": "sha256:8359af9e7ca7aa45afc05fd9947896be7a64ae3ed7b8e20f98a76daa835ffac6"}, "docker": "quay.io/biocontainers/bioconductor-gsbenchmark", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsbenchmark.
shpc-registry automated BioContainers addition for bioconductor-gsbenchmark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsbenchmark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsbenchmark:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsbenchmark/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsbenchmark/1.20.0--r43hdfd78af_0
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