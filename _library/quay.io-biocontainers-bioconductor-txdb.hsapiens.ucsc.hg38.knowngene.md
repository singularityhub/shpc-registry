---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene/container.yaml"
updated_at: "2025-11-29 03:51:48.035691"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.6--r36_1"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.10.0--r40hdfd78af_3"
 - "3.16.0--r42hdfd78af_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.knowngene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.knowngene", "latest": {"3.20.0--r44hdfd78af_0": "sha256:18be072d63e9a54e70938dd0742f06e3c20b09f43c7890ce2bb83a3d36a5acaf"}, "tags": {"3.4.6--r36_1": "sha256:caa7feef0197c0ffea3345a9b5cd4977884712c1c66b90c1633308663c75667b", "3.14.0--r41hdfd78af_1": "sha256:34a5b2df033d794fe69fded1795ae82125b65e7be3a96bce9da3b37e1852876d", "3.13.0--r41hdfd78af_0": "sha256:f2796f2c5bd8937d813aca3cb10b5e2ebda930995598f04f50325cb75f026d86", "3.10.0--r40hdfd78af_3": "sha256:c127ff40a6e4486d575f607d7ed90eee280b54ee0694f16b4cf3c5fc839329eb", "3.16.0--r42hdfd78af_0": "sha256:dbe0d807e0b1b06c36983f8adb8d05f8585205ea14846530a1fad4d3af20731d", "3.17.0--r43hdfd78af_0": "sha256:c9a4751f292e12219a872c31b705dfca3cc79bab8ee0e93645312b76376f7a2e", "3.18.0--r43hdfd78af_0": "sha256:6521958f632984b6664ee272eca8363fb3e9a58440b5f82a776b7236703903ee", "3.20.0--r44hdfd78af_0": "sha256:18be072d63e9a54e70938dd0742f06e3c20b09f43c7890ce2bb83a3d36a5acaf"}, "docker": "quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene.
shpc-registry automated BioContainers addition for bioconductor-txdb.hsapiens.ucsc.hg38.knowngene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-txdb.hsapiens.ucsc.hg38.knowngene/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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