---
layout: container
name:  "quay.io/biocontainers/bioconductor-prize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prize/container.yaml"
updated_at: "2025-02-28 03:38:25.432192"
latest: "1.17.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prize"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.17.0--r40_0"
 - "1.16.0--r36_0"
 - "1.14.0--r36_1"
 - "1.12.1--r351_0"
 - "1.10.0--r351_0"
 - "1.10.0--r341_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prize", "latest": {"1.17.0--r40_0": "sha256:32f357c04d9fe964624c36b7497f0a259e0816d9eb5aae7f39957b6c704c1204"}, "tags": {"1.8.0--r3.4.1_0": "sha256:0180089760669bfa964218374eddbd0cc677bf539cbc8c83c127b6582f8b7ee1", "1.17.0--r40_0": "sha256:32f357c04d9fe964624c36b7497f0a259e0816d9eb5aae7f39957b6c704c1204", "1.16.0--r36_0": "sha256:70ad5695d7b69ed6d1435004ccee4998a6d856c4b7ebb932ac43ab503d96830a", "1.14.0--r36_1": "sha256:ea938e371dc8c1c7f707ae48e184c2f63334991034ccc8d6111f65ec6bbb8e1a", "1.12.1--r351_0": "sha256:dd16e02b4bad81b5a775d876c3bc788eca233ff99f359a61b85d147aa29d84df", "1.10.0--r351_0": "sha256:3e3cd1f8d1e025fe68c5af4f6305be4e495c3b2afbf0401b8871bdc1eaf7ef81", "1.10.0--r341_0": "sha256:9f167ccb021bbe9e924c98f4effb5e098b9eda5b49d7881977b6ab0ce9753a86"}, "docker": "quay.io/biocontainers/bioconductor-prize", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prize.
shpc-registry automated BioContainers addition for bioconductor-prize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prize:1.17.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prize/1.17.0--r40_0
$ module help quay.io/biocontainers/bioconductor-prize/1.17.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prize-inspect-deffile:

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