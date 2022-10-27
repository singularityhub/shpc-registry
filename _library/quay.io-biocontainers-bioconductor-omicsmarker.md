---
layout: container
name:  "quay.io/biocontainers/bioconductor-omicsmarker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omicsmarker/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omicsmarker/container.yaml"
updated_at: "2022-10-27 00:27:42.457175"
latest: "1.19.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omicsmarker"

versions:
 - "1.19.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omicsmarker"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omicsmarker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omicsmarker", "latest": {"1.19.0--r40_0": "sha256:7a444a8c53821fb91a5275e7e2782e58738203412f799e2ce264860068a2c455"}, "tags": {"1.19.0--r40_0": "sha256:7a444a8c53821fb91a5275e7e2782e58738203412f799e2ce264860068a2c455"}, "docker": "quay.io/biocontainers/bioconductor-omicsmarker"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omicsmarker.
shpc-registry automated BioContainers addition for bioconductor-omicsmarker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omicsmarker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omicsmarker:1.19.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omicsmarker/1.19.0--r40_0
$ module help quay.io/biocontainers/bioconductor-omicsmarker/1.19.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omicsmarker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicsmarker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omicsmarker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omicsmarker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omicsmarker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omicsmarker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-omicsmarker

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