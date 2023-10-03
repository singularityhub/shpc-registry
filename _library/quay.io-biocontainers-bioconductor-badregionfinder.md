---
layout: container
name:  "quay.io/biocontainers/bioconductor-badregionfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-badregionfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-badregionfinder/container.yaml"
updated_at: "2023-10-03 02:45:34.098145"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-badregionfinder"
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
description: "shpc-registry automated BioContainers addition for bioconductor-badregionfinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-badregionfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-badregionfinder", "latest": {"1.28.0--r43hdfd78af_0": "sha256:af25869fed3320d32a1b72525e31dac6fe712bd371af9c0080ea87cf46fcb723"}, "tags": {"1.8.0--r341_0": "sha256:cd16612fbac41881de06c8b36aca2c60dc69e9eff93e0070553f52b1e52756e1", "1.26.0--r42hdfd78af_0": "sha256:82d5b28aaf0cb6c42378384d9054f4cf4c092eb0eb16341de565270de6b60b3a", "1.22.0--r41hdfd78af_0": "sha256:304a4be258784b24b74efc048bb8b315eda4a604d68fdf71505ae27b5602350b", "1.20.0--r41hdfd78af_0": "sha256:03cd56dc1ffe278f5038a1cbb74280b574b2ed8eace78278b9a49c3189c7603f", "1.18.0--r40hdfd78af_1": "sha256:ece4f27899cd90075a26fde576b33a3c3887eb5e0c8e51f4207fa0d9dea1fb83", "1.16.0--r40_0": "sha256:8865b21097369e1598daa08f2f5417070adf45fbe06abbb542c000290a964303", "1.28.0--r43hdfd78af_0": "sha256:af25869fed3320d32a1b72525e31dac6fe712bd371af9c0080ea87cf46fcb723"}, "docker": "quay.io/biocontainers/bioconductor-badregionfinder", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-badregionfinder.
shpc-registry automated BioContainers addition for bioconductor-badregionfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-badregionfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-badregionfinder:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-badregionfinder/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-badregionfinder/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-badregionfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-badregionfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-badregionfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-badregionfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-badregionfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-badregionfinder-inspect-deffile:

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