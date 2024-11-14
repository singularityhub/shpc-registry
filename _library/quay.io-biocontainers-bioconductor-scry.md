---
layout: container
name:  "quay.io/biocontainers/bioconductor-scry"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scry/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scry/container.yaml"
updated_at: "2024-11-14 04:25:21.811917"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scry"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scry"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scry", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scry", "latest": {"1.14.0--r43hdfd78af_0": "sha256:34b37838c514a4fefcd6a59fcaf959d0511820e4aa395c63a0bbc726ac80f2eb"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:b5d08ac130b03338bfea30b929b648e73fb1b2fa28e663b83b3a485b52c9a830", "1.10.0--r42hdfd78af_0": "sha256:df05cfd1e0fa0576522c65d49294321108e726d256a70aed545491839c59e5ba", "1.12.0--r43hdfd78af_0": "sha256:bbea409a0d7a2d2292baeeb554a9df94d930084f600e169ed5dfa5a085e206b4", "1.14.0--r43hdfd78af_0": "sha256:34b37838c514a4fefcd6a59fcaf959d0511820e4aa395c63a0bbc726ac80f2eb"}, "docker": "quay.io/biocontainers/bioconductor-scry"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scry.
shpc-registry automated BioContainers addition for bioconductor-scry
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scry
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scry:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scry/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scry/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scry-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scry-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scry-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scry-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scry-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scry-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scry

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