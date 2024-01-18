---
layout: container
name:  "quay.io/biocontainers/bioconductor-tigre"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tigre/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tigre/container.yaml"
updated_at: "2024-01-18 02:39:39.375641"
latest: "1.56.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tigre"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
 - "1.52.0--r42ha9d7317_1"
 - "1.54.0--r43ha9d7317_0"
 - "1.56.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tigre"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tigre", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tigre", "latest": {"1.56.0--r43ha9d7317_0": "sha256:d6a0a088776a42f57cb8d27ab4fcba96263a5da692f4b69d39265715aaccbe68"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:d5a6545f854cf45c0b49c7d80788010f2f22e65a39d94cc23af5937f9a64cddb", "1.52.0--r42hc0cfd56_0": "sha256:9344a6c099c0e9c4e6c723bd47b8980de1163d541ff918c9410f7642dd5231ad", "1.52.0--r42ha9d7317_1": "sha256:25e2e6219357b5a5532442550c52547e30d743ffc181148fed745088a879f510", "1.54.0--r43ha9d7317_0": "sha256:2284722f04491a837cda96bc1f0c4e4a93552303d1d5c7bfb86e5b5c572746d0", "1.56.0--r43ha9d7317_0": "sha256:d6a0a088776a42f57cb8d27ab4fcba96263a5da692f4b69d39265715aaccbe68"}, "docker": "quay.io/biocontainers/bioconductor-tigre"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tigre.
shpc-registry automated BioContainers addition for bioconductor-tigre
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tigre
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tigre:1.56.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tigre/1.56.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-tigre/1.56.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tigre-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tigre-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tigre-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tigre-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tigre-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tigre-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tigre

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