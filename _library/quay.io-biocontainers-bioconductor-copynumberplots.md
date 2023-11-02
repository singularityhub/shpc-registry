---
layout: container
name:  "quay.io/biocontainers/bioconductor-copynumberplots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-copynumberplots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-copynumberplots/container.yaml"
updated_at: "2023-11-02 03:04:19.734360"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-copynumberplots"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-copynumberplots"
config: {"url": "https://biocontainers.pro/tools/bioconductor-copynumberplots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-copynumberplots", "latest": {"1.16.0--r43hdfd78af_0": "sha256:baa8aacb1fd56494f6f5ccd943d251ff9e60eaf9391ed48d21a3ff08145a195d"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:d95d160a8fd628263158f7088c74f9b6a2229c225323a73ca5ac736efc58c8e2", "1.14.0--r42hdfd78af_0": "sha256:b336dc5228294c117967fc54264d14e3774c6b0b3d92851220c0c67361c9e344", "1.10.0--r41hdfd78af_0": "sha256:55dea7d23a21b74f47e5a2a11796d69c05b0340f3527f214f58017380d78f712", "1.16.0--r43hdfd78af_0": "sha256:baa8aacb1fd56494f6f5ccd943d251ff9e60eaf9391ed48d21a3ff08145a195d"}, "docker": "quay.io/biocontainers/bioconductor-copynumberplots", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-copynumberplots.
shpc-registry automated BioContainers addition for bioconductor-copynumberplots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-copynumberplots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-copynumberplots:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-copynumberplots/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-copynumberplots/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-copynumberplots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copynumberplots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-copynumberplots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-copynumberplots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-copynumberplots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-copynumberplots-inspect-deffile:

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