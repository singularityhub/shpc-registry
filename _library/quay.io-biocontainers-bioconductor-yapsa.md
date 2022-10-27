---
layout: container
name:  "quay.io/biocontainers/bioconductor-yapsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yapsa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yapsa/container.yaml"
updated_at: "2022-10-27 01:05:49.000221"
latest: "1.8.0--r351_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yapsa"

versions:
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yapsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yapsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yapsa", "latest": {"1.8.0--r351_0": "sha256:111aa7dbfac5cf3f026c4d92ff2c67a3e368e4ac888e8da1948c16a25af5626e"}, "tags": {"1.8.0--r351_0": "sha256:111aa7dbfac5cf3f026c4d92ff2c67a3e368e4ac888e8da1948c16a25af5626e"}, "docker": "quay.io/biocontainers/bioconductor-yapsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yapsa.
shpc-registry automated BioContainers addition for bioconductor-yapsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yapsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yapsa:1.8.0--r351_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yapsa/1.8.0--r351_0
$ module help quay.io/biocontainers/bioconductor-yapsa/1.8.0--r351_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yapsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yapsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yapsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yapsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yapsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yapsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yapsa

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