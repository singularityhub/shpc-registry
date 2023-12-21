---
layout: container
name:  "quay.io/biocontainers/r-codedepends"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-codedepends/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-codedepends/container.yaml"
updated_at: "2023-12-21 02:29:42.199939"
latest: "0.6.5--r43h3342da4_4"
container_url: "https://biocontainers.pro/tools/r-codedepends"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.6.5--r41h3342da4_2"
 - "0.6.5--r42h3342da4_3"
 - "0.6.5--r43h3342da4_4"
description: "shpc-registry automated BioContainers addition for r-codedepends"
config: {"url": "https://biocontainers.pro/tools/r-codedepends", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-codedepends", "latest": {"0.6.5--r43h3342da4_4": "sha256:40c6b7e7230556e0d34f6fc67dfe5f31822c28f71b82ab293486fa9ce2bd6098"}, "tags": {"0.6.5--r41h3342da4_2": "sha256:ed3a17cddd3f3c638dd7df5bb0263f0327ef562c9342ee60f7197b9839def380", "0.6.5--r42h3342da4_3": "sha256:5fce6007fd1f9da8a9e2779b583d8036b254d5f72abc57d675cd20ea1e8bf38d", "0.6.5--r43h3342da4_4": "sha256:40c6b7e7230556e0d34f6fc67dfe5f31822c28f71b82ab293486fa9ce2bd6098"}, "docker": "quay.io/biocontainers/r-codedepends", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-codedepends.
shpc-registry automated BioContainers addition for r-codedepends
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-codedepends
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-codedepends:0.6.5--r43h3342da4_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-codedepends/0.6.5--r43h3342da4_4
$ module help quay.io/biocontainers/r-codedepends/0.6.5--r43h3342da4_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-codedepends-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-codedepends-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-codedepends-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-codedepends-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-codedepends-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-codedepends-inspect-deffile:

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