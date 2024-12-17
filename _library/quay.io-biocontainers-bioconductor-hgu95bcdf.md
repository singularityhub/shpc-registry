---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95bcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95bcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95bcdf/container.yaml"
updated_at: "2024-12-17 03:40:26.698939"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95bcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95bcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95bcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95bcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:705bd909e2345466732399639ecab6837e4f7cfc5007742e2af5b86295c022f6"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d9c8d31f953c41593a730b694d64c828f5f4ab0447d44fafa0588e474032175d", "2.18.0--r42hdfd78af_10": "sha256:bfbb8af4f4e7f1daf82004f8014b78a64be9a3b16eaf78c6517dd53d9313a25e", "2.18.0--r43hdfd78af_11": "sha256:784448c206035b014d85d4b7cc41973da47654ab8ea41903d927a2069628a9c1", "2.18.0--r43hdfd78af_12": "sha256:705bd909e2345466732399639ecab6837e4f7cfc5007742e2af5b86295c022f6"}, "docker": "quay.io/biocontainers/bioconductor-hgu95bcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95bcdf.
shpc-registry automated BioContainers addition for bioconductor-hgu95bcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95bcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95bcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95bcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hgu95bcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95bcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95bcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95bcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95bcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95bcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95bcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95bcdf

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