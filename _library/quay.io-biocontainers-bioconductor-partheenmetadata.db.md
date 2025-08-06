---
layout: container
name:  "quay.io/biocontainers/bioconductor-partheenmetadata.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-partheenmetadata.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-partheenmetadata.db/container.yaml"
updated_at: "2025-08-06 04:14:40.961562"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-partheenmetadata.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-partheenmetadata.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-partheenmetadata.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-partheenmetadata.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:a05190a975536d552d09ecd19812f2ac29ce300ad9e34526764f11e190196435"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:e6d527bde9685d32ce6d25284dff028529e7331018fee306a8341458f93f50c5", "3.2.3--r42hdfd78af_10": "sha256:0e30d705a764fde184e4bb2008e6ef32b5c4d613406fea320a0bdce0a12cefd7", "3.2.3--r43hdfd78af_11": "sha256:784090b7305f9af02c1714389bae03de2524ee2eb4766c0bfb6056409f5310c6", "3.2.3--r43hdfd78af_12": "sha256:973acccb76f6cdbf620f6137a5a883f867e126911c7675c0868bfd216ec27cca", "3.2.3--r44hdfd78af_13": "sha256:a05190a975536d552d09ecd19812f2ac29ce300ad9e34526764f11e190196435"}, "docker": "quay.io/biocontainers/bioconductor-partheenmetadata.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-partheenmetadata.db.
shpc-registry automated BioContainers addition for bioconductor-partheenmetadata.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-partheenmetadata.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-partheenmetadata.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-partheenmetadata.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-partheenmetadata.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-partheenmetadata.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-partheenmetadata.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-partheenmetadata.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-partheenmetadata.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-partheenmetadata.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-partheenmetadata.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-partheenmetadata.db

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