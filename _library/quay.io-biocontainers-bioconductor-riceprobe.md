---
layout: container
name:  "quay.io/biocontainers/bioconductor-riceprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-riceprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-riceprobe/container.yaml"
updated_at: "2025-08-24 03:58:02.030395"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-riceprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-riceprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-riceprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-riceprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:d8cff52f7fdf7c5485ef9e6aec0382977c044ccef6b0e15d09d6b0afc47b73b7"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5697f8dc2de7255b858ecba6dd0a81f547a30523f07a02a25231352b86c958b9", "2.18.0--r42hdfd78af_10": "sha256:4cbc0595fb983ea0b9cfc2df9d0d35dcfa7c74cf88dd6eeec8eb4bf3ac9b9c74", "2.18.0--r43hdfd78af_11": "sha256:b8a63dd07c0c29faa718b408da8c91b4e272f7071be0d332ffe6224f25201777", "2.18.0--r43hdfd78af_12": "sha256:2d20229812707f1c954e68a608d8965c4b32533689ba7691b32199f13467c0ad", "2.18.0--r44hdfd78af_13": "sha256:d8cff52f7fdf7c5485ef9e6aec0382977c044ccef6b0e15d09d6b0afc47b73b7"}, "docker": "quay.io/biocontainers/bioconductor-riceprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-riceprobe.
shpc-registry automated BioContainers addition for bioconductor-riceprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-riceprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-riceprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-riceprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-riceprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-riceprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riceprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riceprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-riceprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-riceprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-riceprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-riceprobe

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