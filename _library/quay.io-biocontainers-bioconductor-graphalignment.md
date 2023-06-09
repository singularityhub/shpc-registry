---
layout: container
name:  "quay.io/biocontainers/bioconductor-graphalignment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graphalignment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graphalignment/container.yaml"
updated_at: "2023-06-09 03:44:08.997900"
latest: "1.62.0--r42ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-graphalignment"

versions:
 - "1.58.0--r41hc0cfd56_2"
 - "1.62.0--r42hc0cfd56_0"
 - "1.62.0--r42ha9d7317_2"
description: "shpc-registry automated BioContainers addition for bioconductor-graphalignment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graphalignment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graphalignment", "latest": {"1.62.0--r42ha9d7317_2": "sha256:aaf500dbe4daf5c97539b3ce0be93ea5e372b567e121231d22ef082ab85e2324"}, "tags": {"1.58.0--r41hc0cfd56_2": "sha256:ed5eb1a24c546d2d320f780dbeb3c1762fa76e8f48149abd42e61a36c39ec824", "1.62.0--r42hc0cfd56_0": "sha256:ef71b7f4f622167a8fd11bd61160c5659c8eb1334e9ad221851d22714439e151", "1.62.0--r42ha9d7317_2": "sha256:aaf500dbe4daf5c97539b3ce0be93ea5e372b567e121231d22ef082ab85e2324"}, "docker": "quay.io/biocontainers/bioconductor-graphalignment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graphalignment.
shpc-registry automated BioContainers addition for bioconductor-graphalignment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graphalignment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graphalignment:1.62.0--r42ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graphalignment/1.62.0--r42ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-graphalignment/1.62.0--r42ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graphalignment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphalignment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphalignment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graphalignment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graphalignment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graphalignment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-graphalignment

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