---
layout: container
name:  "quay.io/biocontainers/requests-mock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/requests-mock/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/requests-mock/container.yaml"
updated_at: "2022-10-27 00:57:31.128585"
latest: "1.0.0--py27_1"
container_url: "https://biocontainers.pro/tools/requests-mock"

versions:
 - "1.0.0--py27_1"
description: "shpc-registry automated BioContainers addition for requests-mock"
config: {"url": "https://biocontainers.pro/tools/requests-mock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for requests-mock", "latest": {"1.0.0--py27_1": "sha256:e2734501a87e60615c245f9b5c3508ecb19e7708adf63512431897f76229e01f"}, "tags": {"1.0.0--py27_1": "sha256:e2734501a87e60615c245f9b5c3508ecb19e7708adf63512431897f76229e01f"}, "docker": "quay.io/biocontainers/requests-mock"}
---

This module is a singularity container wrapper for quay.io/biocontainers/requests-mock.
shpc-registry automated BioContainers addition for requests-mock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/requests-mock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/requests-mock:1.0.0--py27_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/requests-mock/1.0.0--py27_1
$ module help quay.io/biocontainers/requests-mock/1.0.0--py27_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### requests-mock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### requests-mock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### requests-mock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### requests-mock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### requests-mock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### requests-mock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### requests-mock

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