---
layout: container
name:  "quay.io/biocontainers/bioconductor-rcellminerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rcellminerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rcellminerdata/container.yaml"
updated_at: "2024-08-19 03:11:44.497053"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rcellminerdata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_1"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_2"
 - "2.11.2--r40_0"
 - "2.22.0--r43hdfd78af_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rcellminerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rcellminerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rcellminerdata", "latest": {"2.24.0--r43hdfd78af_0": "sha256:29d489bd7555cc15d40baaca26bd214df204ae9370b0e972c51ccacc654853b1"}, "tags": {"2.8.0--r36_0": "sha256:c0de1acd5bd44786a791905a8702ec1141cb3593fade5f2c9662440c42ab2f0d", "2.20.0--r42hdfd78af_0": "sha256:ad88be2b0d5547724a380b9c96dba0e8954999aa55736b8d5eadd2d9eecc78db", "2.16.0--r41hdfd78af_1": "sha256:bfdd94193770ac74253c38ca343ad699658a639a944544e571f68f332b00ac57", "2.14.0--r41hdfd78af_0": "sha256:f46d36a4ddf90462a5f5a9012f6dc797963b93e1a26e0bd0fc6c4c3832c64f2e", "2.12.0--r40hdfd78af_2": "sha256:dc9dbede0cdc166a818ef1f785e0c72ddbe80bd629cd6e4b12665752c7c16716", "2.11.2--r40_0": "sha256:b1131412201e78add7f73817604cb96fb081943734e26d8a15155adc7541b36e", "2.22.0--r43hdfd78af_0": "sha256:60cec265543014dc5a2aab5046ea53c2e36a8004741f4443ec0f04d64af2751d", "2.24.0--r43hdfd78af_0": "sha256:29d489bd7555cc15d40baaca26bd214df204ae9370b0e972c51ccacc654853b1"}, "docker": "quay.io/biocontainers/bioconductor-rcellminerdata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rcellminerdata.
shpc-registry automated BioContainers addition for bioconductor-rcellminerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rcellminerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rcellminerdata:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rcellminerdata/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rcellminerdata/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rcellminerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcellminerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rcellminerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rcellminerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rcellminerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rcellminerdata-inspect-deffile:

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