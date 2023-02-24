---
layout: container
name:  "quay.io/biocontainers/bioconductor-motifmatchr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-motifmatchr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-motifmatchr/container.yaml"
updated_at: "2023-02-24 03:07:11.925580"
latest: "1.20.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-motifmatchr"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-motifmatchr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-motifmatchr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-motifmatchr", "latest": {"1.20.0--r42hc247a5b_0": "sha256:980af276aff49030fcba05838c3b94deb634ba0e70cb293f24a8b281fea1cab9"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:d64446aa52a081605d338ca675df928449a90f483e23382ec785b717f9237bf0", "1.20.0--r42hc247a5b_0": "sha256:980af276aff49030fcba05838c3b94deb634ba0e70cb293f24a8b281fea1cab9", "1.16.0--r41hc247a5b_2": "sha256:3871d2dfede04a7c4fa5e52ecbec51b9b8bbc81cda1a14f80cfe9b1230480c2c", "1.14.0--r41h399db7b_0": "sha256:b96a9b7bc61ec1223dd53e5da7ede2f8bb7e1b7586744a46a231f8bd0de22deb", "1.12.0--r40h399db7b_1": "sha256:055a2d8260d6a965a7872d76381385bd5daff1bd37ae31f4e06e46494d3a8690", "1.10.0--r40h5f743cb_0": "sha256:2ef7b5ed5433f494093af77288a68dfbc079688376a7521aa1e6d59e85031f7d"}, "docker": "quay.io/biocontainers/bioconductor-motifmatchr", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-motifmatchr.
shpc-registry automated BioContainers addition for bioconductor-motifmatchr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-motifmatchr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-motifmatchr:1.20.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-motifmatchr/1.20.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-motifmatchr/1.20.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-motifmatchr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifmatchr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-motifmatchr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-motifmatchr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-motifmatchr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-motifmatchr-inspect-deffile:

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