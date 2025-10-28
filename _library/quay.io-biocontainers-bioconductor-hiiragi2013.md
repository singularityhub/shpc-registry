---
layout: container
name:  "quay.io/biocontainers/bioconductor-hiiragi2013"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hiiragi2013/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hiiragi2013/container.yaml"
updated_at: "2025-10-28 03:47:29.537640"
latest: "1.41.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hiiragi2013"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.41.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hiiragi2013"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hiiragi2013", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hiiragi2013", "latest": {"1.41.0--r44hdfd78af_0": "sha256:b4f776bc1e846bcc7ae196c53891245de52c78e81bf881797de63f97ee99d3c4"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:b133c0b4e5271cb5adf4699013c5af2be89f39326bce8180db3703c011709c86", "1.34.0--r42hdfd78af_0": "sha256:0208dec89bb2eb65bf7d780c4955c59804ae91fa9ec9b1f95e78dfb66a65d629", "1.36.0--r43hdfd78af_0": "sha256:ac827618c2c44276e037eae3717704b282765f9df33e20f59c9321bd2d854664", "1.38.0--r43hdfd78af_0": "sha256:9423c6ecd52b475f59ad810d6ef536d0758e774b3202e8524ef85dc169a6427d", "1.41.0--r44hdfd78af_0": "sha256:b4f776bc1e846bcc7ae196c53891245de52c78e81bf881797de63f97ee99d3c4"}, "docker": "quay.io/biocontainers/bioconductor-hiiragi2013"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hiiragi2013.
shpc-registry automated BioContainers addition for bioconductor-hiiragi2013
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hiiragi2013
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hiiragi2013:1.41.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hiiragi2013/1.41.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hiiragi2013/1.41.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hiiragi2013-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hiiragi2013-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hiiragi2013-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hiiragi2013-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hiiragi2013-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hiiragi2013-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hiiragi2013

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