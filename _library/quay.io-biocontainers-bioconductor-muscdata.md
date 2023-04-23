---
layout: container
name:  "quay.io/biocontainers/bioconductor-muscdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-muscdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-muscdata/container.yaml"
updated_at: "2023-04-23 03:10:33.622633"
latest: "1.12.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-muscdata"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-muscdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-muscdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-muscdata", "latest": {"1.12.0--r42hdfd78af_0": "sha256:11e610f3d00f33066cab00c8dc4498f0586bab30bb9e5207c9a76fcdfed47419"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:a5c53c3da7823398ba5a8c3fe02a69e8e7eb0a70aab4b0319d818fc94244e566", "1.12.0--r42hdfd78af_0": "sha256:11e610f3d00f33066cab00c8dc4498f0586bab30bb9e5207c9a76fcdfed47419"}, "docker": "quay.io/biocontainers/bioconductor-muscdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-muscdata.
shpc-registry automated BioContainers addition for bioconductor-muscdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-muscdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-muscdata:1.12.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-muscdata/1.12.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-muscdata/1.12.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-muscdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-muscdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-muscdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-muscdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-muscdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-muscdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-muscdata

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