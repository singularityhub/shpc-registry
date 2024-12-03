---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu19ksubacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu19ksubacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu19ksubacdf/container.yaml"
updated_at: "2024-12-03 03:24:45.441519"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mu19ksubacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mu19ksubacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu19ksubacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu19ksubacdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:4fe0d6e7caa4d23723888c36ff85c9e856ad5e6ffbe937a3861f1da2a0581e71"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:1b7d13a6f07be82c00c74a4c69dc0aa97f6c1560b59e089cc93d4e16cebf3c25", "2.18.0--r42hdfd78af_10": "sha256:e43592254e1829678637cbd19c9e74fc19d25adc3799ed928bfad434c6e8b3ce", "2.18.0--r43hdfd78af_11": "sha256:04a211fc5f81cd6f038f78577831cb02bd661b232ce5f4df5625cb949197685e", "2.18.0--r43hdfd78af_12": "sha256:4fe0d6e7caa4d23723888c36ff85c9e856ad5e6ffbe937a3861f1da2a0581e71"}, "docker": "quay.io/biocontainers/bioconductor-mu19ksubacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu19ksubacdf.
shpc-registry automated BioContainers addition for bioconductor-mu19ksubacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubacdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu19ksubacdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mu19ksubacdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu19ksubacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu19ksubacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu19ksubacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu19ksubacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu19ksubacdf

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