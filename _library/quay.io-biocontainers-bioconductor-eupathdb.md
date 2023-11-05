---
layout: container
name:  "quay.io/biocontainers/bioconductor-eupathdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eupathdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eupathdb/container.yaml"
updated_at: "2023-11-05 02:48:42.547768"
latest: "1.0.1--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-eupathdb"

versions:
 - "1.0.1--r41hdfd78af_9"
 - "1.0.1--r42hdfd78af_10"
 - "1.0.1--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-eupathdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eupathdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eupathdb", "latest": {"1.0.1--r43hdfd78af_11": "sha256:c4fe7f0f31879725a73df946a3e3dbbad542da0989705c2a3bef8aae201e3cf4"}, "tags": {"1.0.1--r41hdfd78af_9": "sha256:fa7e853093aafe2efde0ad9843b77dae3735334510b8c533f5a4556a1df57430", "1.0.1--r42hdfd78af_10": "sha256:2a3feb5e9161295802a8da73f65f3974112acafc6df80c7d9d9aaedf29025a5a", "1.0.1--r43hdfd78af_11": "sha256:c4fe7f0f31879725a73df946a3e3dbbad542da0989705c2a3bef8aae201e3cf4"}, "docker": "quay.io/biocontainers/bioconductor-eupathdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eupathdb.
shpc-registry automated BioContainers addition for bioconductor-eupathdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eupathdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eupathdb:1.0.1--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eupathdb/1.0.1--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-eupathdb/1.0.1--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eupathdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eupathdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eupathdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eupathdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eupathdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eupathdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-eupathdb

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