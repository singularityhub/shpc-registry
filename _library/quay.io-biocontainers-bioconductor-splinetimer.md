---
layout: container
name:  "quay.io/biocontainers/bioconductor-splinetimer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-splinetimer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-splinetimer/container.yaml"
updated_at: "2023-10-26 04:02:52.282253"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-splinetimer"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-splinetimer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-splinetimer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-splinetimer", "latest": {"1.28.0--r43hdfd78af_0": "sha256:0ac4888eaafe6643de5e8d9887fb8cc2c2bc4caddc1550bb8348c0434aa71c61"}, "tags": {"1.8.0--r341_0": "sha256:da73e43954943a3dc7f7191a134ea6cd0e53d10b53ca12a4ec876b2c74496df4", "1.22.0--r41hdfd78af_0": "sha256:d73e4a773a65bfcdb9df3e058efb491f3be8c68723ed15fb0d39c723f02a8bce", "1.20.0--r41hdfd78af_0": "sha256:ff90262471cb6da915fcc3ba97e98ab4f04f245763426efee5086deea25c4d6d", "1.18.0--r40hdfd78af_1": "sha256:032d7ad0e191fd5031e2e5a74d8821753c0b4ab793bca887beea45ae061bb85a", "1.16.0--r40_0": "sha256:03b55d076ac7d9cf372d97e56bfa0c2e8c92f3933be1b9cff39e13b4c714af9b", "1.14.0--r36_1": "sha256:954b9c70c0ba293aae871f36ae1535c48f2795e898cfa3cfbd4e2a2cc9b00e67", "1.26.0--r42hdfd78af_0": "sha256:5f79f76cf5b80f6eac74e39fbeac1a2cb89f7a7694a3d0fb04ac26c998ab6840", "1.28.0--r43hdfd78af_0": "sha256:0ac4888eaafe6643de5e8d9887fb8cc2c2bc4caddc1550bb8348c0434aa71c61"}, "docker": "quay.io/biocontainers/bioconductor-splinetimer", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-splinetimer.
shpc-registry automated BioContainers addition for bioconductor-splinetimer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-splinetimer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-splinetimer:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-splinetimer/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-splinetimer/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-splinetimer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splinetimer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-splinetimer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-splinetimer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-splinetimer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-splinetimer-inspect-deffile:

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