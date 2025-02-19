---
layout: container
name:  "quay.io/biocontainers/bioconductor-davidtiling"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-davidtiling/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-davidtiling/container.yaml"
updated_at: "2025-02-19 03:36:03.517464"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-davidtiling"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-davidtiling"
config: {"url": "https://biocontainers.pro/tools/bioconductor-davidtiling", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-davidtiling", "latest": {"1.46.0--r44hdfd78af_0": "sha256:22e05449819361bd7ce6cd716b674955ce4b52eff601a33e342969de51b39822"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:53ef5fbc1f5c9873845c2d176ad37f42cea17c770a1481d6932eefb92ca17ebf", "1.38.0--r42hdfd78af_0": "sha256:9ee3b4d06b9bdd313817661b250190f73350084f1994f0cdb9492aed16ea7adb", "1.40.0--r43hdfd78af_0": "sha256:5ae7c433d7b4f69fdc2834be900e44255794f9e1db14a20cf705ae37e7821608", "1.42.0--r43hdfd78af_0": "sha256:eed3dc41cb42006e44a00c5d7dfeead589445cf931817d0c0ce5d36b50319afa", "1.46.0--r44hdfd78af_0": "sha256:22e05449819361bd7ce6cd716b674955ce4b52eff601a33e342969de51b39822"}, "docker": "quay.io/biocontainers/bioconductor-davidtiling"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-davidtiling.
shpc-registry automated BioContainers addition for bioconductor-davidtiling
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-davidtiling
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-davidtiling:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-davidtiling/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-davidtiling/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-davidtiling-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-davidtiling-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-davidtiling-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-davidtiling-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-davidtiling-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-davidtiling-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-davidtiling

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