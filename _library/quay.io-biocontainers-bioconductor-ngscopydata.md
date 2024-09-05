---
layout: container
name:  "quay.io/biocontainers/bioconductor-ngscopydata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ngscopydata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ngscopydata/container.yaml"
updated_at: "2024-09-05 03:17:13.960693"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ngscopydata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ngscopydata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ngscopydata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ngscopydata", "latest": {"1.22.0--r43hdfd78af_0": "sha256:1c48a8920d2a1ba4cb9c3a0c62d0b198aecc3b42d95c414b0cc3ed9e773a64bd"}, "tags": {"1.9.0--r40_0": "sha256:8d4e563698e044531de6ab62a31af47d4e15a2aa527fe5b962cad9a395cb0df8", "1.17.0--r42hdfd78af_0": "sha256:3c85fae391fab268745da46eb93d20aeca5b8a31f683325b630273c0586b1142", "1.14.0--r41hdfd78af_1": "sha256:cd58bc6a12638ceb5d2b692f151f05fa3a8e711ed6d77cc79c728055299ab121", "1.12.0--r41hdfd78af_0": "sha256:307f6491a635662037466d305f8cc691b6b87b9e2588af6d124fe3ac7753f793", "1.10.0--r40hdfd78af_1": "sha256:e911f86d114961137237555ccf63c90fb8c5c0cb2301898c5012b672c6ada66d", "1.20.0--r43hdfd78af_0": "sha256:e2a655a8dd05d4b427f8c0d495743761bdf9debf3ede7eddcc858a8cf3447831", "1.22.0--r43hdfd78af_0": "sha256:1c48a8920d2a1ba4cb9c3a0c62d0b198aecc3b42d95c414b0cc3ed9e773a64bd"}, "docker": "quay.io/biocontainers/bioconductor-ngscopydata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ngscopydata.
shpc-registry automated BioContainers addition for bioconductor-ngscopydata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ngscopydata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ngscopydata:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ngscopydata/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ngscopydata/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ngscopydata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ngscopydata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ngscopydata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ngscopydata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ngscopydata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ngscopydata-inspect-deffile:

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