---
layout: container
name:  "quay.io/biocontainers/r-cimpl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cimpl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cimpl/container.yaml"
updated_at: "2024-11-25 04:07:19.063635"
latest: "1.1--r43h9ee0642_6"
container_url: "https://biocontainers.pro/tools/r-cimpl"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1--r41h9ee0642_4"
 - "1.1--r42h9ee0642_5"
 - "1.1--r43h9ee0642_6"
description: "shpc-registry automated BioContainers addition for r-cimpl"
config: {"url": "https://biocontainers.pro/tools/r-cimpl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-cimpl", "latest": {"1.1--r43h9ee0642_6": "sha256:e209e028d600bea4e8caa8e249ca64434dfc96094cb3fbc056974f407a4ac840"}, "tags": {"1.1--r41h9ee0642_4": "sha256:9630c2b9c7022f200bf7cfedf29fc3ae924c08dc412c798570373b26229bfd2e", "1.1--r42h9ee0642_5": "sha256:8db684729fb7e1e933807af223f34cc89ef79c73865e977a6d8acb0c09e675c2", "1.1--r43h9ee0642_6": "sha256:e209e028d600bea4e8caa8e249ca64434dfc96094cb3fbc056974f407a4ac840"}, "docker": "quay.io/biocontainers/r-cimpl", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cimpl.
shpc-registry automated BioContainers addition for r-cimpl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cimpl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cimpl:1.1--r43h9ee0642_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cimpl/1.1--r43h9ee0642_6
$ module help quay.io/biocontainers/r-cimpl/1.1--r43h9ee0642_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cimpl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cimpl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cimpl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cimpl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cimpl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cimpl-inspect-deffile:

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