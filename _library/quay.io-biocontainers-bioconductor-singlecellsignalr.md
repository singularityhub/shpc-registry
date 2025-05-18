---
layout: container
name:  "quay.io/biocontainers/bioconductor-singlecellsignalr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singlecellsignalr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singlecellsignalr/container.yaml"
updated_at: "2025-05-18 03:33:39.563801"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-singlecellsignalr"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-singlecellsignalr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singlecellsignalr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singlecellsignalr", "latest": {"1.18.0--r44hdfd78af_0": "sha256:c1eb270090752e745d97bd9ad5ab0be546a34e22539fcfdbcbc43d43e9e42259"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:28c73bdec67d2f64237f307f5a0fa88816aec095473498fae170bb74e6a4a9d8", "1.10.0--r42hdfd78af_0": "sha256:1e4e1344bdabfaa761c876f12ce178a727bbc4799247a25d7bb06b983fb01e46", "1.12.0--r43hdfd78af_0": "sha256:f468f205c7b81caa46391b5628a213a39714b2b1556c11bcb5b3803d525b0ae6", "1.14.0--r43hdfd78af_0": "sha256:5df0f2473f41fc78050a7511cf59337ee19b62425bb842b97d328c735883b2db", "1.18.0--r44hdfd78af_0": "sha256:c1eb270090752e745d97bd9ad5ab0be546a34e22539fcfdbcbc43d43e9e42259"}, "docker": "quay.io/biocontainers/bioconductor-singlecellsignalr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singlecellsignalr.
shpc-registry automated BioContainers addition for bioconductor-singlecellsignalr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellsignalr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellsignalr:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singlecellsignalr/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-singlecellsignalr/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singlecellsignalr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellsignalr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellsignalr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singlecellsignalr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singlecellsignalr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singlecellsignalr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-singlecellsignalr

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