---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathprint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathprint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathprint/container.yaml"
updated_at: "2025-01-01 03:05:48.256442"
latest: "1.17.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathprint"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.6.0--r3.4.1_0"
 - "1.17.0--r40_0"
 - "1.16.0--r36_0"
 - "1.14.0--r36_1"
 - "1.12.0--r351_0"
 - "1.10.4--r351_0"
 - "1.10.4--r341_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathprint"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathprint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathprint", "latest": {"1.17.0--r40_0": "sha256:41ceed7ba37537e4f726a69912de204099c05cf2aa57fa9fff50e7c7ae6b3983"}, "tags": {"1.6.0--r3.4.1_0": "sha256:06b89ae2ebf334403e2e6b7a731d0df72fc6bf979085588780295a2bae4983b7", "1.17.0--r40_0": "sha256:41ceed7ba37537e4f726a69912de204099c05cf2aa57fa9fff50e7c7ae6b3983", "1.16.0--r36_0": "sha256:ec1d5a12a2a58e06ad4ee622ed9b94127e8606dc3f48e6d5f283e424f656a283", "1.14.0--r36_1": "sha256:6ba0f07da78908d4dd8326d4cbe2d19fc5f2761ef4726b932b85ecf93c2d4c25", "1.12.0--r351_0": "sha256:c7b5795ebf7fdf41bbe01f7040a56aeeaac83640fe254e43d7a3f9234853c03e", "1.10.4--r351_0": "sha256:b7c51870653a62026c63ca05f959cb74ac22c8793f3d1a9814f24f56dd0c05be", "1.10.4--r341_0": "sha256:7552a74d1cccb5ce1e1fcb6478dc07ec6a7cbe81d3bdb777f9151eaf3a22fe60"}, "docker": "quay.io/biocontainers/bioconductor-pathprint", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathprint.
shpc-registry automated BioContainers addition for bioconductor-pathprint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathprint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathprint:1.17.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathprint/1.17.0--r40_0
$ module help quay.io/biocontainers/bioconductor-pathprint/1.17.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathprint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathprint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathprint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathprint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathprint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathprint-inspect-deffile:

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