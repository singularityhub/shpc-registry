---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu6800subacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu6800subacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu6800subacdf/container.yaml"
updated_at: "2023-08-29 04:02:17.411806"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-hu6800subacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-hu6800subacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu6800subacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu6800subacdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:cad7bd655053c3ad63fef8ea5ec88453959d39ceca30290412ca73d4fc55ec56"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:741daf4c0765d82c8d20f3c9743ced032a7b22d17ae87df76a5ecf9fea2d38ba", "2.18.0--r42hdfd78af_10": "sha256:ad189a6a7c6e9a1bec23ce1d013dee8e848d73f57ba556700fd5031ebd299e6d", "2.18.0--r43hdfd78af_11": "sha256:cad7bd655053c3ad63fef8ea5ec88453959d39ceca30290412ca73d4fc55ec56"}, "docker": "quay.io/biocontainers/bioconductor-hu6800subacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu6800subacdf.
shpc-registry automated BioContainers addition for bioconductor-hu6800subacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subacdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu6800subacdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-hu6800subacdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu6800subacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu6800subacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu6800subacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu6800subacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu6800subacdf

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