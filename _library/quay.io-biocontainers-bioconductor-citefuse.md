---
layout: container
name:  "quay.io/biocontainers/bioconductor-citefuse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-citefuse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-citefuse/container.yaml"
updated_at: "2023-09-17 00:09:22.707793"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-citefuse"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-citefuse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-citefuse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-citefuse", "latest": {"1.10.0--r42hdfd78af_0": "sha256:35f4604b32d4c3363c9173bc3e887b2f6f5dfc8e9b1f85cc1badac6c48f1bfc6"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:f0e5b6e5804e01e6cdff7103011d7b54f81f1ef9ef13236251037ee0b92bc5eb", "1.10.0--r42hdfd78af_0": "sha256:35f4604b32d4c3363c9173bc3e887b2f6f5dfc8e9b1f85cc1badac6c48f1bfc6"}, "docker": "quay.io/biocontainers/bioconductor-citefuse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-citefuse.
shpc-registry automated BioContainers addition for bioconductor-citefuse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-citefuse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-citefuse:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-citefuse/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-citefuse/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-citefuse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citefuse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citefuse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-citefuse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-citefuse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-citefuse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-citefuse

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