---
layout: container
name:  "quay.io/biocontainers/bioconductor-neighbornet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-neighbornet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-neighbornet/container.yaml"
updated_at: "2025-03-24 03:24:14.692465"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-neighbornet"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-neighbornet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-neighbornet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-neighbornet", "latest": {"1.18.0--r43hdfd78af_0": "sha256:a792d143314ddfb7add981aa63fb270661593628fd4690bd62b8edb6dfd93aff"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:a8412f69c6fc4324b81a2f79935ad25f35201207dd936d8015754c5a0d63584c", "1.16.0--r42hdfd78af_0": "sha256:76ca47ef8cac8fbcf94a42d5b89147636e0fa773a8b43f81a0e4396b064d7b3f", "1.12.0--r41hdfd78af_0": "sha256:5b8f00bd12237d4055ba45443a79ba67c06e0e6c8aa997e99a9e4854f041eb7f", "1.10.0--r41hdfd78af_0": "sha256:8d2926f1a07648a592305d40db4d6674eba95e50c15ebb7887b87cba824777f6", "1.18.0--r43hdfd78af_0": "sha256:a792d143314ddfb7add981aa63fb270661593628fd4690bd62b8edb6dfd93aff"}, "docker": "quay.io/biocontainers/bioconductor-neighbornet", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-neighbornet.
shpc-registry automated BioContainers addition for bioconductor-neighbornet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-neighbornet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-neighbornet:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-neighbornet/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-neighbornet/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-neighbornet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neighbornet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neighbornet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-neighbornet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-neighbornet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-neighbornet-inspect-deffile:

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