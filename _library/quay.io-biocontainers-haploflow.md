---
layout: container
name:  "quay.io/biocontainers/haploflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haploflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haploflow/container.yaml"
updated_at: "2024-09-19 03:00:40.551317"
latest: "1.0--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/haploflow"
aliases:
 - "haploflow"
versions:
 - "1.0--h2df963e_1"
 - "1.0--h376f1d3_3"
 - "1.0--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for haploflow"
config: {"url": "https://biocontainers.pro/tools/haploflow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haploflow", "latest": {"1.0--h4ac6f70_4": "sha256:4f391df9c456c0846304e7a15254e695358e45a76d910f3f66a1b7b11e30e0f1"}, "tags": {"1.0--h2df963e_1": "sha256:1485875272bbe20ce2f994e9b5c161469eefb57bcf4b7526a4bdacfdc2940c2f", "1.0--h376f1d3_3": "sha256:ba2526a0e30a199fd5a793ce3b8f3ebdad1621037afe71ffcf385859d82b6220", "1.0--h4ac6f70_4": "sha256:4f391df9c456c0846304e7a15254e695358e45a76d910f3f66a1b7b11e30e0f1"}, "docker": "quay.io/biocontainers/haploflow", "aliases": {"haploflow": "/usr/local/bin/haploflow"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haploflow.
shpc-registry automated BioContainers addition for haploflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haploflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haploflow:1.0--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haploflow/1.0--h4ac6f70_4
$ module help quay.io/biocontainers/haploflow/1.0--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haploflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haploflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haploflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haploflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haploflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haploflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haploflow

```bash
$ singularity exec <container> /usr/local/bin/haploflow
$ podman run --it --rm --entrypoint /usr/local/bin/haploflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haploflow   -v ${PWD} -w ${PWD} <container> -c " $@"
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