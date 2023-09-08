---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathprint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathprint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathprint/container.yaml"
updated_at: "2023-09-08 02:56:44.564702"
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
description: "shpc-registry automated BioContainers addition for bioconductor-pathprint"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathprint", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathprint", "latest": {"1.17.0--r40_0": "sha256:41ceed7ba37537e4f726a69912de204099c05cf2aa57fa9fff50e7c7ae6b3983"}, "tags": {"1.6.0--r3.4.1_0": "sha256:743dedfdbd34761c26b2fb24f8113d5cd02cb6788ab45c130388b097fefe890d", "1.17.0--r40_0": "sha256:41ceed7ba37537e4f726a69912de204099c05cf2aa57fa9fff50e7c7ae6b3983", "1.16.0--r36_0": "sha256:5cd8f4e9abd39d18639212cfc8ae35e31c678fd8cae44b176424d2ff870b2061", "1.14.0--r36_1": "sha256:c12e96eaaacd2b388c98f0be0826313db527a6e49743544c634f984463540c16", "1.12.0--r351_0": "sha256:0f72e2296499e7136c50c22861e86c977624397285af2ab56d088631710ade7e", "1.10.4--r351_0": "sha256:bea19fae4fab5a4ddc6890e76566b03a0f405e179b1fbfdeef7b77ebe7f17b07"}, "docker": "quay.io/biocontainers/bioconductor-pathprint", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
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