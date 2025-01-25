---
layout: container
name:  "quay.io/biocontainers/bioconductor-graph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graph/container.yaml"
updated_at: "2025-01-25 03:05:16.083563"
latest: "1.80.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-graph"

versions:
 - "1.72.0--r41hc0cfd56_2"
 - "1.76.0--r42hc0cfd56_0"
 - "1.76.0--r42ha9d7317_1"
 - "1.78.0--r43ha9d7317_0"
 - "1.80.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-graph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graph", "latest": {"1.80.0--r43ha9d7317_0": "sha256:aedfcd370a60d6db238a7ac50b2b5f42359feb33612e7597d958f71be2aacb44"}, "tags": {"1.72.0--r41hc0cfd56_2": "sha256:5e320e1d35fb3a3059143ef1e2df6304fad38a98433d23f31b6bec9334b2496a", "1.76.0--r42hc0cfd56_0": "sha256:79eaa561533169681599c654eb09be49e2727e15a1a5c83671c0e93345c906c1", "1.76.0--r42ha9d7317_1": "sha256:2502ac7ea40380c0f368120c92f1ce309f3b99ca9acb4b24ff712c0c98f6a0fc", "1.78.0--r43ha9d7317_0": "sha256:ea1a74ee13457f4a88f6aaaa30448f20812f0a250b78b68c522bc55a0d6d1492", "1.80.0--r43ha9d7317_0": "sha256:aedfcd370a60d6db238a7ac50b2b5f42359feb33612e7597d958f71be2aacb44"}, "docker": "quay.io/biocontainers/bioconductor-graph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graph.
shpc-registry automated BioContainers addition for bioconductor-graph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graph:1.80.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graph/1.80.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-graph/1.80.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-graph

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