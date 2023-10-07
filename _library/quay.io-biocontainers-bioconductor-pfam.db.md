---
layout: container
name:  "quay.io/biocontainers/bioconductor-pfam.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pfam.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pfam.db/container.yaml"
updated_at: "2023-10-07 02:48:46.897996"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pfam.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.10.0--r40_1"
 - "3.17.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pfam.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pfam.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pfam.db", "latest": {"3.17.0--r43hdfd78af_0": "sha256:fe6bfe5134b84a60663d3b4b8aca5e5b10efd5f2955a37a99a1658d64af9ab82"}, "tags": {"3.8.2--r36_1": "sha256:be2ba30b7307531062c70e611d4c57822f27913dc8bbd00b4875bff18e93c3a7", "3.16.0--r42hdfd78af_0": "sha256:e248e97c21d1ff95a27671aef425b24a674673c5d082c4ea3eb2900c2280b682", "3.14.0--r41hdfd78af_1": "sha256:817adae48d127df57debb7857f873aea721c26834e5661bccf5165721e4a49b9", "3.13.0--r41hdfd78af_0": "sha256:ae3dc2006841692075a78254f3ec9edbcca68a51e33c54be8e817542899c8d2c", "3.12.0--r40hdfd78af_1": "sha256:8f8ed00ca082a8db611b229e52997f8366dc8da6440c8b8e433646dbc41cfed1", "3.10.0--r40_1": "sha256:ce4fc9bbbba39d503eb2acb16646b9a6ed2b31de648e1b5f4abf4569889dbca8", "3.17.0--r43hdfd78af_0": "sha256:fe6bfe5134b84a60663d3b4b8aca5e5b10efd5f2955a37a99a1658d64af9ab82"}, "docker": "quay.io/biocontainers/bioconductor-pfam.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pfam.db.
shpc-registry automated BioContainers addition for bioconductor-pfam.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pfam.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pfam.db:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pfam.db/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pfam.db/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pfam.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pfam.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pfam.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pfam.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pfam.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pfam.db-inspect-deffile:

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