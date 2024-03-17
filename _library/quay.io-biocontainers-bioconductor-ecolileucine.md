---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecolileucine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecolileucine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecolileucine/container.yaml"
updated_at: "2024-03-17 02:49:41.809021"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ecolileucine"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ecolileucine"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecolileucine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecolileucine", "latest": {"1.42.0--r43hdfd78af_0": "sha256:ebbedd97ac3c5f2a879290a29d1ada25aa363c0c3fb3d84bc06b0c31f0d5d393"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:d759edf24ececc2b9796e3abd6b7dc9a1740e03341174a22090650d1d04de085", "1.38.0--r42hdfd78af_0": "sha256:61e782fba15a6ccf3a068eea72ec3c9f6ea4caaebc1f3112f3c1ccff75223feb", "1.40.0--r43hdfd78af_0": "sha256:9f56dc94b70a5ad972200609be8f3695661f8b1aad5a6406a001fd28e87ec003", "1.42.0--r43hdfd78af_0": "sha256:ebbedd97ac3c5f2a879290a29d1ada25aa363c0c3fb3d84bc06b0c31f0d5d393"}, "docker": "quay.io/biocontainers/bioconductor-ecolileucine"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecolileucine.
shpc-registry automated BioContainers addition for bioconductor-ecolileucine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolileucine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolileucine:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecolileucine/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ecolileucine/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecolileucine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolileucine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolileucine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecolileucine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecolileucine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecolileucine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ecolileucine

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