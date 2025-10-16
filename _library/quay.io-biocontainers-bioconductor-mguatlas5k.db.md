---
layout: container
name:  "quay.io/biocontainers/bioconductor-mguatlas5k.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mguatlas5k.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mguatlas5k.db/container.yaml"
updated_at: "2025-10-16 03:20:06.657084"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mguatlas5k.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mguatlas5k.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mguatlas5k.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mguatlas5k.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:79d7804e6bb380220e3feaf41343add9965f7329e1dc99a5ce9f30bf69449722"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:83747689c8ebeb20945ec4b617ff2c85adc70702ec9ef3ba04d25130f209e3ef", "3.2.3--r42hdfd78af_10": "sha256:917be5fa9fbb500091dc2c9b491546abe1f4061c525c9d1f8f6a8c4eeda092b6", "3.2.3--r43hdfd78af_11": "sha256:d199fe1a687ac3c6e4a812020ea40dde77b807b482d689d23c7acbd5fd1d7777", "3.2.3--r43hdfd78af_12": "sha256:468e53b147d63bed8276aa8401603f8b9cb7dcb2feb31a3b55fe9693688246d4", "3.2.3--r44hdfd78af_13": "sha256:79d7804e6bb380220e3feaf41343add9965f7329e1dc99a5ce9f30bf69449722"}, "docker": "quay.io/biocontainers/bioconductor-mguatlas5k.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mguatlas5k.db.
shpc-registry automated BioContainers addition for bioconductor-mguatlas5k.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mguatlas5k.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mguatlas5k.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mguatlas5k.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mguatlas5k.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mguatlas5k.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mguatlas5k.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mguatlas5k.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mguatlas5k.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mguatlas5k.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mguatlas5k.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mguatlas5k.db

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