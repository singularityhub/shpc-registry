---
layout: container
name:  "quay.io/biocontainers/bioconductor-clustifyrdatahub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clustifyrdatahub/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clustifyrdatahub/container.yaml"
updated_at: "2024-06-10 03:00:27.867991"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clustifyrdatahub"

versions:
 - "1.4.0--r41hdfd78af_1"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clustifyrdatahub"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clustifyrdatahub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clustifyrdatahub", "latest": {"1.12.0--r43hdfd78af_0": "sha256:a005c3d122489c85ef7c5fa46f5c8c8911c744a01e51832d6a3624ac9a1a630e"}, "tags": {"1.4.0--r41hdfd78af_1": "sha256:536ff3b834c0a1952ff3a1ffa5833a000a9a5074bcc26b17f6639459d2ca1caa", "1.8.0--r42hdfd78af_0": "sha256:3ac8f154ead3c426e8a46b8819cc917013a84cc442f6ebef47cbdeef51b155d2", "1.10.0--r43hdfd78af_0": "sha256:03fcd92746e7c4fd2a89d322e3516fdbfbf7897a7af8dcb088d9e59686d9bf41", "1.12.0--r43hdfd78af_0": "sha256:a005c3d122489c85ef7c5fa46f5c8c8911c744a01e51832d6a3624ac9a1a630e"}, "docker": "quay.io/biocontainers/bioconductor-clustifyrdatahub"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clustifyrdatahub.
shpc-registry automated BioContainers addition for bioconductor-clustifyrdatahub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clustifyrdatahub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clustifyrdatahub:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clustifyrdatahub/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clustifyrdatahub/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clustifyrdatahub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustifyrdatahub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clustifyrdatahub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clustifyrdatahub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clustifyrdatahub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clustifyrdatahub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clustifyrdatahub

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