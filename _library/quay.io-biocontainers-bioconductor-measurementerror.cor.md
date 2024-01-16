---
layout: container
name:  "quay.io/biocontainers/bioconductor-measurementerror.cor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-measurementerror.cor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-measurementerror.cor/container.yaml"
updated_at: "2024-01-16 02:36:58.583142"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-measurementerror.cor"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-measurementerror.cor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-measurementerror.cor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-measurementerror.cor", "latest": {"1.74.0--r43hdfd78af_0": "sha256:189717aeec823e6f313597e1b52d5db2d2f793423dbac9d1724861183d882283"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:e73e8cfc007d43f29c6cff440db323ab24ebebfe13067043d99bf0b5a7ec88e7", "1.70.0--r42hdfd78af_0": "sha256:7e05bd98b815c05b2d888b3e9fb6756702b7dadbe75b9989e6d1b56cb5138599", "1.72.0--r43hdfd78af_0": "sha256:f7dfcb733d91644648e3419042ad4853658451c4b0d7b889a5760ca99336ac43", "1.74.0--r43hdfd78af_0": "sha256:189717aeec823e6f313597e1b52d5db2d2f793423dbac9d1724861183d882283"}, "docker": "quay.io/biocontainers/bioconductor-measurementerror.cor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-measurementerror.cor.
shpc-registry automated BioContainers addition for bioconductor-measurementerror.cor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-measurementerror.cor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-measurementerror.cor:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-measurementerror.cor/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-measurementerror.cor/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-measurementerror.cor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-measurementerror.cor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-measurementerror.cor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-measurementerror.cor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-measurementerror.cor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-measurementerror.cor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-measurementerror.cor

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