---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsar/container.yaml"
updated_at: "2023-10-09 02:34:04.911295"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsar"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsar", "latest": {"1.34.0--r43hdfd78af_0": "sha256:81aee8ce902a037d3ab9b5de4ac751ca7a9aa0824d73098d4800c208067d5436"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:d4abdf74d9216462a903abf1ecc4822dc18b0dadcfc5a917f198c31a5a1d2feb", "1.32.0--r42hdfd78af_0": "sha256:7cd240095dc8e9f66c6a8b2529d29c2f42848a015b4f8a869cac64c5e2a9f9bf", "1.34.0--r43hdfd78af_0": "sha256:81aee8ce902a037d3ab9b5de4ac751ca7a9aa0824d73098d4800c208067d5436"}, "docker": "quay.io/biocontainers/bioconductor-gsar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsar.
shpc-registry automated BioContainers addition for bioconductor-gsar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsar:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsar/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsar/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsar

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