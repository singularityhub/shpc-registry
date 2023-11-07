---
layout: container
name:  "quay.io/biocontainers/bioconductor-deformats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deformats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deformats/container.yaml"
updated_at: "2023-11-07 02:53:27.442943"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deformats"
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
description: "shpc-registry automated BioContainers addition for bioconductor-deformats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deformats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deformats", "latest": {"1.28.0--r43hdfd78af_0": "sha256:648fd41fa524129cc63cab4d514c49e1d37d0b1a9cfa13a4aecb768e73ec3f9b"}, "tags": {"1.8.0--r341_0": "sha256:0b232cc51141e4f5bc5f7b7646cab9d06787a09de6e4e9b83803106f574375d7", "1.26.0--r42hdfd78af_0": "sha256:50beda78f2ad745c2b9af43056468f6ff0a9004969a5c893f50fdbc45bb2914c", "1.22.0--r41hdfd78af_0": "sha256:1226eba7ea1c4abde32e455871ced766165e8aa1c9c0dfd742c165a2d052a3a4", "1.20.0--r41hdfd78af_0": "sha256:c21e68eed2a70fa68369ddc068ae534bddc5f9b5f0c9daaad8084a5c2f9d98a1", "1.18.0--r40hdfd78af_1": "sha256:a1e3e820e951d50a1b6d0377cc909398579aed2d7aebbdab3472c0aa6f542675", "1.16.0--r40_0": "sha256:c8d9e9185c6d876c731b52948e7c956549de87e27ed14996da5eaffedc4b2a3d", "1.28.0--r43hdfd78af_0": "sha256:648fd41fa524129cc63cab4d514c49e1d37d0b1a9cfa13a4aecb768e73ec3f9b"}, "docker": "quay.io/biocontainers/bioconductor-deformats", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deformats.
shpc-registry automated BioContainers addition for bioconductor-deformats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deformats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deformats:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deformats/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deformats/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deformats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deformats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deformats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deformats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deformats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deformats-inspect-deffile:

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