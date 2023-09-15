---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbcbook1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbcbook1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbcbook1/container.yaml"
updated_at: "2023-09-15 02:55:52.844339"
latest: "1.66.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rbcbook1"

versions:
 - "1.62.0--r41hdfd78af_0"
 - "1.66.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rbcbook1"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbcbook1", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbcbook1", "latest": {"1.66.0--r42hdfd78af_0": "sha256:35b6b92de45464b04c2c9f69720c8ce5eeb24413aa93173813b997b7c1ab95fc"}, "tags": {"1.62.0--r41hdfd78af_0": "sha256:15a0d576d12ca6664a4985f67eb9c93829a7c06d2054368498b40a4365f928eb", "1.66.0--r42hdfd78af_0": "sha256:35b6b92de45464b04c2c9f69720c8ce5eeb24413aa93173813b997b7c1ab95fc"}, "docker": "quay.io/biocontainers/bioconductor-rbcbook1"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbcbook1.
shpc-registry automated BioContainers addition for bioconductor-rbcbook1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbcbook1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbcbook1:1.66.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbcbook1/1.66.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rbcbook1/1.66.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbcbook1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbcbook1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbcbook1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbcbook1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbcbook1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbcbook1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbcbook1

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