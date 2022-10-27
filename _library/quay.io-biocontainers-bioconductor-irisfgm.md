---
layout: container
name:  "quay.io/biocontainers/bioconductor-irisfgm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-irisfgm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-irisfgm/container.yaml"
updated_at: "2022-10-27 00:52:39.976360"
latest: "1.2.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-irisfgm"

versions:
 - "1.2.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-irisfgm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-irisfgm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-irisfgm", "latest": {"1.2.0--r41hc247a5b_2": "sha256:1d44c47aea396502ffdce092b7393207b8d746e2f4cc2c99f3583266082151b5"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:1d44c47aea396502ffdce092b7393207b8d746e2f4cc2c99f3583266082151b5"}, "docker": "quay.io/biocontainers/bioconductor-irisfgm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-irisfgm.
shpc-registry automated BioContainers addition for bioconductor-irisfgm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-irisfgm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-irisfgm:1.2.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-irisfgm/1.2.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-irisfgm/1.2.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-irisfgm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-irisfgm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-irisfgm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-irisfgm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-irisfgm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-irisfgm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-irisfgm

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