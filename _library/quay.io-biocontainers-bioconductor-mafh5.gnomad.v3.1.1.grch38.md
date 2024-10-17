---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38/container.yaml"
updated_at: "2024-10-17 02:54:22.451344"
latest: "3.13.1--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-mafh5.gnomad.v3.1.1.grch38"

versions:
 - "3.13.0--r41hdfd78af_2"
 - "3.13.1--r42hdfd78af_0"
 - "3.13.1--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-mafh5.gnomad.v3.1.1.grch38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafh5.gnomad.v3.1.1.grch38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafh5.gnomad.v3.1.1.grch38", "latest": {"3.13.1--r43hdfd78af_1": "sha256:e6f109398d6ff1e5048860a03d22cef837704555bdffbe14f67ebdc169f68141"}, "tags": {"3.13.0--r41hdfd78af_2": "sha256:d5ac07c8b2de60d3918b33c9a4e02bd3f18c3c1c5a1d74b71297c26cebba3b1e", "3.13.1--r42hdfd78af_0": "sha256:776c44f88a17dc45e0617ec900e74af77187c709f17d2120eca69127961c8b81", "3.13.1--r43hdfd78af_1": "sha256:e6f109398d6ff1e5048860a03d22cef837704555bdffbe14f67ebdc169f68141"}, "docker": "quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38.
shpc-registry automated BioContainers addition for bioconductor-mafh5.gnomad.v3.1.1.grch38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38:3.13.1--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38/3.13.1--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-mafh5.gnomad.v3.1.1.grch38/3.13.1--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafh5.gnomad.v3.1.1.grch38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mafh5.gnomad.v3.1.1.grch38

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