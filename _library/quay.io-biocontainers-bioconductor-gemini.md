---
layout: container
name:  "quay.io/biocontainers/bioconductor-gemini"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gemini/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gemini/container.yaml"
updated_at: "2025-02-13 03:02:55.213094"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gemini"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gemini"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gemini", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gemini", "latest": {"1.20.0--r44hdfd78af_0": "sha256:e383384a01b6dab2ed11b4c77cd3fd181a3af8f43aefbd3ccc8379c01f4b3023"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:07cf68c9fce8a2476caa77fc95e9352dd02374aca8875dda51e046e137ab2f3c", "1.12.0--r42hdfd78af_0": "sha256:3e8673a1245ba51ae9a6be613d9ceb590a832296cc91c414749cade124f99c79", "1.14.0--r43hdfd78af_0": "sha256:c5d332765c0a60e1ca825eed5fadbf004f8336dba28e1a604d1e12ca67ec2f49", "1.16.0--r43hdfd78af_0": "sha256:0989a88f0248fe469be6fe068b4e7976711cad688ab32037cdc5c7410547c5af", "1.20.0--r44hdfd78af_0": "sha256:e383384a01b6dab2ed11b4c77cd3fd181a3af8f43aefbd3ccc8379c01f4b3023"}, "docker": "quay.io/biocontainers/bioconductor-gemini"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gemini.
shpc-registry automated BioContainers addition for bioconductor-gemini
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gemini
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gemini:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gemini/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gemini/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gemini-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gemini-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gemini-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gemini-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gemini-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gemini-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gemini

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