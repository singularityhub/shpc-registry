---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaeditr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaeditr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaeditr/container.yaml"
updated_at: "2025-08-24 04:12:14.238129"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaeditr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaeditr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaeditr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaeditr", "latest": {"1.16.0--r44hdfd78af_0": "sha256:9dd41d712298b241014eb76a55b617fbb8e13105dad46b303cbb34d845941c9e"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:07f0bb7cf5ed2ea0ff5b17f904625e079c3c93788adfbd73f0753d3007b7ec12", "1.8.0--r42hdfd78af_0": "sha256:1bfa53ba3dc69a0e5ccd4542f2c09384974d36037cfe21cd81e8ec98d070409d", "1.10.0--r43hdfd78af_0": "sha256:13eb0ce6a44b36ff303f0a4288066c93b6a02746158663cc92eeec912ab63dd7", "1.12.0--r43hdfd78af_0": "sha256:bc8ba8eeabc402f5503a9965e46c16d6c83740a869761f4a29b64720ce3232b3", "1.16.0--r44hdfd78af_0": "sha256:9dd41d712298b241014eb76a55b617fbb8e13105dad46b303cbb34d845941c9e"}, "docker": "quay.io/biocontainers/bioconductor-rnaeditr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaeditr.
shpc-registry automated BioContainers addition for bioconductor-rnaeditr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaeditr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaeditr:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaeditr/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaeditr/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaeditr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaeditr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaeditr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaeditr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaeditr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaeditr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnaeditr

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