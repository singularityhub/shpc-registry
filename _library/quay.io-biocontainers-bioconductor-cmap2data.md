---
layout: container
name:  "quay.io/biocontainers/bioconductor-cmap2data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cmap2data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cmap2data/container.yaml"
updated_at: "2025-04-22 03:49:14.792309"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cmap2data"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cmap2data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cmap2data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cmap2data", "latest": {"1.42.0--r44hdfd78af_0": "sha256:29b0c0b24086e5917d3479485d91556adbe017cf3b5e068df5b83222279d40a7"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:87fe33287ab75d5d775053d5e3a71d3ff45c343507b60b85afd1e71434922f49", "1.34.0--r42hdfd78af_0": "sha256:98a2f5201ec1a1f296ef163e32c78bc556b0c0aa3bc7618f2e0b4ccdc9d711bd", "1.33.0--r42hdfd78af_0": "sha256:cccf8e18aead9d2dc917d64dfce001bb26d20303f3c45ab488b73c131d6385eb", "1.36.0--r43hdfd78af_0": "sha256:1a9189b598bb72811dd97e29c9867008cf4c98ff0284802b300280f3b4e1e928", "1.38.0--r43hdfd78af_0": "sha256:f2f47df2c8af9a8d359cfc2290c503e8c00c680215888b22367d6e1ecbb17a3a", "1.42.0--r44hdfd78af_0": "sha256:29b0c0b24086e5917d3479485d91556adbe017cf3b5e068df5b83222279d40a7"}, "docker": "quay.io/biocontainers/bioconductor-cmap2data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cmap2data.
shpc-registry automated BioContainers addition for bioconductor-cmap2data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap2data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cmap2data:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cmap2data/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cmap2data/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cmap2data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cmap2data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cmap2data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cmap2data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cmap2data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cmap2data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cmap2data

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