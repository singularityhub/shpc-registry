---
layout: container
name:  "quay.io/biocontainers/bioconductor-rama"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rama/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rama/container.yaml"
updated_at: "2023-04-01 02:41:58.948789"
latest: "1.72.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rama"

versions:
 - "1.68.0--r41hc0cfd56_2"
 - "1.72.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rama"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rama", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rama", "latest": {"1.72.0--r42hc0cfd56_0": "sha256:e65e8ed776e829fde5b5ebc0f72f20370319818c0dc2f2f2f88ef3243a6731f5"}, "tags": {"1.68.0--r41hc0cfd56_2": "sha256:31d2c232e93d19a63983fc5dda4b325a1de1b033d789c4a25fd9be630b73129e", "1.72.0--r42hc0cfd56_0": "sha256:e65e8ed776e829fde5b5ebc0f72f20370319818c0dc2f2f2f88ef3243a6731f5"}, "docker": "quay.io/biocontainers/bioconductor-rama"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rama.
shpc-registry automated BioContainers addition for bioconductor-rama
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rama
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rama:1.72.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rama/1.72.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-rama/1.72.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rama-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rama-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rama-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rama-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rama-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rama-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rama

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