---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcsconnection"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcsconnection/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcsconnection/container.yaml"
updated_at: "2025-08-28 03:45:40.828776"
latest: "1.6.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-gcsconnection"

versions:
 - "1.6.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-gcsconnection"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcsconnection", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcsconnection", "latest": {"1.6.0--r41hc247a5b_2": "sha256:67d19f987adab9554d9033d6f7dfff1ec49f14b0c492b43dae456fb8515b0b2d"}, "tags": {"1.6.0--r41hc247a5b_2": "sha256:67d19f987adab9554d9033d6f7dfff1ec49f14b0c492b43dae456fb8515b0b2d"}, "docker": "quay.io/biocontainers/bioconductor-gcsconnection"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcsconnection.
shpc-registry automated BioContainers addition for bioconductor-gcsconnection
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcsconnection
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcsconnection:1.6.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcsconnection/1.6.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-gcsconnection/1.6.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcsconnection-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcsconnection-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcsconnection-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcsconnection-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcsconnection-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcsconnection-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gcsconnection

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