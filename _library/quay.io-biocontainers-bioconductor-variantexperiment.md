---
layout: container
name:  "quay.io/biocontainers/bioconductor-variantexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-variantexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-variantexperiment/container.yaml"
updated_at: "2024-01-03 02:31:09.594428"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-variantexperiment"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-variantexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-variantexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-variantexperiment", "latest": {"1.16.0--r43hdfd78af_0": "sha256:5277f0bc6779079754268980fd60f232c895bdf943b83556647874985d8a2692"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:a598f71ae9cabedcf89a48fb4ed6b6162d60124b1ceb99ba9c9bb3c9adc174e6", "1.12.0--r42hdfd78af_0": "sha256:a806aeac45dac2db05e5f83b890f92c6c300d88e1505f36e6928b6cb4b198408", "1.14.0--r43hdfd78af_0": "sha256:6c847894828d5b37e6856d35d2518fae6e5aa3558a31f8c40a5905f1d13b00db", "1.16.0--r43hdfd78af_0": "sha256:5277f0bc6779079754268980fd60f232c895bdf943b83556647874985d8a2692"}, "docker": "quay.io/biocontainers/bioconductor-variantexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-variantexperiment.
shpc-registry automated BioContainers addition for bioconductor-variantexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-variantexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-variantexperiment:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-variantexperiment/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-variantexperiment/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-variantexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-variantexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-variantexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-variantexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-variantexperiment

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