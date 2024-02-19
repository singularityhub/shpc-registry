---
layout: container
name:  "quay.io/biocontainers/bioconductor-multiclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multiclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multiclust/container.yaml"
updated_at: "2024-02-19 02:49:27.413758"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multiclust"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.2--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multiclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multiclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multiclust", "latest": {"1.32.0--r43hdfd78af_0": "sha256:d2f7213f7d03f995b30ab33ca553d50de490c4b5c3c55b309e45153c67255c65"}, "tags": {"1.8.2--r3.4.1_0": "sha256:03f2c20688dd7544b8085edb232c725bd97a0f355cd8eea1a35347be649002c1", "1.24.0--r41hdfd78af_0": "sha256:f6d4baf2135d15b6555dbe9841eeaba38d09273e594d34ace161136ef9f6806c", "1.22.0--r41hdfd78af_0": "sha256:bd7dcbbb1c86332e12682898d6106d13ea6a43273ee63962d2467c8787ed4668", "1.20.0--r40hdfd78af_1": "sha256:03537ef557a0d9fd51f8448c441eb9f8ad44340bf1f3e199076a5665aa215305", "1.18.0--r40_0": "sha256:376a3e9f1ed47aa97a433024f55087471d035bd311fa8ee815ce4c36c7ee45d7", "1.16.0--r36_0": "sha256:c6923b8a7f1de911561f7d0e2e7d23061c701a2edeb44fe6d5b9e31316699674", "1.28.0--r42hdfd78af_0": "sha256:c4230ae53aa87880e3351108e66e14bd4358ad66943c8628481afe9aaa370695", "1.30.0--r43hdfd78af_0": "sha256:e3ecf5ccfe7e722208fd73b542117260e7f8ada389c9c33b3fe23b7b388022f2", "1.32.0--r43hdfd78af_0": "sha256:d2f7213f7d03f995b30ab33ca553d50de490c4b5c3c55b309e45153c67255c65"}, "docker": "quay.io/biocontainers/bioconductor-multiclust", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multiclust.
shpc-registry automated BioContainers addition for bioconductor-multiclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multiclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multiclust:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multiclust/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multiclust/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multiclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multiclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multiclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multiclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multiclust-inspect-deffile:

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