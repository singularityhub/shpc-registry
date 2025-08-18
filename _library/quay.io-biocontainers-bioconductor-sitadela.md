---
layout: container
name:  "quay.io/biocontainers/bioconductor-sitadela"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sitadela/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sitadela/container.yaml"
updated_at: "2025-08-18 03:49:42.547033"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sitadela"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sitadela"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sitadela", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sitadela", "latest": {"1.14.0--r44hdfd78af_0": "sha256:94abab61d7500d61cf66fd09b014208a8ce12477edcd892a5c440eca4d0d53bf"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:bed7b011d5ae9013114bb5b06d03fc3705f1bec61e71df957b5716c85a4f98af", "1.6.0--r42hdfd78af_0": "sha256:3cfdcb4028db4e8d4cc607e738a2f777edec9fd39f1f21ff499dabe511bf7a1f", "1.8.0--r43hdfd78af_0": "sha256:ab8385cb8ae6df33723e89129a0cbdc96f4333e7c9fdbb39e273ded62cf3be6f", "1.10.0--r43hdfd78af_0": "sha256:d12bf6acd004a029041d5ada915d66b88aabd97782d33e70206bdb1c38192b5e", "1.14.0--r44hdfd78af_0": "sha256:94abab61d7500d61cf66fd09b014208a8ce12477edcd892a5c440eca4d0d53bf"}, "docker": "quay.io/biocontainers/bioconductor-sitadela"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sitadela.
shpc-registry automated BioContainers addition for bioconductor-sitadela
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sitadela
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sitadela:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sitadela/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sitadela/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sitadela-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sitadela-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sitadela-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sitadela-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sitadela-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sitadela-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sitadela

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