---
layout: container
name:  "quay.io/biocontainers/bioconductor-pairadise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pairadise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pairadise/container.yaml"
updated_at: "2023-10-02 03:16:00.377220"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pairadise"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pairadise"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pairadise", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pairadise", "latest": {"1.16.0--r43hdfd78af_0": "sha256:04101b2b3acdad028f97fd25941b8a68a10042760a6c42b38ecc25eeac881b47"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:661802560e9fcbc01d251bd5e59aa4e7a2c2ab2044aebf1177ee5c92996c8b91", "1.14.0--r42hdfd78af_0": "sha256:342a434762064df1882526c214377c4e6ca02d4a3d4713392cb506276857f835", "1.10.0--r41hdfd78af_0": "sha256:26dcb2d7af4f9bb778f9dab78a50414733a03b176c3c546b0d9baee7ff5661dc", "1.16.0--r43hdfd78af_0": "sha256:04101b2b3acdad028f97fd25941b8a68a10042760a6c42b38ecc25eeac881b47"}, "docker": "quay.io/biocontainers/bioconductor-pairadise", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pairadise.
shpc-registry automated BioContainers addition for bioconductor-pairadise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pairadise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pairadise:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pairadise/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pairadise/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pairadise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pairadise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pairadise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pairadise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pairadise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pairadise-inspect-deffile:

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