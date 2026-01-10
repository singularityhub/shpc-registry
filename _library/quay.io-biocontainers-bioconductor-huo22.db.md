---
layout: container
name:  "quay.io/biocontainers/bioconductor-huo22.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huo22.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huo22.db/container.yaml"
updated_at: "2026-01-10 03:40:40.926239"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-huo22.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-huo22.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huo22.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huo22.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:44820bb07a75e76d337b7424b09e3d769af532b1597e5fe9cd43f6ec6da8f0ba"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:ec301832b73e6219a58616ab9b43c1252196982fb1c3d20326c0aa01fff872d0", "3.2.3--r42hdfd78af_10": "sha256:4b0d4071ede64eedddacc2a5a4eb72d616f0b2719758afc6ebd1afd5befb6de0", "3.2.3--r43hdfd78af_11": "sha256:e942447c24372899aed0277d1e17d4b5edc4604ca8ab31c1fb2083a409158621", "3.2.3--r43hdfd78af_12": "sha256:f0f66a1fb50b7aa4286fb85f73182fe99dd1be171d10a4bb22208c9cc6b1683d", "3.2.3--r44hdfd78af_13": "sha256:44820bb07a75e76d337b7424b09e3d769af532b1597e5fe9cd43f6ec6da8f0ba"}, "docker": "quay.io/biocontainers/bioconductor-huo22.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huo22.db.
shpc-registry automated BioContainers addition for bioconductor-huo22.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huo22.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huo22.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huo22.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-huo22.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huo22.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huo22.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huo22.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huo22.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huo22.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huo22.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huo22.db

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