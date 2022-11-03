---
layout: container
name:  "quay.io/biocontainers/bioconductor-stepnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stepnorm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stepnorm/container.yaml"
updated_at: "2022-11-03 01:04:10.181142"
latest: "1.66.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stepnorm"

versions:
 - "1.66.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stepnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stepnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stepnorm", "latest": {"1.66.0--r41hdfd78af_0": "sha256:93aed3590b31c82bfca249f73a0b9bcae8d10d662f5346965eeddd916a4d9f10"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:93aed3590b31c82bfca249f73a0b9bcae8d10d662f5346965eeddd916a4d9f10"}, "docker": "quay.io/biocontainers/bioconductor-stepnorm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stepnorm.
shpc-registry automated BioContainers addition for bioconductor-stepnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stepnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stepnorm:1.66.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stepnorm/1.66.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stepnorm/1.66.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stepnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stepnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stepnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stepnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stepnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stepnorm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-stepnorm

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