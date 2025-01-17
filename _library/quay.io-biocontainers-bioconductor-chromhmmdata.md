---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromhmmdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromhmmdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromhmmdata/container.yaml"
updated_at: "2025-01-17 03:23:18.970943"
latest: "0.99.2--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-chromhmmdata"

versions:
 - "0.99.2--r41hdfd78af_1"
 - "0.99.2--r42hdfd78af_2"
 - "0.99.2--r43hdfd78af_3"
 - "0.99.2--r43hdfd78af_4"
 - "0.99.2--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-chromhmmdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromhmmdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromhmmdata", "latest": {"0.99.2--r44hdfd78af_5": "sha256:c9cb4c726b40766891dc0a259855accebcb5498d712fdf0c7a2c6f0c3cfd64bd"}, "tags": {"0.99.2--r41hdfd78af_1": "sha256:98c45eb5ce87ad8dd746a4a9746ff879cfe19c04eb40ba5ba8f2f8487a330935", "0.99.2--r42hdfd78af_2": "sha256:eac3189592a2d044eae1bde58b69a127791d494db13c4ad9bd8297046644bbfd", "0.99.2--r43hdfd78af_3": "sha256:8f4726701c890ca27870bbf9e68f45026fca289bbc2cd1ea33eea92a24a6c90a", "0.99.2--r43hdfd78af_4": "sha256:fba9023cf9bb5dafa8a9aca74ec94e13a71a1239985902fcbdb99fc529700350", "0.99.2--r44hdfd78af_5": "sha256:c9cb4c726b40766891dc0a259855accebcb5498d712fdf0c7a2c6f0c3cfd64bd"}, "docker": "quay.io/biocontainers/bioconductor-chromhmmdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromhmmdata.
shpc-registry automated BioContainers addition for bioconductor-chromhmmdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromhmmdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromhmmdata:0.99.2--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromhmmdata/0.99.2--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-chromhmmdata/0.99.2--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromhmmdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromhmmdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromhmmdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromhmmdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromhmmdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromhmmdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chromhmmdata

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