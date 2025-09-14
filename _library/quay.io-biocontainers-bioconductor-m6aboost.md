---
layout: container
name:  "quay.io/biocontainers/bioconductor-m6aboost"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-m6aboost/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-m6aboost/container.yaml"
updated_at: "2025-09-14 03:21:33.311892"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-m6aboost"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-m6aboost"
config: {"url": "https://biocontainers.pro/tools/bioconductor-m6aboost", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-m6aboost", "latest": {"1.12.0--r44hdfd78af_0": "sha256:bea821b07521c3ca014c3c4059e7e647946d9d857ee93a6e2496cc6f9f1a98ef"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:c207c9e91ffa77913eca3ed5ae8b579395457036d25f056b637e1f57320adbec", "1.4.0--r42hdfd78af_0": "sha256:c9bc284334c96ae674b45b680ce42de9b878634f03e211d487c3dff2aa50bc58", "1.6.0--r43hdfd78af_0": "sha256:b74e84792e8d83f5de30b9b123909ce3bfe77b157d676ca202222e5a0d54ac0c", "1.8.0--r43hdfd78af_0": "sha256:09bee7bd89f259f60e28836f86e2147946b0b8bbc3a996d044362b31711f48cd", "1.12.0--r44hdfd78af_0": "sha256:bea821b07521c3ca014c3c4059e7e647946d9d857ee93a6e2496cc6f9f1a98ef"}, "docker": "quay.io/biocontainers/bioconductor-m6aboost"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-m6aboost.
shpc-registry automated BioContainers addition for bioconductor-m6aboost
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-m6aboost
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-m6aboost:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-m6aboost/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-m6aboost/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-m6aboost-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m6aboost-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m6aboost-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-m6aboost-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-m6aboost-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-m6aboost-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-m6aboost

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