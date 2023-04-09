---
layout: container
name:  "quay.io/biocontainers/bioconductor-mlseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mlseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mlseq/container.yaml"
updated_at: "2023-04-09 02:36:14.546587"
latest: "2.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mlseq"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r40hdfd78af_1"
 - "2.16.0--r42hdfd78af_0"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mlseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mlseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mlseq", "latest": {"2.16.0--r42hdfd78af_0": "sha256:c2b46105a4c2d837943aeb74567449eccff534795a69dda84a069c19980e5073"}, "tags": {"2.8.0--r40hdfd78af_1": "sha256:f83763f03c34520e36941f38217c5314a9784ad6f1388cc6595c10853de23288", "2.16.0--r42hdfd78af_0": "sha256:c2b46105a4c2d837943aeb74567449eccff534795a69dda84a069c19980e5073", "2.12.0--r41hdfd78af_0": "sha256:c00cf5e898ffa8a4e9733e47b0cf4d313575b7d516d5a348e10016455170702c", "2.10.0--r41hdfd78af_0": "sha256:2563878ebf1fa3f94a50b2764be1d5291889de924b39f5381f03781e26b97079"}, "docker": "quay.io/biocontainers/bioconductor-mlseq", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mlseq.
shpc-registry automated BioContainers addition for bioconductor-mlseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mlseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mlseq:2.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mlseq/2.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mlseq/2.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mlseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mlseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mlseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mlseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mlseq-inspect-deffile:

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