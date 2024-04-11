---
layout: container
name:  "quay.io/biocontainers/bioconductor-anvil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anvil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anvil/container.yaml"
updated_at: "2024-04-11 03:11:12.031867"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anvil"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.3--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-anvil"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anvil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-anvil", "latest": {"1.14.0--r43hdfd78af_0": "sha256:cc9719670925383dbfe5c1e508e0b46d97aec3918a7457e14495ec7938d45297"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:7ce7b1c080c925c83b7623000a610479c52eba3bc74f69224c746a01dc2cd566", "1.10.0--r42hdfd78af_0": "sha256:883ad9c35669f8e3c987d305fc6c25b433f914f79dbe181c58292efafc355cb2", "1.12.3--r43hdfd78af_0": "sha256:d56552d9b5a4806f560d227ab36be1fa49d635ae396da8a56f6e9f756205e46c", "1.14.0--r43hdfd78af_0": "sha256:cc9719670925383dbfe5c1e508e0b46d97aec3918a7457e14495ec7938d45297"}, "docker": "quay.io/biocontainers/bioconductor-anvil"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anvil.
shpc-registry automated BioContainers addition for bioconductor-anvil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anvil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anvil:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anvil/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anvil/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anvil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anvil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anvil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anvil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-anvil

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