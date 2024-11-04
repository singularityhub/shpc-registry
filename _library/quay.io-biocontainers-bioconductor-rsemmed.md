---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsemmed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsemmed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsemmed/container.yaml"
updated_at: "2024-11-04 07:55:49.787241"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rsemmed"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rsemmed"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsemmed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsemmed", "latest": {"1.12.0--r43hdfd78af_0": "sha256:29c24b9794f1ddf5c0ac4c8b4aa281b0f4fc10faefb16af2e5b439831246eaab"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:b3d9766c560dcd8bc3d4247835d6c57ef843eaf0a563309c46cb6f99984d8a0f", "1.8.0--r42hdfd78af_0": "sha256:779438585d65401761d5c3a83ab20cf2df003bc065e365975454e45d34dfa344", "1.10.0--r43hdfd78af_0": "sha256:1e7c250ddb47309e154f64c90c1571c0c1828b348912fbba2a1a09774b736f8e", "1.12.0--r43hdfd78af_0": "sha256:29c24b9794f1ddf5c0ac4c8b4aa281b0f4fc10faefb16af2e5b439831246eaab"}, "docker": "quay.io/biocontainers/bioconductor-rsemmed"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsemmed.
shpc-registry automated BioContainers addition for bioconductor-rsemmed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsemmed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsemmed:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsemmed/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rsemmed/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsemmed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsemmed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsemmed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsemmed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsemmed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsemmed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsemmed

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