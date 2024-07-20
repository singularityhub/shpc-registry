---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcrma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcrma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcrma/container.yaml"
updated_at: "2024-07-20 03:03:18.705865"
latest: "2.74.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcrma"

versions:
 - "2.66.0--r41hc0cfd56_2"
 - "2.70.0--r42hc0cfd56_0"
 - "2.70.0--r42ha9d7317_1"
 - "2.72.0--r43ha9d7317_0"
 - "2.74.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcrma"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcrma", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcrma", "latest": {"2.74.0--r43ha9d7317_0": "sha256:f4f3e8dc5c44fad2d7e93ca48be755be2ec2b45c8b0acbc630d037ad4eaa7390"}, "tags": {"2.66.0--r41hc0cfd56_2": "sha256:5d7fe65c21e750c17b593a1dca57d9dc85d5d9ee3b2108479054618fc1bd9eb6", "2.70.0--r42hc0cfd56_0": "sha256:2c3739bbd962b544fbdcc42ad2b5b3d59dd56e7a34783a74bc6eac08fd070a11", "2.70.0--r42ha9d7317_1": "sha256:5084f8c677506c7cc9274001c0a199ae057ef95628c91e51777955f8fb7dcc39", "2.72.0--r43ha9d7317_0": "sha256:8de44a6ad516240e245094bddf8beb37dc41a13052d8ace89b321e555dd34667", "2.74.0--r43ha9d7317_0": "sha256:f4f3e8dc5c44fad2d7e93ca48be755be2ec2b45c8b0acbc630d037ad4eaa7390"}, "docker": "quay.io/biocontainers/bioconductor-gcrma"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcrma.
shpc-registry automated BioContainers addition for bioconductor-gcrma
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcrma
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcrma:2.74.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcrma/2.74.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-gcrma/2.74.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcrma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcrma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcrma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcrma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcrma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcrma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gcrma

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