---
layout: container
name:  "quay.io/biocontainers/tclap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tclap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tclap/container.yaml"
updated_at: "2024-01-16 02:59:09.417724"
latest: "1.2.1--h470a237_1"
container_url: "https://biocontainers.pro/tools/tclap"

versions:
 - "1.2.1--h470a237_1"
description: "shpc-registry automated BioContainers addition for tclap"
config: {"url": "https://biocontainers.pro/tools/tclap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tclap", "latest": {"1.2.1--h470a237_1": "sha256:a70df844302ac4c91f90cedd6bd0f3115a021705dbebf744b888b4144f837dea"}, "tags": {"1.2.1--h470a237_1": "sha256:a70df844302ac4c91f90cedd6bd0f3115a021705dbebf744b888b4144f837dea"}, "docker": "quay.io/biocontainers/tclap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/tclap.
shpc-registry automated BioContainers addition for tclap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tclap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tclap:1.2.1--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tclap/1.2.1--h470a237_1
$ module help quay.io/biocontainers/tclap/1.2.1--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tclap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tclap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tclap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tclap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tclap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tclap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tclap

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