---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirnatap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirnatap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirnatap/container.yaml"
updated_at: "2023-07-19 04:01:24.358467"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirnatap"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirnatap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirnatap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirnatap", "latest": {"1.34.0--r43hdfd78af_0": "sha256:f1fdc9d4ca51ba13a19d5837c750bf3562a9c80f5bbf73c73c2c2e640ed5ae9e"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:070e11125a851ef06357f8dbf37c15ccde3b50b640452104233129a11f232b68", "1.32.0--r42hdfd78af_0": "sha256:7612e15f88e3c1d3e1c56012b16fe733110c0ac12b09d12778c2fbae5ed7e1a2", "1.34.0--r43hdfd78af_0": "sha256:f1fdc9d4ca51ba13a19d5837c750bf3562a9c80f5bbf73c73c2c2e640ed5ae9e"}, "docker": "quay.io/biocontainers/bioconductor-mirnatap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirnatap.
shpc-registry automated BioContainers addition for bioconductor-mirnatap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnatap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirnatap:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirnatap/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirnatap/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirnatap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnatap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirnatap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirnatap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirnatap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirnatap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirnatap

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