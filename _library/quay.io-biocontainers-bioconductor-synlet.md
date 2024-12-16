---
layout: container
name:  "quay.io/biocontainers/bioconductor-synlet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synlet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synlet/container.yaml"
updated_at: "2024-12-16 03:33:33.283540"
latest: "2.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-synlet"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "2.0.0--r43hdfd78af_0"
 - "2.2.0--r43hdfd78af_0"
 - "2.6.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-synlet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synlet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synlet", "latest": {"2.6.0--r44hdfd78af_0": "sha256:81a70518e52714a7a690f5715f915ed0ef0efec9b009f69a3a97d7fe325c0c08"}, "tags": {"1.8.0--r3.4.1_0": "sha256:73d089ed12c38d9e7a7db2ca841a33b523c8d5c24aaf205a764376082304e73f", "1.28.0--r42hdfd78af_0": "sha256:08bdb92ef42f57a2d668622468d2f043d80049e3b4a449fe9cf59497fb4a1bb5", "1.24.0--r41hdfd78af_0": "sha256:26fb5e3392d969ab43e0fa74d069c3dc5b9b13b98166086ca8fef815fd8a9c89", "1.22.0--r41hdfd78af_0": "sha256:b2d43234c8be3007f9246f38301bfbffb4a6b493fb4cfa5b33dcd7dc7dd63a0c", "1.20.0--r40hdfd78af_1": "sha256:f2ce984c5542c8139bdfc0d7ad774cca027493dbc360aae7160b266e36f799b4", "1.18.0--r40_0": "sha256:8e17f33855cb680122e5856be712f3194b1a226ba2816bf941bb252be7d6a31f", "2.0.0--r43hdfd78af_0": "sha256:d3364227d0e3448f2e2cf6897a26778ca26da649c251d283b1f9871f45d76bdd", "2.2.0--r43hdfd78af_0": "sha256:4d0f61e8353a6dcb385138ba71a4320412139e1d11fb6757d2a68e309175ca77", "2.6.0--r44hdfd78af_0": "sha256:81a70518e52714a7a690f5715f915ed0ef0efec9b009f69a3a97d7fe325c0c08"}, "docker": "quay.io/biocontainers/bioconductor-synlet", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synlet.
shpc-registry automated BioContainers addition for bioconductor-synlet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synlet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synlet:2.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synlet/2.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-synlet/2.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synlet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synlet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synlet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synlet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synlet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synlet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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