---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowworkspacedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowworkspacedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowworkspacedata/container.yaml"
updated_at: "2024-05-10 02:50:02.780930"
latest: "3.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowworkspacedata"

versions:
 - "3.6.0--r41hdfd78af_1"
 - "3.9.0--r42hdfd78af_0"
 - "3.12.0--r43hdfd78af_0"
 - "3.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowworkspacedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowworkspacedata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowworkspacedata", "latest": {"3.14.0--r43hdfd78af_0": "sha256:6c8f11417fb59b4fabe5887e7e3fee8d6f8b1700d83ba389ceb67f9a7e2b0b85"}, "tags": {"3.6.0--r41hdfd78af_1": "sha256:4f8496f23f44f0f04c0c976ee16f9860df9cfeee70288f305741f8e69f4e4c4c", "3.9.0--r42hdfd78af_0": "sha256:34ba28c8388b3b26eb6da7889936328f325424e412079a49470247f965d4ca9f", "3.12.0--r43hdfd78af_0": "sha256:2e4519b3ac7dc8c8c98fac3b56409f6dab25e993859c4bb0e9127dbbb2a2db92", "3.14.0--r43hdfd78af_0": "sha256:6c8f11417fb59b4fabe5887e7e3fee8d6f8b1700d83ba389ceb67f9a7e2b0b85"}, "docker": "quay.io/biocontainers/bioconductor-flowworkspacedata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowworkspacedata.
shpc-registry automated BioContainers addition for bioconductor-flowworkspacedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowworkspacedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowworkspacedata:3.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowworkspacedata/3.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowworkspacedata/3.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowworkspacedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowworkspacedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowworkspacedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowworkspacedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowworkspacedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowworkspacedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowworkspacedata

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