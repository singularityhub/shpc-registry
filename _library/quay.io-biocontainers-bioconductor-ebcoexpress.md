---
layout: container
name:  "quay.io/biocontainers/bioconductor-ebcoexpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ebcoexpress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ebcoexpress/container.yaml"
updated_at: "2024-06-20 03:09:41.992106"
latest: "1.46.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ebcoexpress"

versions:
 - "1.38.0--r41hc0cfd56_2"
 - "1.42.0--r42hc0cfd56_0"
 - "1.42.0--r42ha9d7317_1"
 - "1.44.0--r43ha9d7317_0"
 - "1.46.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ebcoexpress"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ebcoexpress", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ebcoexpress", "latest": {"1.46.0--r43ha9d7317_0": "sha256:12866f8a8e9b52ac5cf42fd61198718a38630f8c2ac411bf725fb819b104efd1"}, "tags": {"1.38.0--r41hc0cfd56_2": "sha256:801af83f9aff29876ee4711c6cfefc3b8e98d5c6be863230b7c8c6448e547f1a", "1.42.0--r42hc0cfd56_0": "sha256:c330880628ad3113328b47fa41acfdbf6f95c27d85d2d6b78c980f8f8132fe11", "1.42.0--r42ha9d7317_1": "sha256:874a004905056a607cf07a8b2ec6e15e81afdec3a41ac702c680000a1e838e44", "1.44.0--r43ha9d7317_0": "sha256:f0b56bb61eb206aede348d2a33b9256c38614fe33d6b0137240e9e8db1186acc", "1.46.0--r43ha9d7317_0": "sha256:12866f8a8e9b52ac5cf42fd61198718a38630f8c2ac411bf725fb819b104efd1"}, "docker": "quay.io/biocontainers/bioconductor-ebcoexpress"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ebcoexpress.
shpc-registry automated BioContainers addition for bioconductor-ebcoexpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ebcoexpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ebcoexpress:1.46.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ebcoexpress/1.46.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-ebcoexpress/1.46.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ebcoexpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebcoexpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ebcoexpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ebcoexpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ebcoexpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ebcoexpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ebcoexpress

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