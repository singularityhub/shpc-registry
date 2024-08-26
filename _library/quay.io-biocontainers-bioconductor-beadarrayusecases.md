---
layout: container
name:  "quay.io/biocontainers/bioconductor-beadarrayusecases"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-beadarrayusecases/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-beadarrayusecases/container.yaml"
updated_at: "2024-08-26 03:09:15.217545"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-beadarrayusecases"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-beadarrayusecases"
config: {"url": "https://biocontainers.pro/tools/bioconductor-beadarrayusecases", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-beadarrayusecases", "latest": {"1.40.0--r43hdfd78af_0": "sha256:5a2448b0e2afa3c8c65ddb44eb0a4a3c798c27e2e2e632754ad99d6f8fd7c34e"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:8f00c7527366e6417cf9d932b6a03cc9bc920106416320d2358bf824cce9aead", "1.36.0--r42hdfd78af_0": "sha256:1f74520fa54f2ced30da896e3c2070a023d6f053e50d4b947d52d5de93bfc802", "1.38.0--r43hdfd78af_0": "sha256:009394e65e38b1aaf50de36c8f2a7fa8449868d6b8d437836fd50ac7f02dab0a", "1.40.0--r43hdfd78af_0": "sha256:5a2448b0e2afa3c8c65ddb44eb0a4a3c798c27e2e2e632754ad99d6f8fd7c34e"}, "docker": "quay.io/biocontainers/bioconductor-beadarrayusecases"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-beadarrayusecases.
shpc-registry automated BioContainers addition for bioconductor-beadarrayusecases
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarrayusecases
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-beadarrayusecases:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-beadarrayusecases/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-beadarrayusecases/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-beadarrayusecases-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarrayusecases-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-beadarrayusecases-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-beadarrayusecases-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-beadarrayusecases-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-beadarrayusecases-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-beadarrayusecases

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