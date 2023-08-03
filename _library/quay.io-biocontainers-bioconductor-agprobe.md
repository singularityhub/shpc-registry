---
layout: container
name:  "quay.io/biocontainers/bioconductor-agprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-agprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-agprobe/container.yaml"
updated_at: "2023-08-03 02:42:45.031076"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-agprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-agprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-agprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-agprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:10f1bc0c3bf7f86d4487346c444dc30708e555e0b418913e2228262087f48404"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:3a49204e53bf60c0762ddcc6d776cb911e5e4b8572f1b56bdabe55216c78ab4e", "2.18.0--r42hdfd78af_10": "sha256:cd0a57223a70af9ec8353a06be09cbbcfb1c8a1fb3d3aaa4557a88386288694d", "2.18.0--r43hdfd78af_11": "sha256:10f1bc0c3bf7f86d4487346c444dc30708e555e0b418913e2228262087f48404"}, "docker": "quay.io/biocontainers/bioconductor-agprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-agprobe.
shpc-registry automated BioContainers addition for bioconductor-agprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-agprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-agprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-agprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-agprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-agprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-agprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-agprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-agprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-agprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-agprobe

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