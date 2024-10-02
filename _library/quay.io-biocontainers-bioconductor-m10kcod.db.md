---
layout: container
name:  "quay.io/biocontainers/bioconductor-m10kcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-m10kcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-m10kcod.db/container.yaml"
updated_at: "2024-10-02 03:13:04.450150"
latest: "3.4.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-m10kcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-m10kcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-m10kcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-m10kcod.db", "latest": {"3.4.0--r43hdfd78af_12": "sha256:6a6a8e11ef3758a4b8531ca8cdeda844efe56d12957a45119aa9447f8e9140c0"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:90b2097e922c9e45f2b2d4276e2ad92a928882fbf26c8bf1bfe4537132389baa", "3.4.0--r42hdfd78af_10": "sha256:3e7b15cfcfacf4cfb02677fefd62e160d9712dd70407119d8cb157b7f8d3dceb", "3.4.0--r43hdfd78af_11": "sha256:2bd60aa1226e4a5e1b1c434e42bd8e1b7c029062652f9c9ca82d9fac3af32c6b", "3.4.0--r43hdfd78af_12": "sha256:6a6a8e11ef3758a4b8531ca8cdeda844efe56d12957a45119aa9447f8e9140c0"}, "docker": "quay.io/biocontainers/bioconductor-m10kcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-m10kcod.db.
shpc-registry automated BioContainers addition for bioconductor-m10kcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-m10kcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-m10kcod.db:3.4.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-m10kcod.db/3.4.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-m10kcod.db/3.4.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-m10kcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m10kcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-m10kcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-m10kcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-m10kcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-m10kcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-m10kcod.db

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