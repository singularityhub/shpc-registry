---
layout: container
name:  "quay.io/biocontainers/bioconductor-methimpute"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methimpute/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methimpute/container.yaml"
updated_at: "2023-08-24 02:21:26.459344"
latest: "1.22.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methimpute"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methimpute"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methimpute", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methimpute", "latest": {"1.22.0--r43hf17093f_0": "sha256:dd4bfbe10054a5b8d8cb89fa275299a04235e232e65fca6c0794bf03a7b4faa8"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:aeb40641b65ca7d4a9b19448aebbd676166ddab976624fd2064bed89bd0dd575", "1.20.0--r42hc247a5b_0": "sha256:157fca3dedc6cb6cece4249135eb8745c8b8f3ad663aa927999280fda91c2b0d", "1.16.0--r41hc247a5b_2": "sha256:4d8bcb2e71163ca5429a2292c36a3cdcb1641a7b03d1d436456e439297b24612", "1.14.0--r41h399db7b_0": "sha256:f365a55744ce5672b5f6c5f79aeabdd0cb1ae77bba410a48a14da06fa3919dea", "1.12.0--r40h399db7b_1": "sha256:139bb3dd5514932304c5f5dca53aa25f47d4475561bb39abaee81392099ea30b", "1.10.0--r40h5f743cb_0": "sha256:ee061cf360ba05307df9b2cc746c0fdc4f460e506dcbee41966c4bdd6c53e393", "1.20.0--r42hf17093f_1": "sha256:b079e2aa9107ee48fcabe9bc8ac2da8d225cf3bdebebf5b28635f8cca4a1d24f", "1.22.0--r43hf17093f_0": "sha256:dd4bfbe10054a5b8d8cb89fa275299a04235e232e65fca6c0794bf03a7b4faa8"}, "docker": "quay.io/biocontainers/bioconductor-methimpute", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methimpute.
shpc-registry automated BioContainers addition for bioconductor-methimpute
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methimpute
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methimpute:1.22.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methimpute/1.22.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-methimpute/1.22.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methimpute-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methimpute-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methimpute-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methimpute-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methimpute-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methimpute-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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