---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbgl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbgl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbgl/container.yaml"
updated_at: "2023-02-11 03:22:14.324794"
latest: "1.74.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rbgl"

versions:
 - "1.70.0--r41hc247a5b_2"
 - "1.74.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rbgl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbgl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbgl", "latest": {"1.74.0--r42hc247a5b_0": "sha256:d68d68fcee8c0d6fe2d90feebe7c6b0247c90a747970ce4b2f7085bcd81d165c"}, "tags": {"1.70.0--r41hc247a5b_2": "sha256:16e02b3a444b6621bc8a66fefed19b12c3215b40f05f29ea51ed5c020c456a8b", "1.74.0--r42hc247a5b_0": "sha256:d68d68fcee8c0d6fe2d90feebe7c6b0247c90a747970ce4b2f7085bcd81d165c"}, "docker": "quay.io/biocontainers/bioconductor-rbgl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbgl.
shpc-registry automated BioContainers addition for bioconductor-rbgl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbgl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbgl:1.74.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbgl/1.74.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-rbgl/1.74.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbgl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbgl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbgl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbgl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbgl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbgl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbgl

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