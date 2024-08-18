---
layout: container
name:  "quay.io/biocontainers/bioconductor-lymphoseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lymphoseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lymphoseq/container.yaml"
updated_at: "2024-08-18 03:23:28.908056"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lymphoseq"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lymphoseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lymphoseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lymphoseq", "latest": {"1.30.0--r43hdfd78af_0": "sha256:7c0c640412653580dc4e88980582f5fe1bb6b209572ec8fcc37bff9a6ec05ea7"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:2ffc4e4b0075dad7b827bdecc5f00cc378fc7afd711fa3b7ee8a568f8af648c6", "1.26.0--r42hdfd78af_0": "sha256:b47be6be0d1c98dc47d665375f1896b46256930c01703de0faded78ea3b460d8", "1.28.0--r43hdfd78af_0": "sha256:2f5fcda154bf77043a5cc7f9c7d931365989ca5c543eb58b2a8188fb332b7bd7", "1.30.0--r43hdfd78af_0": "sha256:7c0c640412653580dc4e88980582f5fe1bb6b209572ec8fcc37bff9a6ec05ea7"}, "docker": "quay.io/biocontainers/bioconductor-lymphoseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lymphoseq.
shpc-registry automated BioContainers addition for bioconductor-lymphoseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lymphoseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lymphoseq:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lymphoseq/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lymphoseq/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lymphoseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lymphoseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lymphoseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lymphoseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lymphoseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lymphoseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lymphoseq

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