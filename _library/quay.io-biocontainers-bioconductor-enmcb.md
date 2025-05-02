---
layout: container
name:  "quay.io/biocontainers/bioconductor-enmcb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-enmcb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-enmcb/container.yaml"
updated_at: "2025-05-02 03:32:49.056187"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-enmcb"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-enmcb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-enmcb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-enmcb", "latest": {"1.18.0--r44hdfd78af_0": "sha256:0dccf32b2d6d543221bb89b146abcfa22601604b7599f52e8729bcbacaf2a9db"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:9aa68ac9e89033b1c2c5cecebe30e8fbb2df2a2cd9bdcaea4c92a635775c9907", "1.12.0--r43hdfd78af_0": "sha256:e7ad6b97f5c2d7c06d81be00f26d34997f3faebac3ecb04a97eb2d4ca5203572", "1.14.0--r43hdfd78af_0": "sha256:60742741cc3f235c22c8e5ce4c5c2a817d8665c475b8b524e6e2e8c5bd475991", "1.18.0--r44hdfd78af_0": "sha256:0dccf32b2d6d543221bb89b146abcfa22601604b7599f52e8729bcbacaf2a9db"}, "docker": "quay.io/biocontainers/bioconductor-enmcb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-enmcb.
shpc-registry automated BioContainers addition for bioconductor-enmcb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-enmcb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-enmcb:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-enmcb/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-enmcb/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-enmcb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enmcb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-enmcb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-enmcb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-enmcb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-enmcb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-enmcb

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