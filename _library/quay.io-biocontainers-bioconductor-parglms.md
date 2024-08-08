---
layout: container
name:  "quay.io/biocontainers/bioconductor-parglms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-parglms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-parglms/container.yaml"
updated_at: "2024-08-08 03:23:51.497224"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-parglms"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-parglms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-parglms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-parglms", "latest": {"1.34.0--r43hdfd78af_0": "sha256:f22e748615f019547bd5e2b16e793915c8ca22606aa8a735ff5ab59a5853e333"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:af0cad4bd815a9264b8d39a23f55551949ddfcc4089fbc7b2c8c21e11fc1349c", "1.30.0--r42hdfd78af_0": "sha256:1089fd3cddbb2b94eb040cabee86774f8f83f77b9a4a74defa7a744b55fe7a2a", "1.32.0--r43hdfd78af_0": "sha256:dc97577ea9afa1056d0cd098c457699a144e6e0927e6bd1e0f3254a43efafe95", "1.34.0--r43hdfd78af_0": "sha256:f22e748615f019547bd5e2b16e793915c8ca22606aa8a735ff5ab59a5853e333"}, "docker": "quay.io/biocontainers/bioconductor-parglms"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-parglms.
shpc-registry automated BioContainers addition for bioconductor-parglms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-parglms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-parglms:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-parglms/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-parglms/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-parglms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parglms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parglms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-parglms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-parglms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-parglms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-parglms

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