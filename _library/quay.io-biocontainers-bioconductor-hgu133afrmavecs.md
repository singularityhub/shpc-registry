---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133afrmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133afrmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133afrmavecs/container.yaml"
updated_at: "2025-12-14 04:30:47.141837"
latest: "1.5.0--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133afrmavecs"

versions:
 - "1.5.0--r41hdfd78af_9"
 - "1.5.0--r42hdfd78af_11"
 - "1.5.0--r43hdfd78af_12"
 - "1.5.0--r43hdfd78af_13"
 - "1.5.0--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133afrmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133afrmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133afrmavecs", "latest": {"1.5.0--r44hdfd78af_14": "sha256:019710bdf64226d15f403e48db46c9ef091c0adb89612e5a55a1170119b57b76"}, "tags": {"1.5.0--r41hdfd78af_9": "sha256:246a6c4bb47f3c2d7a89c3f5155ed8362aa7f46ee7e96ad006559d0f51b2645d", "1.5.0--r42hdfd78af_11": "sha256:07e1e8931aa3fa094232cbc0a5167adbf08570ab563eb277dc5776737b387d53", "1.5.0--r43hdfd78af_12": "sha256:bd7156b192d13066acac41b65adec677e213c5f0b1b2b8cdd24fac9e6b1fab25", "1.5.0--r43hdfd78af_13": "sha256:1b9640528b5097dcfb2154d6fa4fd8ef99ff64007e89762646eaf2d072b0463b", "1.5.0--r44hdfd78af_14": "sha256:019710bdf64226d15f403e48db46c9ef091c0adb89612e5a55a1170119b57b76"}, "docker": "quay.io/biocontainers/bioconductor-hgu133afrmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133afrmavecs.
shpc-registry automated BioContainers addition for bioconductor-hgu133afrmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133afrmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133afrmavecs:1.5.0--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133afrmavecs/1.5.0--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-hgu133afrmavecs/1.5.0--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133afrmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133afrmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133afrmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133afrmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133afrmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133afrmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133afrmavecs

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