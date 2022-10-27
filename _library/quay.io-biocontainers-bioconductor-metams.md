---
layout: container
name:  "quay.io/biocontainers/bioconductor-metams"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metams/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metams/container.yaml"
updated_at: "2022-10-27 00:37:42.783978"
latest: "1.8.0--0"
container_url: "https://biocontainers.pro/tools/bioconductor-metams"

versions:
 - "1.8.0--0"
description: "shpc-registry automated BioContainers addition for bioconductor-metams"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metams", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metams", "latest": {"1.8.0--0": "sha256:d1e2c9473cd7d4fb6de868c687e4966e7011b8a078bc42b0a09fe1d766b3c5c0"}, "tags": {"1.8.0--0": "sha256:d1e2c9473cd7d4fb6de868c687e4966e7011b8a078bc42b0a09fe1d766b3c5c0"}, "docker": "quay.io/biocontainers/bioconductor-metams"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metams.
shpc-registry automated BioContainers addition for bioconductor-metams
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metams
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metams:1.8.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metams/1.8.0--0
$ module help quay.io/biocontainers/bioconductor-metams/1.8.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metams-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metams-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metams-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metams-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metams-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metams-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metams

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