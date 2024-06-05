---
layout: container
name:  "quay.io/biocontainers/bioconductor-jazaerimetadata.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-jazaerimetadata.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-jazaerimetadata.db/container.yaml"
updated_at: "2024-06-05 03:07:58.504680"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-jazaerimetadata.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-jazaerimetadata.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-jazaerimetadata.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-jazaerimetadata.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:271aa22b70e0cbb2d98bd6403d746e1756186597528f3ec1c1f893520222ff5b"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:978d3e374ecde90b974ed6363dce901a78bf2c2b45ea2f6abcf7bed054a7bffc", "3.2.3--r42hdfd78af_10": "sha256:238e7f90eb505aaafe31f0f71d80ba12f1a6626ac5f2227797f16b8e3ef24a88", "3.2.3--r43hdfd78af_11": "sha256:98d97f46992d842e5d5b78f352e961b736a53c00d0d3788cafae703540d2da64", "3.2.3--r43hdfd78af_12": "sha256:271aa22b70e0cbb2d98bd6403d746e1756186597528f3ec1c1f893520222ff5b"}, "docker": "quay.io/biocontainers/bioconductor-jazaerimetadata.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-jazaerimetadata.db.
shpc-registry automated BioContainers addition for bioconductor-jazaerimetadata.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-jazaerimetadata.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-jazaerimetadata.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-jazaerimetadata.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-jazaerimetadata.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-jazaerimetadata.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jazaerimetadata.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jazaerimetadata.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-jazaerimetadata.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-jazaerimetadata.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-jazaerimetadata.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-jazaerimetadata.db

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