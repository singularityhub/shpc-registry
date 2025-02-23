---
layout: container
name:  "quay.io/biocontainers/r-pairadise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-pairadise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-pairadise/container.yaml"
updated_at: "2025-02-23 03:12:15.399977"
latest: "1.0.0--r36hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-pairadise"

versions:
 - "1.0.0--r36hdfd78af_0"
 - "1.0.0--r36hdfd78af_1"
description: "singularity registry hpc automated addition for r-pairadise"
config: {"url": "https://biocontainers.pro/tools/r-pairadise", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-pairadise", "latest": {"1.0.0--r36hdfd78af_1": "sha256:bd1de5d47374a92d0f17ca38d4e2aff725b97eb7d57ee7b9620d4f91c00e9be1"}, "tags": {"1.0.0--r36hdfd78af_0": "sha256:c292a459567f7daa0303ad96df135289454e0293da14e3012f084a771d50e8f6", "1.0.0--r36hdfd78af_1": "sha256:bd1de5d47374a92d0f17ca38d4e2aff725b97eb7d57ee7b9620d4f91c00e9be1"}, "docker": "quay.io/biocontainers/r-pairadise"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-pairadise.
singularity registry hpc automated addition for r-pairadise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-pairadise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-pairadise:1.0.0--r36hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-pairadise/1.0.0--r36hdfd78af_1
$ module help quay.io/biocontainers/r-pairadise/1.0.0--r36hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-pairadise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-pairadise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-pairadise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-pairadise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-pairadise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-pairadise-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-pairadise

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