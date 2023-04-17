---
layout: container
name:  "quay.io/biocontainers/bioconductor-soybeancdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-soybeancdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-soybeancdf/container.yaml"
updated_at: "2023-04-17 03:20:01.356820"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-soybeancdf"

versions:
 - "2.18.0--r41hdfd78af_8"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-soybeancdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-soybeancdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-soybeancdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:f92f0120a63cfe36441277df73af063c7dcc0d383693067a836bb58f7acd4e97"}, "tags": {"2.18.0--r41hdfd78af_8": "sha256:4180bce2b2c7475bfd8de2911569086df966f72e62d4225c07f6cc63de3a7417", "2.18.0--r42hdfd78af_10": "sha256:f92f0120a63cfe36441277df73af063c7dcc0d383693067a836bb58f7acd4e97"}, "docker": "quay.io/biocontainers/bioconductor-soybeancdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-soybeancdf.
shpc-registry automated BioContainers addition for bioconductor-soybeancdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-soybeancdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-soybeancdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-soybeancdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-soybeancdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-soybeancdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-soybeancdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-soybeancdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-soybeancdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-soybeancdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-soybeancdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-soybeancdf

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