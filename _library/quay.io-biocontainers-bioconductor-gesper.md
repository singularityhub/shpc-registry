---
layout: container
name:  "quay.io/biocontainers/bioconductor-gesper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gesper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gesper/container.yaml"
updated_at: "2023-07-15 03:42:12.582078"
latest: "1.30.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gesper"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gesper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gesper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gesper", "latest": {"1.30.0--r42hdfd78af_0": "sha256:45d2f7bda3eb3a1bdf79e0805bdcd7a9e3da6a453fc9502f89eb459895d434ed"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:dae89c09e791c32763813f5f6834aa8344ead1cdb40dc0acc99620dac5a5616d", "1.30.0--r42hdfd78af_0": "sha256:45d2f7bda3eb3a1bdf79e0805bdcd7a9e3da6a453fc9502f89eb459895d434ed"}, "docker": "quay.io/biocontainers/bioconductor-gesper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gesper.
shpc-registry automated BioContainers addition for bioconductor-gesper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gesper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gesper:1.30.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gesper/1.30.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gesper/1.30.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gesper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gesper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gesper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gesper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gesper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gesper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gesper

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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