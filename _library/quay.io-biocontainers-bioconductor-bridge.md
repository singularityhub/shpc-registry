---
layout: container
name:  "quay.io/biocontainers/bioconductor-bridge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bridge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bridge/container.yaml"
updated_at: "2023-11-19 02:50:09.257883"
latest: "1.62.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-bridge"

versions:
 - "1.58.0--r41hc0cfd56_2"
 - "1.62.0--r42hc0cfd56_0"
 - "1.62.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-bridge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bridge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bridge", "latest": {"1.62.0--r42ha9d7317_1": "sha256:3ea756787dd93e5ed6c6f1affd193cc8090010e2d1f362f2fca4c26c968ca0c0"}, "tags": {"1.58.0--r41hc0cfd56_2": "sha256:670cf2714e02f74b754c536d10a42947587046d686d71e03f4f0939de9579d76", "1.62.0--r42hc0cfd56_0": "sha256:f95fc63417e89f2d003a30fa445747e541d70f432c331d23ed8d684fe802afe7", "1.62.0--r42ha9d7317_1": "sha256:3ea756787dd93e5ed6c6f1affd193cc8090010e2d1f362f2fca4c26c968ca0c0"}, "docker": "quay.io/biocontainers/bioconductor-bridge"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bridge.
shpc-registry automated BioContainers addition for bioconductor-bridge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bridge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bridge:1.62.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bridge/1.62.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-bridge/1.62.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bridge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bridge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bridge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bridge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bridge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bridge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bridge

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