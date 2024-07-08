---
layout: container
name:  "quay.io/biocontainers/bioconductor-hguatlas13k.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hguatlas13k.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hguatlas13k.db/container.yaml"
updated_at: "2024-07-08 02:46:25.449554"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hguatlas13k.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r41hdfd78af_10"
 - "3.2.3--r42hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hguatlas13k.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hguatlas13k.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hguatlas13k.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:1dd49f1a75882814903e1cd70bdbe706bb3d13be77ecf5df275b6780ce708f0b"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:c7617143c444557b4436f4ebf59eabd7081ddc709b8b02967d63c8c08007ac71", "3.2.3--r41hdfd78af_10": "sha256:6dbd5922123b7a92c75d8ddb2f9dd5690e523a295bba48803878c55ef63f3906", "3.2.3--r42hdfd78af_11": "sha256:4edcc137a3045f342576b7edb10d0019ba87df2f1ebbb6b125537e49f52f936e", "3.2.3--r43hdfd78af_12": "sha256:1dd49f1a75882814903e1cd70bdbe706bb3d13be77ecf5df275b6780ce708f0b"}, "docker": "quay.io/biocontainers/bioconductor-hguatlas13k.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hguatlas13k.db.
shpc-registry automated BioContainers addition for bioconductor-hguatlas13k.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hguatlas13k.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hguatlas13k.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hguatlas13k.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hguatlas13k.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hguatlas13k.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hguatlas13k.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hguatlas13k.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hguatlas13k.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hguatlas13k.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hguatlas13k.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hguatlas13k.db

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