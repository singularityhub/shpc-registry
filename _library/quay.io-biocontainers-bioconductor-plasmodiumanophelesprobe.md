---
layout: container
name:  "quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe/container.yaml"
updated_at: "2024-04-28 03:10:32.850837"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-plasmodiumanophelesprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelesprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-plasmodiumanophelesprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelesprobe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:628f0cda3711c0fa20b20337bc99160304a81cc61d6fb1c1657d59b2d74f69e1"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d6bcd68f8d70280b9021aaec2efcae222fd748ad4f9a46d5296a301a999fb363", "2.18.0--r42hdfd78af_11": "sha256:09e59f91d5a6603b7628a1fe7599e7a4f5ce0854fbf7a53103e768da19c068d4", "2.18.0--r43hdfd78af_12": "sha256:07674d1c37dc2d802cd8d08b8b89065c36e91440d364091f69512e54c89714c0", "2.18.0--r43hdfd78af_13": "sha256:628f0cda3711c0fa20b20337bc99160304a81cc61d6fb1c1657d59b2d74f69e1"}, "docker": "quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe.
shpc-registry automated BioContainers addition for bioconductor-plasmodiumanophelesprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-plasmodiumanophelesprobe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-plasmodiumanophelesprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plasmodiumanophelesprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-plasmodiumanophelesprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-plasmodiumanophelesprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-plasmodiumanophelesprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-plasmodiumanophelesprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-plasmodiumanophelesprobe

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