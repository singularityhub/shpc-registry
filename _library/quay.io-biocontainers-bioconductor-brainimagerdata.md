---
layout: container
name:  "quay.io/biocontainers/bioconductor-brainimagerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-brainimagerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-brainimagerdata/container.yaml"
updated_at: "2023-07-04 03:37:06.927779"
latest: "1.12.0--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-brainimagerdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-brainimagerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-brainimagerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-brainimagerdata", "latest": {"1.12.0--r41hdfd78af_1": "sha256:213c2599deaf6b28cfdb694932e8a05b1c2229cfa62f4b58822ae0a2bc5abf01"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:f2127099c9617964f635628cc143764d57aac19a459f3ac174f2bfc58c91e7dc", "1.12.0--r41hdfd78af_1": "sha256:213c2599deaf6b28cfdb694932e8a05b1c2229cfa62f4b58822ae0a2bc5abf01", "1.10.0--r41hdfd78af_0": "sha256:436ab6d9bd7cd8fb6b88e7dcd12e7e8ca29a79889f906e3ff05ca29727e79b16"}, "docker": "quay.io/biocontainers/bioconductor-brainimagerdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-brainimagerdata.
shpc-registry automated BioContainers addition for bioconductor-brainimagerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-brainimagerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-brainimagerdata:1.12.0--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-brainimagerdata/1.12.0--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-brainimagerdata/1.12.0--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-brainimagerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brainimagerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-brainimagerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-brainimagerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-brainimagerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-brainimagerdata-inspect-deffile:

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