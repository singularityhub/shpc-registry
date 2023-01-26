---
layout: container
name:  "quay.io/biocontainers/bioconductor-glad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-glad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-glad/container.yaml"
updated_at: "2023-01-26 03:11:50.910350"
latest: "2.62.0--r42hd4b0f26_0"
container_url: "https://biocontainers.pro/tools/bioconductor-glad"

versions:
 - "2.58.0--r41hd4b0f26_3"
 - "2.62.0--r42hd4b0f26_0"
description: "shpc-registry automated BioContainers addition for bioconductor-glad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-glad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-glad", "latest": {"2.62.0--r42hd4b0f26_0": "sha256:6a61fdc25a7c1c40f282297cd94624e59460a446c5cbf4abbd89f3cfc7cae106"}, "tags": {"2.58.0--r41hd4b0f26_3": "sha256:86f1d3508a046245b5c9fc463fcccd1fcb5830182b95e638479c192b7819c48c", "2.62.0--r42hd4b0f26_0": "sha256:6a61fdc25a7c1c40f282297cd94624e59460a446c5cbf4abbd89f3cfc7cae106"}, "docker": "quay.io/biocontainers/bioconductor-glad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-glad.
shpc-registry automated BioContainers addition for bioconductor-glad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-glad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-glad:2.62.0--r42hd4b0f26_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-glad/2.62.0--r42hd4b0f26_0
$ module help quay.io/biocontainers/bioconductor-glad/2.62.0--r42hd4b0f26_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-glad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-glad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-glad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-glad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-glad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-glad

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