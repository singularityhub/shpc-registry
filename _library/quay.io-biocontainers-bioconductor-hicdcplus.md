---
layout: container
name:  "quay.io/biocontainers/bioconductor-hicdcplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hicdcplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hicdcplus/container.yaml"
updated_at: "2025-10-10 03:19:09.062919"
latest: "1.14.0--r44h77050f0_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hicdcplus"
aliases:
 - "glpsol"
versions:
 - "1.2.1--r41hc247a5b_1"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
 - "1.14.0--r44h77050f0_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hicdcplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hicdcplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hicdcplus", "latest": {"1.14.0--r44h77050f0_0": "sha256:5753f49530799cfd6be53591e122f57a3a76c6d95798f468ff7f764dcf0be8d1"}, "tags": {"1.2.1--r41hc247a5b_1": "sha256:1a07323f2db6f9fd4bf7ff0af0e04da476010810bbf9ca1ac25e125a6693f3fd", "1.6.0--r42hc247a5b_0": "sha256:2e4d62e6812c7619a1c4e202eba328880465a3785ba5fbf27b6b54aa5fccc7b6", "1.6.0--r42hf17093f_1": "sha256:689b796b7a5ee52a21323f46e9ba6ec29010981697703f0771d9bd1449ab58cd", "1.8.0--r43hf17093f_0": "sha256:f840a9f3e8f0e839a97ad9f81236477a210b6c46b89e6e600ef80e4f6e1b135e", "1.10.0--r43hf17093f_0": "sha256:5f3036b077c50aac66f103a29a6f2996959e9aa144ead61dc4cd498bc01866f8", "1.14.0--r44h77050f0_0": "sha256:5753f49530799cfd6be53591e122f57a3a76c6d95798f468ff7f764dcf0be8d1"}, "docker": "quay.io/biocontainers/bioconductor-hicdcplus", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hicdcplus.
shpc-registry automated BioContainers addition for bioconductor-hicdcplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hicdcplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hicdcplus:1.14.0--r44h77050f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hicdcplus/1.14.0--r44h77050f0_0
$ module help quay.io/biocontainers/bioconductor-hicdcplus/1.14.0--r44h77050f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hicdcplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicdcplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicdcplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hicdcplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hicdcplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hicdcplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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