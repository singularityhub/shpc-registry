---
layout: container
name:  "quay.io/biocontainers/bioconductor-sbmlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sbmlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sbmlr/container.yaml"
updated_at: "2025-01-14 03:08:33.366140"
latest: "2.2.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sbmlr"

versions:
 - "1.90.0--r41hdfd78af_0"
 - "1.94.0--r42hdfd78af_0"
 - "1.96.0--r43hdfd78af_0"
 - "1.98.0--r43hdfd78af_0"
 - "2.2.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sbmlr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sbmlr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sbmlr", "latest": {"2.2.0--r44hdfd78af_0": "sha256:1754641a98040b8c4e3e3696a74adff311aac8ab239828dcd26b247458384870"}, "tags": {"1.90.0--r41hdfd78af_0": "sha256:eb93515af3b47eff2234eccb3d9fba9d4bcf360f07460977a4676153297f2f68", "1.94.0--r42hdfd78af_0": "sha256:5de73562eeaa0faa8c43d843afd01cec968f8b62e2eac28f7808154f05105251", "1.96.0--r43hdfd78af_0": "sha256:8f8b876b99038ac1405998529587f2a9918d7d13a31cb1ee98674a93c9682ceb", "1.98.0--r43hdfd78af_0": "sha256:d72e3763a97e8f8ba507f5b9ad1042c0f337e6fc1cffb051a10fb813f32b0f84", "2.2.0--r44hdfd78af_0": "sha256:1754641a98040b8c4e3e3696a74adff311aac8ab239828dcd26b247458384870"}, "docker": "quay.io/biocontainers/bioconductor-sbmlr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sbmlr.
shpc-registry automated BioContainers addition for bioconductor-sbmlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sbmlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sbmlr:2.2.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sbmlr/2.2.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sbmlr/2.2.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sbmlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sbmlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sbmlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sbmlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sbmlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sbmlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sbmlr

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