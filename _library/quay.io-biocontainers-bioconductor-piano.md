---
layout: container
name:  "quay.io/biocontainers/bioconductor-piano"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-piano/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-piano/container.yaml"
updated_at: "2025-08-24 03:44:55.495281"
latest: "2.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-piano"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
 - "2.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-piano"
config: {"url": "https://biocontainers.pro/tools/bioconductor-piano", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-piano", "latest": {"2.22.0--r44hdfd78af_0": "sha256:f9ab3ee7c2e8ac3db6616f9e46da4166271bcab3a3e83fb400bfda85f645ba01"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:5e73e4e0165d1d2f788c7ca797628684b466512b60a5bc68583beb9096d3cc3f", "2.14.0--r42hdfd78af_0": "sha256:1783ae80860735d738e07682369ecb6a5a3c094bb0bb37a6d9d1ccbe5751863e", "2.10.0--r41hdfd78af_0": "sha256:929c378bc0222dde8c2c79705c33e914e9efc6368c57a76f3d749840146722c1", "2.16.0--r43hdfd78af_0": "sha256:48c9c156ab37c88cc48e62583cec06034258eea0045271857e72ba0e06028152", "2.18.0--r43hdfd78af_0": "sha256:a58da83638f75c1a99730b7a775619d58ce03918950afca62cbf722b8452ff7c", "2.22.0--r44hdfd78af_0": "sha256:f9ab3ee7c2e8ac3db6616f9e46da4166271bcab3a3e83fb400bfda85f645ba01"}, "docker": "quay.io/biocontainers/bioconductor-piano", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-piano.
shpc-registry automated BioContainers addition for bioconductor-piano
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-piano
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-piano:2.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-piano/2.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-piano/2.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-piano-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-piano-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-piano-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-piano-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-piano-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-piano-inspect-deffile:

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