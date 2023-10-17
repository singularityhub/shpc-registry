---
layout: container
name:  "quay.io/biocontainers/r-phyext2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-phyext2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-phyext2/container.yaml"
updated_at: "2023-10-17 02:52:10.565939"
latest: "0.0.4--r43h3121a25_9"
container_url: "https://biocontainers.pro/tools/r-phyext2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.0.4--r41h3121a25_7"
 - "0.0.4--r42h3121a25_8"
 - "0.0.4--r43h3121a25_9"
description: "shpc-registry automated BioContainers addition for r-phyext2"
config: {"url": "https://biocontainers.pro/tools/r-phyext2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-phyext2", "latest": {"0.0.4--r43h3121a25_9": "sha256:be4a5b194cf5453f4899726934e669f25879fe445f0dbfcf9911c3c3c2e277df"}, "tags": {"0.0.4--r41h3121a25_7": "sha256:e3a4cdb3b721e45cf16869f21b3013e623b3443b01c29f331353da7f873b964f", "0.0.4--r42h3121a25_8": "sha256:9f08ca5c254e5f4376424d58a1d2778f1364573bca38c087c2bace8f9526ac2f", "0.0.4--r43h3121a25_9": "sha256:be4a5b194cf5453f4899726934e669f25879fe445f0dbfcf9911c3c3c2e277df"}, "docker": "quay.io/biocontainers/r-phyext2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-phyext2.
shpc-registry automated BioContainers addition for r-phyext2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-phyext2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-phyext2:0.0.4--r43h3121a25_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-phyext2/0.0.4--r43h3121a25_9
$ module help quay.io/biocontainers/r-phyext2/0.0.4--r43h3121a25_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-phyext2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-phyext2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-phyext2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-phyext2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-phyext2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-phyext2-inspect-deffile:

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