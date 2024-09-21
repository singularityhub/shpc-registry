---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanotubes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanotubes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanotubes/container.yaml"
updated_at: "2024-09-21 02:48:16.831456"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanotubes"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanotubes"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanotubes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanotubes", "latest": {"1.18.0--r43hdfd78af_0": "sha256:b7b06c4619dcfec1d53b92bf3ad900d32775629231e7a19f194351c1a1d9a350"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:787cbddfc0a4a20cf31d8a187eb490fd0223e12fff70a21d42bacd9a11f298f8", "1.14.0--r42hdfd78af_0": "sha256:d1518d5c642a55b6a06008f7d7cc72373ace0d4442c181a925b8341feb57d881", "1.10.0--r41hdfd78af_1": "sha256:4dffc6a0bd600ca030f286ccb71b351dc45e6433af8d74b9cb2af533e8973460", "1.16.0--r43hdfd78af_0": "sha256:e44828d03fe36705987cb29802a19bb454b1732a4a89f90a20148f2a9f1b7e86", "1.18.0--r43hdfd78af_0": "sha256:b7b06c4619dcfec1d53b92bf3ad900d32775629231e7a19f194351c1a1d9a350"}, "docker": "quay.io/biocontainers/bioconductor-nanotubes", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanotubes.
shpc-registry automated BioContainers addition for bioconductor-nanotubes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanotubes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanotubes:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanotubes/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nanotubes/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanotubes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanotubes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanotubes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanotubes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanotubes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanotubes-inspect-deffile:

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