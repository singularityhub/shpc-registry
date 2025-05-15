---
layout: container
name:  "quay.io/biocontainers/bioconductor-conclus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-conclus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-conclus/container.yaml"
updated_at: "2025-05-15 03:46:38.857923"
latest: "1.5.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-conclus"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.5.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-conclus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-conclus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-conclus", "latest": {"1.5.0--r42hdfd78af_0": "sha256:73af3304cc62d7f5c4f586e56b8342f568c24bec824d58df9e83456c89b0ccff"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ca1956fe362079abeabb65b9d8e8db5304ff5202f29d49f6fe92391c49386c8b", "1.5.0--r42hdfd78af_0": "sha256:73af3304cc62d7f5c4f586e56b8342f568c24bec824d58df9e83456c89b0ccff"}, "docker": "quay.io/biocontainers/bioconductor-conclus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-conclus.
shpc-registry automated BioContainers addition for bioconductor-conclus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-conclus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-conclus:1.5.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-conclus/1.5.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-conclus/1.5.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-conclus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-conclus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-conclus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-conclus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-conclus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-conclus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-conclus

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