---
layout: container
name:  "quay.io/biocontainers/bioconductor-egseadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-egseadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-egseadata/container.yaml"
updated_at: "2024-10-08 03:00:39.668252"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-egseadata"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_1"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-egseadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-egseadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-egseadata", "latest": {"1.30.0--r43hdfd78af_0": "sha256:a85c63f2016c70da7b7b2a3ad5fed453107c0adb4724b85966965a49078903ee"}, "tags": {"1.8.0--r341_0": "sha256:ab88c303fa8b13c56c7eef74819b09b5407913599a28e50d5288109367daf5b6", "1.26.0--r42hdfd78af_0": "sha256:2dca331a2796347a75159f576a19695ea76bb8fa85725f08dcce227af157e79d", "1.25.0--r42hdfd78af_0": "sha256:220466f819a044fa42c65c898348c4116aab8c5d3d6b37324ce03aeabdb3a4cb", "1.22.0--r41hdfd78af_1": "sha256:042be6df784b4cb2cb30f4fb00a5a4c6db1c7e4a49749a109a3dfecf2f9ac0cb", "1.20.0--r41hdfd78af_0": "sha256:484e4ad516f46cf78f339979e592118262d00d467bc45696633a9ff28be37194", "1.18.0--r40hdfd78af_1": "sha256:3f606d1305b4ae8de7de440857ec45bd5b8806aba351de57a670195868637d59", "1.28.0--r43hdfd78af_0": "sha256:064ce7a54e86988b0dc8f9730998120c99e18692c9597a8d5926bd93d85c9ced", "1.30.0--r43hdfd78af_0": "sha256:a85c63f2016c70da7b7b2a3ad5fed453107c0adb4724b85966965a49078903ee"}, "docker": "quay.io/biocontainers/bioconductor-egseadata", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-egseadata.
shpc-registry automated BioContainers addition for bioconductor-egseadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-egseadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-egseadata:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-egseadata/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-egseadata/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-egseadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egseadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-egseadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-egseadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-egseadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-egseadata-inspect-deffile:

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