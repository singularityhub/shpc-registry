---
layout: container
name:  "quay.io/biocontainers/bioconductor-tomatocdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tomatocdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tomatocdf/container.yaml"
updated_at: "2023-03-21 03:15:36.230437"
latest: "2.18.0--r42hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-tomatocdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-tomatocdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tomatocdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tomatocdf", "latest": {"2.18.0--r42hdfd78af_11": "sha256:40ebe57be02a629870eccea7b188a4d0f90837b702ee563d1012e9919d2a22a0"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:50957b3f809421f6d9719b93aae2aab8b17aefa3443ce48207d4854755760c3b", "2.18.0--r41hdfd78af_10": "sha256:3b0104ca907d8a7639002c6e446f27cef8ad6d5b5287d0e786485540b64c6dbb", "2.18.0--r42hdfd78af_11": "sha256:40ebe57be02a629870eccea7b188a4d0f90837b702ee563d1012e9919d2a22a0"}, "docker": "quay.io/biocontainers/bioconductor-tomatocdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tomatocdf.
shpc-registry automated BioContainers addition for bioconductor-tomatocdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tomatocdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tomatocdf:2.18.0--r42hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tomatocdf/2.18.0--r42hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-tomatocdf/2.18.0--r42hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tomatocdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomatocdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tomatocdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tomatocdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tomatocdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tomatocdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tomatocdf

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