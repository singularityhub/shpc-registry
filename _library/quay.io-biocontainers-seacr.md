---
layout: container
name:  "quay.io/biocontainers/seacr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seacr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seacr/container.yaml"
updated_at: "2023-05-18 03:10:14.863109"
latest: "1.3--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/seacr"
aliases:
 - "SEACR_1.3.R"
 - "SEACR_1.3.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.3--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for seacr"
config: {"url": "https://biocontainers.pro/tools/seacr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seacr", "latest": {"1.3--hdfd78af_2": "sha256:13d8be6125d96261a246c583948746cb5faf04703db5921944fc8e890dc92450"}, "tags": {"1.3--hdfd78af_2": "sha256:13d8be6125d96261a246c583948746cb5faf04703db5921944fc8e890dc92450"}, "docker": "quay.io/biocontainers/seacr", "aliases": {"SEACR_1.3.R": "/usr/local/bin/SEACR_1.3.R", "SEACR_1.3.sh": "/usr/local/bin/SEACR_1.3.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seacr.
shpc-registry automated BioContainers addition for seacr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seacr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seacr:1.3--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seacr/1.3--hdfd78af_2
$ module help quay.io/biocontainers/seacr/1.3--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seacr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seacr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seacr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seacr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seacr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seacr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SEACR_1.3.R

```bash
$ singularity exec <container> /usr/local/bin/SEACR_1.3.R
$ podman run --it --rm --entrypoint /usr/local/bin/SEACR_1.3.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SEACR_1.3.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SEACR_1.3.sh

```bash
$ singularity exec <container> /usr/local/bin/SEACR_1.3.sh
$ podman run --it --rm --entrypoint /usr/local/bin/SEACR_1.3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SEACR_1.3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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