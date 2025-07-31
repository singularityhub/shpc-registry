---
layout: container
name:  "quay.io/biocontainers/bioconductor-mvoutdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mvoutdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mvoutdata/container.yaml"
updated_at: "2025-07-31 11:17:09.480839"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mvoutdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mvoutdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mvoutdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mvoutdata", "latest": {"1.42.0--r44hdfd78af_0": "sha256:25e9f2ed58a55e24ddc824d50f481c1831194316dbc48575e3bdcb2f0c1a5dee"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:67aa02490eb54dfe8714f49d7763a3dab0c38fc36b2ed7dd8f25d44801fa8be4", "1.34.0--r42hdfd78af_0": "sha256:be131b41f7bb9517a91f944df370675153bd67d9596c55031978e7cc3e5b93cd", "1.36.0--r43hdfd78af_0": "sha256:e5fe6840de1f449651f7c38b69b3a03502545d9c0e26d68d8686fa95ac8a5a56", "1.38.0--r43hdfd78af_0": "sha256:7c04406cffcf13cac9d2db3956be0d8ab12024375a1509a3fa253d1a9a338f4a", "1.42.0--r44hdfd78af_0": "sha256:25e9f2ed58a55e24ddc824d50f481c1831194316dbc48575e3bdcb2f0c1a5dee"}, "docker": "quay.io/biocontainers/bioconductor-mvoutdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mvoutdata.
shpc-registry automated BioContainers addition for bioconductor-mvoutdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mvoutdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mvoutdata:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mvoutdata/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mvoutdata/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mvoutdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvoutdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mvoutdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mvoutdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mvoutdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mvoutdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mvoutdata

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