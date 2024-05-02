---
layout: container
name:  "quay.io/biocontainers/bioconductor-metavolcanor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metavolcanor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metavolcanor/container.yaml"
updated_at: "2024-05-02 03:04:49.051664"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metavolcanor"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metavolcanor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metavolcanor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metavolcanor", "latest": {"1.14.0--r43hdfd78af_0": "sha256:596cb184f53f825269daabe9944b1c4a40789a3559aae4c7a56d27301ba9940b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b7430c2453301b364e155ed2b51e24f338cb1ae192b76639d5f241702f2b6dc7", "1.12.0--r42hdfd78af_0": "sha256:245e939d96d003c3b72f234d79ae525f8db574462752c8c291022c906c3565bc", "1.14.0--r43hdfd78af_0": "sha256:596cb184f53f825269daabe9944b1c4a40789a3559aae4c7a56d27301ba9940b"}, "docker": "quay.io/biocontainers/bioconductor-metavolcanor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metavolcanor.
shpc-registry automated BioContainers addition for bioconductor-metavolcanor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metavolcanor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metavolcanor:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metavolcanor/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metavolcanor/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metavolcanor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metavolcanor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metavolcanor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metavolcanor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metavolcanor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metavolcanor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metavolcanor

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