---
layout: container
name:  "quay.io/biocontainers/bioconductor-chic.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chic.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chic.data/container.yaml"
updated_at: "2026-01-26 04:31:23.811961"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chic.data"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.18.0--r42hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chic.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chic.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chic.data", "latest": {"1.22.0--r43hdfd78af_0": "sha256:e545083086102df0e5a3405e493af0169510c294c5cce100190b8b4d8fe7c2c3"}, "tags": {"1.9.0--r40_0": "sha256:3e4e28ec5a2a671485c57dbd8713c437f82585eb5719d5bf3d6b0d866e7aa2f1", "1.14.0--r41hdfd78af_1": "sha256:e783af1e753a09f9847d36e25fd58cbeec808c48348ae7edcf017e37a320ff76", "1.12.0--r41hdfd78af_0": "sha256:4dced7846866258c662402e451c488444a6c5e46e1d4cfc56f1848193d4906ae", "1.10.0--r40hdfd78af_1": "sha256:94e8accacab341dd4c85bc2360830405bf8fe51490c9dfc8fbf4681aa92da04a", "1.18.0--r42hdfd78af_0": "sha256:ced877703844bd802b89e861649a5331b3457aab290aa264b7d5fa24ec5b938d", "1.20.0--r43hdfd78af_0": "sha256:d6705a25133e8fae6c6e5efc2657274ba12470aa4c26adc36686c10ff3dae6b6", "1.22.0--r43hdfd78af_0": "sha256:e545083086102df0e5a3405e493af0169510c294c5cce100190b8b4d8fe7c2c3"}, "docker": "quay.io/biocontainers/bioconductor-chic.data", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chic.data.
shpc-registry automated BioContainers addition for bioconductor-chic.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chic.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chic.data:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chic.data/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chic.data/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chic.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chic.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chic.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chic.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chic.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chic.data-inspect-deffile:

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