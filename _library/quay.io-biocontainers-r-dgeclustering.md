---
layout: container
name:  "quay.io/biocontainers/r-dgeclustering"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-dgeclustering/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-dgeclustering/container.yaml"
updated_at: "2023-11-20 02:36:13.883988"
latest: "0.1.0--r43h9ee0642_5"
container_url: "https://biocontainers.pro/tools/r-dgeclustering"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.0--r41h9ee0642_3"
 - "0.1.0--r42h9ee0642_4"
 - "0.1.0--r43h9ee0642_5"
description: "shpc-registry automated BioContainers addition for r-dgeclustering"
config: {"url": "https://biocontainers.pro/tools/r-dgeclustering", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-dgeclustering", "latest": {"0.1.0--r43h9ee0642_5": "sha256:48330bf1120d8c8252677dfbb16f5a657fc980b3e62e26d3c8a1e87ec0f9712b"}, "tags": {"0.1.0--r41h9ee0642_3": "sha256:020e9b02c94baf801be9f2ac0b9638491aa791619d3e04dbab933691f2455a41", "0.1.0--r42h9ee0642_4": "sha256:ff0ead51a414f413793d70b24d9fe247d585b5f655919c3a0394fb94c3a67d71", "0.1.0--r43h9ee0642_5": "sha256:48330bf1120d8c8252677dfbb16f5a657fc980b3e62e26d3c8a1e87ec0f9712b"}, "docker": "quay.io/biocontainers/r-dgeclustering", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-dgeclustering.
shpc-registry automated BioContainers addition for r-dgeclustering
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-dgeclustering
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-dgeclustering:0.1.0--r43h9ee0642_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-dgeclustering/0.1.0--r43h9ee0642_5
$ module help quay.io/biocontainers/r-dgeclustering/0.1.0--r43h9ee0642_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-dgeclustering-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-dgeclustering-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-dgeclustering-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-dgeclustering-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-dgeclustering-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-dgeclustering-inspect-deffile:

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