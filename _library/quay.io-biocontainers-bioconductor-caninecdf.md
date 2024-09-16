---
layout: container
name:  "quay.io/biocontainers/bioconductor-caninecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-caninecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-caninecdf/container.yaml"
updated_at: "2024-09-16 03:53:35.458800"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-caninecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-caninecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-caninecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-caninecdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:9cbc2ed4c1d756d96d4ba05e10c2553722a8930219234a380d52b9ce588cd4d8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:34abe7c01ebbd58b3d4a3d1da829363484cfbb179b374aa9654d449fdc81afd7", "2.18.0--r42hdfd78af_10": "sha256:82d503021c0c7dd39ca48ee84a7a8fc96983af8365c5fc00da802143260d2c0f", "2.18.0--r43hdfd78af_11": "sha256:f62b2126aecc4b42f90c4a960f44790fdfcc0803a29aea063bfa0c07e5b1c68a", "2.18.0--r43hdfd78af_12": "sha256:9cbc2ed4c1d756d96d4ba05e10c2553722a8930219234a380d52b9ce588cd4d8"}, "docker": "quay.io/biocontainers/bioconductor-caninecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-caninecdf.
shpc-registry automated BioContainers addition for bioconductor-caninecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-caninecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-caninecdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-caninecdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-caninecdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-caninecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caninecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caninecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-caninecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-caninecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-caninecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-caninecdf

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