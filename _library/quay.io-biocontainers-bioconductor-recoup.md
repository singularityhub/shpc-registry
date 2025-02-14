---
layout: container
name:  "quay.io/biocontainers/bioconductor-recoup"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-recoup/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-recoup/container.yaml"
updated_at: "2025-02-14 03:03:25.797482"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-recoup"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-recoup"
config: {"url": "https://biocontainers.pro/tools/bioconductor-recoup", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-recoup", "latest": {"1.34.0--r44hdfd78af_0": "sha256:658749a92f36548a33c2834d6d61f5263fce03c0187b8d48ad700278068177a9"}, "tags": {"1.8.0--r341_0": "sha256:48f13e9e049f6aecf2d86b1cf48716a40751357e5d89f7840acd6d1b02368037", "1.26.0--r42hdfd78af_0": "sha256:b362f1532234b8f0cf67b7ed85554092bd5c9b7b63f87d5c7796ff418087afb0", "1.22.0--r41hdfd78af_0": "sha256:932f54baa4599191f092e74c7b72788ec64717aff0fe3d5e6928e7fe6d2fac2e", "1.20.0--r41hdfd78af_0": "sha256:f402a4a2f8a3938fcf8fb11075150bea41082f919083255ae8b731813506be77", "1.18.0--r40hdfd78af_1": "sha256:bb3b3a7ac32ac5f597fa64f2612be0665e78eb9bec09e65b1f5a964fd61e9c01", "1.16.0--r40_0": "sha256:a659ea0b83d3c9cc1a185e5045152e4d1882ffac4f9b3b03c01f58bbf2a27ccc", "1.28.0--r43hdfd78af_0": "sha256:8056aea1b52ba415a941c96c5779abfdef693fff6acf17c7e2c93b375200c57c", "1.30.0--r43hdfd78af_0": "sha256:8cc55ec605fdb16a90dadc556763582d03dc7f6ba9c4c8329ea4ca4da9d582eb", "1.34.0--r44hdfd78af_0": "sha256:658749a92f36548a33c2834d6d61f5263fce03c0187b8d48ad700278068177a9"}, "docker": "quay.io/biocontainers/bioconductor-recoup", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-recoup.
shpc-registry automated BioContainers addition for bioconductor-recoup
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-recoup
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-recoup:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-recoup/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-recoup/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-recoup-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-recoup-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-recoup-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-recoup-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-recoup-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-recoup-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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