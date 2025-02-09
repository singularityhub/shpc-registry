---
layout: container
name:  "quay.io/biocontainers/bioconductor-cghcall"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cghcall/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cghcall/container.yaml"
updated_at: "2025-02-09 03:24:11.204870"
latest: "2.68.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cghcall"

versions:
 - "2.56.0--r41hdfd78af_0"
 - "2.60.0--r42hdfd78af_0"
 - "2.62.0--r43hdfd78af_0"
 - "2.64.0--r43hdfd78af_0"
 - "2.68.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cghcall"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cghcall", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cghcall", "latest": {"2.68.0--r44hdfd78af_0": "sha256:4c25d7c89a5b4f68d8f9b8a378ce08fa500e761c2e1d4e940fda8e35dee48558"}, "tags": {"2.56.0--r41hdfd78af_0": "sha256:f42f60a56d1a997c248082dd5f4ff7458afa8b826f76b58360e4f05d540d0a60", "2.60.0--r42hdfd78af_0": "sha256:66bec1d88f37f8a1d6b155938fa60319f41b077c5f70a5ebc9f49808d77a8d5c", "2.62.0--r43hdfd78af_0": "sha256:dd844bb3936342ea6000c434c4ab6a5152487f02d96806bb4a843eda570c0262", "2.64.0--r43hdfd78af_0": "sha256:3ff59a6ae952869fa36831063c49b738ad6378858c3e6c52bfe6a848e15f9e53", "2.68.0--r44hdfd78af_0": "sha256:4c25d7c89a5b4f68d8f9b8a378ce08fa500e761c2e1d4e940fda8e35dee48558"}, "docker": "quay.io/biocontainers/bioconductor-cghcall"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cghcall.
shpc-registry automated BioContainers addition for bioconductor-cghcall
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cghcall
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cghcall:2.68.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cghcall/2.68.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cghcall/2.68.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cghcall-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghcall-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cghcall-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cghcall-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cghcall-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cghcall-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cghcall

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