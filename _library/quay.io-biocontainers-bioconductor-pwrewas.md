---
layout: container
name:  "quay.io/biocontainers/bioconductor-pwrewas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pwrewas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pwrewas/container.yaml"
updated_at: "2025-01-30 03:53:06.956040"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pwrewas"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pwrewas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pwrewas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pwrewas", "latest": {"1.14.0--r43hdfd78af_0": "sha256:847ca6f5ad0e20490933b0ffa6abbee5a210a8c87494c797494071295dec2ec5"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:5a4688f9912ef48f6ae30bccf301f3b2edc66c20bc43afe6032acfc2d32ccbc9", "1.12.0--r42hdfd78af_0": "sha256:893c35159108294d30af3d96d26d67f60764f6e75d0e536ee9310486cdf979d8", "1.14.0--r43hdfd78af_0": "sha256:847ca6f5ad0e20490933b0ffa6abbee5a210a8c87494c797494071295dec2ec5"}, "docker": "quay.io/biocontainers/bioconductor-pwrewas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pwrewas.
shpc-registry automated BioContainers addition for bioconductor-pwrewas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pwrewas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pwrewas:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pwrewas/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pwrewas/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pwrewas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwrewas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwrewas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pwrewas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pwrewas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pwrewas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pwrewas

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