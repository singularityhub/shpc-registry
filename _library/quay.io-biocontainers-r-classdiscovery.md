---
layout: container
name:  "quay.io/biocontainers/r-classdiscovery"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-classdiscovery/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-classdiscovery/container.yaml"
updated_at: "2024-06-18 02:54:44.826554"
latest: "3.4.5--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-classdiscovery"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.4.0--r41h3342da4_0"
 - "3.4.0--r42h3342da4_1"
 - "3.4.0--r43h3342da4_2"
 - "3.4.5--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-classdiscovery"
config: {"url": "https://biocontainers.pro/tools/r-classdiscovery", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-classdiscovery", "latest": {"3.4.5--r43h3342da4_0": "sha256:42340931ca0a71e2f8fbb16ad606423f72ab58928b57a37f816866a0b1fd78d5"}, "tags": {"3.4.0--r41h3342da4_0": "sha256:a55868ca243ef85b5d9c3afe6e79febb26b879863b9535b0f71e65d8be43874a", "3.4.0--r42h3342da4_1": "sha256:717dd78d96e9253c229e7604a510da64bc92a324cdcb9c594d6aecf3534875a9", "3.4.0--r43h3342da4_2": "sha256:88bd70df7b6e318aabecd09725182e6b34b508c07e295b22b6fe2201a557f9f8", "3.4.5--r43h3342da4_0": "sha256:42340931ca0a71e2f8fbb16ad606423f72ab58928b57a37f816866a0b1fd78d5"}, "docker": "quay.io/biocontainers/r-classdiscovery", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-classdiscovery.
shpc-registry automated BioContainers addition for r-classdiscovery
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-classdiscovery
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-classdiscovery:3.4.5--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-classdiscovery/3.4.5--r43h3342da4_0
$ module help quay.io/biocontainers/r-classdiscovery/3.4.5--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-classdiscovery-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-classdiscovery-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-classdiscovery-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-classdiscovery-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-classdiscovery-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-classdiscovery-inspect-deffile:

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