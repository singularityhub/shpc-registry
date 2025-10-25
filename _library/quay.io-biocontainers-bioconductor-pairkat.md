---
layout: container
name:  "quay.io/biocontainers/bioconductor-pairkat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pairkat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pairkat/container.yaml"
updated_at: "2025-10-25 03:35:50.236713"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pairkat"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pairkat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pairkat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pairkat", "latest": {"1.12.0--r44hdfd78af_0": "sha256:c84c913a6d9f4060631c3477235f628d9b96f79fb25bebf2374fb8a091986b28"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:bf9c91369c979729eb350ea84c5ccf2435587760b78929dd9f8926fb6b66df22", "1.4.0--r42hdfd78af_0": "sha256:736ca2afd0158279f28cadb48173feb5ac75e1cd78c05ea6c0abc523add24569", "1.6.0--r43hdfd78af_0": "sha256:ae8f43a1211b974c13c1ba3569878a4f38e9d583b19f91fddbd446c2a901c2d7", "1.8.0--r43hdfd78af_0": "sha256:d98eb45ffdf3cd8feb985119ad544d12fd991195900028b7828017d731b08a89", "1.12.0--r44hdfd78af_0": "sha256:c84c913a6d9f4060631c3477235f628d9b96f79fb25bebf2374fb8a091986b28"}, "docker": "quay.io/biocontainers/bioconductor-pairkat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pairkat.
shpc-registry automated BioContainers addition for bioconductor-pairkat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pairkat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pairkat:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pairkat/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pairkat/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pairkat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pairkat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pairkat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pairkat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pairkat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pairkat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pairkat

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