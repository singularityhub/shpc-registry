---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatzie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatzie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatzie/container.yaml"
updated_at: "2024-04-13 02:24:54.515990"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatzie"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spatzie"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatzie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spatzie", "latest": {"1.8.0--r43hdfd78af_0": "sha256:9b8cca4d2ac1117fa8bc9ec3342c9e62d47e59f54ebad0124ea162f71e35e06e"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:2d2f9cb23fe013047c57fe798713509ac4e4190bb98c3ef6c3cd555f2c2b4062", "1.4.0--r42hdfd78af_0": "sha256:2cd6dfdae2cbbc36038fafad8607eea8e1a2eaaf6a4b339cb271ebc99ab1c80d", "1.6.0--r43hdfd78af_0": "sha256:f93e076de1f193686bf778367de0b558e17c3587412a7788be4fd1fe5168bf09", "1.8.0--r43hdfd78af_0": "sha256:9b8cca4d2ac1117fa8bc9ec3342c9e62d47e59f54ebad0124ea162f71e35e06e"}, "docker": "quay.io/biocontainers/bioconductor-spatzie"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatzie.
shpc-registry automated BioContainers addition for bioconductor-spatzie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatzie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatzie:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatzie/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatzie/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatzie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatzie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatzie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatzie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatzie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatzie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spatzie

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