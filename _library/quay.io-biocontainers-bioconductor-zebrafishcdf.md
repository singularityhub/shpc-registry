---
layout: container
name:  "quay.io/biocontainers/bioconductor-zebrafishcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zebrafishcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zebrafishcdf/container.yaml"
updated_at: "2023-11-23 03:05:08.565620"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-zebrafishcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-zebrafishcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zebrafishcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zebrafishcdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:102137aa6dbd2c5836efbe799d80db8d5180145cbb39d0ebfda55934470f3e82"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:6ea1c24d7d09ad974b4f31ace4a366db106748e1df940a2b11576fbb4bfb839f", "2.18.0--r42hdfd78af_10": "sha256:8b6116e4128ffffca336ea3b8e691acd8e4519436b719b6e3c4ddff338815bfa", "2.18.0--r43hdfd78af_11": "sha256:102137aa6dbd2c5836efbe799d80db8d5180145cbb39d0ebfda55934470f3e82"}, "docker": "quay.io/biocontainers/bioconductor-zebrafishcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zebrafishcdf.
shpc-registry automated BioContainers addition for bioconductor-zebrafishcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafishcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafishcdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zebrafishcdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-zebrafishcdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zebrafishcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafishcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafishcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zebrafishcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zebrafishcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zebrafishcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-zebrafishcdf

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