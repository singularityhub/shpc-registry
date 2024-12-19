---
layout: container
name:  "quay.io/biocontainers/r-swamp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-swamp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-swamp/container.yaml"
updated_at: "2024-12-19 04:52:48.151120"
latest: "1.5.1--r43h3121a25_5"
container_url: "https://biocontainers.pro/tools/r-swamp"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.5.1--r41h3121a25_3"
 - "1.5.1--r42h3121a25_4"
 - "1.5.1--r43h3121a25_5"
description: "shpc-registry automated BioContainers addition for r-swamp"
config: {"url": "https://biocontainers.pro/tools/r-swamp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-swamp", "latest": {"1.5.1--r43h3121a25_5": "sha256:c92fec8b6d572e2b96d497d0201b93ff7f2f65194af429ca6829141fcaab7ec6"}, "tags": {"1.5.1--r41h3121a25_3": "sha256:e007bdc921ff01e3b86bab3875c1855a426c622a4f1f9be86b279e7d1a2fc0fe", "1.5.1--r42h3121a25_4": "sha256:92bb73f8051a4139ff7bb6f45cb605a278791a03464027dcebb1386fc6f5f73a", "1.5.1--r43h3121a25_5": "sha256:c92fec8b6d572e2b96d497d0201b93ff7f2f65194af429ca6829141fcaab7ec6"}, "docker": "quay.io/biocontainers/r-swamp", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-swamp.
shpc-registry automated BioContainers addition for r-swamp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-swamp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-swamp:1.5.1--r43h3121a25_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-swamp/1.5.1--r43h3121a25_5
$ module help quay.io/biocontainers/r-swamp/1.5.1--r43h3121a25_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-swamp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-swamp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-swamp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-swamp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-swamp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-swamp-inspect-deffile:

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