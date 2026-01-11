---
layout: container
name:  "quay.io/biocontainers/bioconductor-bioqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bioqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bioqc/container.yaml"
updated_at: "2026-01-11 03:55:24.502409"
latest: "1.34.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bioqc"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.16.0--r40h5f743cb_0"
 - "1.14.0--r36he1b5a44_0"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_1"
 - "1.34.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bioqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bioqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bioqc", "latest": {"1.34.0--r44he5774e6_0": "sha256:2ada05ab0f597d6c226ee9e045b3dc3ef2ee80195d1f63bf8d08a959d9763e70"}, "tags": {"1.8.0--r341hfc679d8_0": "sha256:c0f1fbd70b5f4cd57e6425ba4f20f0588c98e8c5e5369db2f073d502376e599b", "1.22.0--r41hc247a5b_2": "sha256:cc76208d641da94003e4e17ade26d8bc16406dab93cd512f08a8495fe20f011e", "1.20.0--r41h399db7b_0": "sha256:bece82b25a9de255b124d4ffaa03496897b3f7ba76791f4cac9d26d4d976906f", "1.18.0--r40h399db7b_1": "sha256:f061676d3e48a2fa67efa4aaba80896960308d341aaa9eaf5e27a5d6ae5a1221", "1.16.0--r40h5f743cb_0": "sha256:9767c349029687a2e147b7f2f220db6bf5706cb3c2a3a51e97373f53223e12c6", "1.14.0--r36he1b5a44_0": "sha256:701f78b9da9aa5b23cc0c7305ce01c071f3d24b4b755ddf91b7ea537093d6b59", "1.26.0--r42hc247a5b_0": "sha256:0398c2d3c8cd78d37d4a4d4f4e006318a4970472c3e697ed3a3dc4558bd84502", "1.26.0--r42hf17093f_1": "sha256:256fccf4e7eb0832f646361010cc487263b4a80f1ef23d12f70173b34dacb73e", "1.28.0--r43hf17093f_0": "sha256:7f002d272241004f6341c37bf29048e1ad136af504a88832b7bd961c914b7d70", "1.30.0--r43hf17093f_0": "sha256:35bdde1027efba0ceb6602bea8918ed43b2119a25d8b26cede90be377536b06a", "1.30.0--r43hf17093f_1": "sha256:eb3a66c0b873ac8fbbef5c85dc6f9b7c1d2166bf8a6a36929fdb9700983b1309", "1.34.0--r44he5774e6_0": "sha256:2ada05ab0f597d6c226ee9e045b3dc3ef2ee80195d1f63bf8d08a959d9763e70"}, "docker": "quay.io/biocontainers/bioconductor-bioqc", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bioqc.
shpc-registry automated BioContainers addition for bioconductor-bioqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bioqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bioqc:1.34.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bioqc/1.34.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-bioqc/1.34.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bioqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bioqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bioqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bioqc-inspect-deffile:

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