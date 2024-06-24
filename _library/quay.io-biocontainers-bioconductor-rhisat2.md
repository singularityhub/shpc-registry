---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhisat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhisat2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhisat2/container.yaml"
updated_at: "2024-06-24 03:09:20.128278"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rhisat2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hc247a5b_0"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rhisat2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhisat2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhisat2", "latest": {"1.18.0--r43hf17093f_0": "sha256:358efe5397c579804df6a17460c1ecb643a857d8ed4cef2084be2d89946499d9"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:94895883ad4da2b7503ff478255035b6f784cab51cb29f852fd275b9d5421c4d", "1.10.0--r41hc247a5b_2": "sha256:c182b49acb8a4b565d63f22c2a87169e229e7e95c4da0c99b41e44127e4b7547", "1.14.0--r42hc247a5b_0": "sha256:e4c4d7ae6de0ccf86636e239ce3974c90d208b37a24dcca98ce424b2bfaf4273", "1.14.0--r42hf17093f_1": "sha256:a809b6934492269e076f356926d37fbb0bbc06ec3279e0911f6777a053930516", "1.16.0--r43hf17093f_0": "sha256:f745bb5bfd9823f036e73cc0f62afe5f443b1215e98e0f9ac432a7d7d1683ac0", "1.18.0--r43hf17093f_0": "sha256:358efe5397c579804df6a17460c1ecb643a857d8ed4cef2084be2d89946499d9"}, "docker": "quay.io/biocontainers/bioconductor-rhisat2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhisat2.
shpc-registry automated BioContainers addition for bioconductor-rhisat2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhisat2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhisat2:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhisat2/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rhisat2/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhisat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhisat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhisat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhisat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhisat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhisat2-inspect-deffile:

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