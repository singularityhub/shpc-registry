---
layout: container
name:  "quay.io/biocontainers/bioconductor-homo.sapiens"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-homo.sapiens/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-homo.sapiens/container.yaml"
updated_at: "2025-09-03 03:08:11.620232"
latest: "1.3.1--r44hdfd78af_17"
container_url: "https://biocontainers.pro/tools/bioconductor-homo.sapiens"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.3.1--r40_9"
 - "1.3.1--r42hdfd78af_14"
 - "1.3.1--r43hdfd78af_15"
 - "1.3.1--r43hdfd78af_16"
 - "1.3.1--r44hdfd78af_17"
description: "shpc-registry automated BioContainers addition for bioconductor-homo.sapiens"
config: {"url": "https://biocontainers.pro/tools/bioconductor-homo.sapiens", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-homo.sapiens", "latest": {"1.3.1--r44hdfd78af_17": "sha256:23327b31e3211c141010844aaa027fabe3ed1748117351227c472930e9afce73"}, "tags": {"1.3.1--r40_9": "sha256:d36836f2b62d6d3740d1312cd44d338b4e12f101bf9582d73aae5b2e2848f709", "1.3.1--r42hdfd78af_14": "sha256:6af85da35480f22cf69fbdf723ad8ccf7a0d48124d4fce35d5da03da2f5a4d44", "1.3.1--r43hdfd78af_15": "sha256:0a8c270b44397eee8ddce77d23999f976e8204698856c3200b4e44046fad54de", "1.3.1--r43hdfd78af_16": "sha256:03de03974181d11ca2204767a65eb9c73e98761528f569e7df5199b5a5f49233", "1.3.1--r44hdfd78af_17": "sha256:23327b31e3211c141010844aaa027fabe3ed1748117351227c472930e9afce73"}, "docker": "quay.io/biocontainers/bioconductor-homo.sapiens", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-homo.sapiens.
shpc-registry automated BioContainers addition for bioconductor-homo.sapiens
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-homo.sapiens
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-homo.sapiens:1.3.1--r44hdfd78af_17
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-homo.sapiens/1.3.1--r44hdfd78af_17
$ module help quay.io/biocontainers/bioconductor-homo.sapiens/1.3.1--r44hdfd78af_17
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-homo.sapiens-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-homo.sapiens-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-homo.sapiens-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-homo.sapiens-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-homo.sapiens-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-homo.sapiens-inspect-deffile:

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