---
layout: container
name:  "quay.io/biocontainers/bioconductor-hcaexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hcaexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hcaexplorer/container.yaml"
updated_at: "2024-07-26 03:14:10.686446"
latest: "1.4.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-hcaexplorer"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.4.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-hcaexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hcaexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hcaexplorer", "latest": {"1.4.0--r40hdfd78af_1": "sha256:1f5362e678984f236853cd128afd37c8e00589e949946d8ab5511cfb1a37a3db"}, "tags": {"1.4.0--r40hdfd78af_1": "sha256:1f5362e678984f236853cd128afd37c8e00589e949946d8ab5511cfb1a37a3db"}, "docker": "quay.io/biocontainers/bioconductor-hcaexplorer", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hcaexplorer.
shpc-registry automated BioContainers addition for bioconductor-hcaexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hcaexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hcaexplorer:1.4.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hcaexplorer/1.4.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-hcaexplorer/1.4.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hcaexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hcaexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hcaexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hcaexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hcaexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hcaexplorer-inspect-deffile:

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