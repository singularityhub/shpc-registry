---
layout: container
name:  "quay.io/biocontainers/r-statvisual"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-statvisual/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-statvisual/container.yaml"
updated_at: "2024-08-15 03:19:57.587398"
latest: "1.2.1--r43h3342da4_5"
container_url: "https://biocontainers.pro/tools/r-statvisual"
aliases:
 - "pandoc"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.2.1--r41h3342da4_3"
 - "1.2.1--r42h3342da4_4"
 - "1.2.1--r43h3342da4_5"
description: "shpc-registry automated BioContainers addition for r-statvisual"
config: {"url": "https://biocontainers.pro/tools/r-statvisual", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-statvisual", "latest": {"1.2.1--r43h3342da4_5": "sha256:ab4cf7a4ed50a51e15c45268766077b46283fce2597a5aeec4068f9910169b3c"}, "tags": {"1.2.1--r41h3342da4_3": "sha256:0e4ce10e44f6b84478f7741885d6e1a8d393c1814972c0cc3319b5edfd878d30", "1.2.1--r42h3342da4_4": "sha256:3bbf07b24a98f99246030d18fd5a98a416a15c7afb0aa9d0f84fe4599fc6f6d9", "1.2.1--r43h3342da4_5": "sha256:ab4cf7a4ed50a51e15c45268766077b46283fce2597a5aeec4068f9910169b3c"}, "docker": "quay.io/biocontainers/r-statvisual", "aliases": {"pandoc": "/usr/local/bin/pandoc", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-statvisual.
shpc-registry automated BioContainers addition for r-statvisual
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-statvisual
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-statvisual:1.2.1--r43h3342da4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-statvisual/1.2.1--r43h3342da4_5
$ module help quay.io/biocontainers/r-statvisual/1.2.1--r43h3342da4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-statvisual-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-statvisual-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-statvisual-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-statvisual-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-statvisual-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-statvisual-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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