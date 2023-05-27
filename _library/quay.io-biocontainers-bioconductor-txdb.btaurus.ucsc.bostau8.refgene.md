---
layout: container
name:  "quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene/container.yaml"
updated_at: "2023-05-27 03:05:00.001936"
latest: "3.12.0--r42hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-txdb.btaurus.ucsc.bostau8.refgene"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.4.6--r36_1"
 - "3.12.0--r42hdfd78af_5"
 - "3.11.0--r40_0"
 - "3.10.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau8.refgene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txdb.btaurus.ucsc.bostau8.refgene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau8.refgene", "latest": {"3.12.0--r42hdfd78af_5": "sha256:b6c6e600c69b309d5ad60ed26c732424788abea5566d4011db9675876bac1926"}, "tags": {"3.4.6--r36_1": "sha256:002682ecf9565d754b22f577b5afd56fbcc98678addadd1b3fff232250a4149e", "3.12.0--r42hdfd78af_5": "sha256:b6c6e600c69b309d5ad60ed26c732424788abea5566d4011db9675876bac1926", "3.11.0--r40_0": "sha256:2df266683df2d8d766d0d36bcd96a4e77a228934d7e616e55aba6204b0c8eb7d", "3.10.0--r36_0": "sha256:30e7f834f6d024fbbae90e90882853bd08e107318c38d4ed37342caf10d7239f"}, "docker": "quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene.
shpc-registry automated BioContainers addition for bioconductor-txdb.btaurus.ucsc.bostau8.refgene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene:3.12.0--r42hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene/3.12.0--r42hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-txdb.btaurus.ucsc.bostau8.refgene/3.12.0--r42hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txdb.btaurus.ucsc.bostau8.refgene-inspect-deffile:

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