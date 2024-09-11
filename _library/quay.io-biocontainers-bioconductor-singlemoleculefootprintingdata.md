---
layout: container
name:  "quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata/container.yaml"
updated_at: "2024-09-11 03:08:31.198627"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-singlemoleculefootprintingdata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-singlemoleculefootprintingdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singlemoleculefootprintingdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singlemoleculefootprintingdata", "latest": {"1.10.0--r43hdfd78af_0": "sha256:ffb69bf22a2549f79c62840834f74ed31ef2f47ed5dba4012b00322368c62648"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:e6fcc53cd4e92fdc413c734a97d5b1c6a10a17b1b72b5825c79d3d1098cf1d67", "1.6.0--r42hdfd78af_0": "sha256:9811759805f1ffe161899080e0b203b57cf27cf47710191ef6f749c39d4b30c1", "1.8.0--r43hdfd78af_0": "sha256:9ce406bfe248863f813e9bd8ad2ad47811a2e0a1bbe0b4a5194c64f035ffc968", "1.10.0--r43hdfd78af_0": "sha256:ffb69bf22a2549f79c62840834f74ed31ef2f47ed5dba4012b00322368c62648"}, "docker": "quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata.
shpc-registry automated BioContainers addition for bioconductor-singlemoleculefootprintingdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-singlemoleculefootprintingdata/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singlemoleculefootprintingdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlemoleculefootprintingdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlemoleculefootprintingdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singlemoleculefootprintingdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singlemoleculefootprintingdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singlemoleculefootprintingdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-singlemoleculefootprintingdata

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