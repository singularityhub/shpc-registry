---
layout: container
name:  "quay.io/biocontainers/bioconductor-trigger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trigger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trigger/container.yaml"
updated_at: "2024-03-04 03:29:00.088520"
latest: "1.48.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trigger"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.46.0--r43ha9d7317_0"
 - "1.48.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trigger"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trigger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trigger", "latest": {"1.48.0--r43ha9d7317_0": "sha256:2c13479c37f3389d88ed68dcc5d05168981b0aeffa77c1d09a31932f0b2a373c"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:43f15acd399c9b5919813c61d4f11d4190534957f8d1909ce4b58b6742900a47", "1.44.0--r42hc0cfd56_0": "sha256:24ef3294fac15c100751fc374d213af3d8c348d9bda4e855e8dd36fd3d351f9b", "1.44.0--r42ha9d7317_1": "sha256:4c3c78b78cbe33b156ca2a11ec30d1cdc15e183a43b5439e0dec4f0969a33eca", "1.46.0--r43ha9d7317_0": "sha256:469956ff48c878ac344b35309a9cf2981beb59785ecf12c591a1d4e604f82054", "1.48.0--r43ha9d7317_0": "sha256:2c13479c37f3389d88ed68dcc5d05168981b0aeffa77c1d09a31932f0b2a373c"}, "docker": "quay.io/biocontainers/bioconductor-trigger"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trigger.
shpc-registry automated BioContainers addition for bioconductor-trigger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trigger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trigger:1.48.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trigger/1.48.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-trigger/1.48.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trigger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trigger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trigger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trigger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trigger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trigger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trigger

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