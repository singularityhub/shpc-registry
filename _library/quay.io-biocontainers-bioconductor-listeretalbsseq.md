---
layout: container
name:  "quay.io/biocontainers/bioconductor-listeretalbsseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-listeretalbsseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-listeretalbsseq/container.yaml"
updated_at: "2024-04-01 03:04:16.027755"
latest: "1.32.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-listeretalbsseq"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-listeretalbsseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-listeretalbsseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-listeretalbsseq", "latest": {"1.32.1--r43hdfd78af_0": "sha256:4524c5da4d0d4f33cbb77ba17aee2ddac9afb52b84840cab47f6913e813806b5"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:89cb781434b29f1280f17252ffd9683fb3e71e82c78edda8845cfabe7b9c4a48", "1.30.0--r42hdfd78af_0": "sha256:626e8b4ca673b3cef39de166c8bb02097c3f76f3e5acc7382563eb4afc90dc24", "1.32.1--r43hdfd78af_0": "sha256:4524c5da4d0d4f33cbb77ba17aee2ddac9afb52b84840cab47f6913e813806b5"}, "docker": "quay.io/biocontainers/bioconductor-listeretalbsseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-listeretalbsseq.
shpc-registry automated BioContainers addition for bioconductor-listeretalbsseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-listeretalbsseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-listeretalbsseq:1.32.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-listeretalbsseq/1.32.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-listeretalbsseq/1.32.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-listeretalbsseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-listeretalbsseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-listeretalbsseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-listeretalbsseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-listeretalbsseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-listeretalbsseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-listeretalbsseq

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