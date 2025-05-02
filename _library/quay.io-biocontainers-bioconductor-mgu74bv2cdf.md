---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74bv2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74bv2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74bv2cdf/container.yaml"
updated_at: "2025-05-02 03:40:56.671682"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74bv2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74bv2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:3ba67db7e0dba36bf0f768a05879266778726641627d6752696f1f3ca19ee910"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:62d509813e80c62dcad177448d94c50ee7b4786ff6de5cfb5691b9cfe21a6095", "2.18.0--r42hdfd78af_10": "sha256:29e008c36b2aac24f51c030be431566dd409d7c1f4feebf706ecfda912dd74e3", "2.18.0--r43hdfd78af_11": "sha256:70e397ff05a596eb5eebb7e2233aa13e3418970f3b7b4e109736f7975955c8c7", "2.18.0--r43hdfd78af_12": "sha256:8c2e2a9ea638ae4e43c9620350128f8d91b68ccae5127aaf097bc00f57b169a0", "2.18.0--r44hdfd78af_13": "sha256:3ba67db7e0dba36bf0f768a05879266778726641627d6752696f1f3ca19ee910"}, "docker": "quay.io/biocontainers/bioconductor-mgu74bv2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74bv2cdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74bv2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74bv2cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mgu74bv2cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74bv2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74bv2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74bv2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74bv2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74bv2cdf

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