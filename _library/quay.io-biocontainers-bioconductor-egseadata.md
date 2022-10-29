---
layout: container
name:  "quay.io/biocontainers/bioconductor-egseadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-egseadata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-egseadata/container.yaml"
updated_at: "2022-10-29 08:01:04.717651"
latest: "1.8.0--r341_0"
container_url: "https://biocontainers.pro/tools/bioconductor-egseadata"
aliases:
 - ".bioconductor-egseadata-post-link.sh"
 - ".bioconductor-egseadata-pre-unlink.sh"
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
description: "shpc-registry automated BioContainers addition for bioconductor-egseadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-egseadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-egseadata", "latest": {"1.8.0--r341_0": "sha256:9a1deec659e6be10d7709627b78a06dd8ce8e5526c0f831ec4891c21c126832c"}, "tags": {"1.8.0--r341_0": "sha256:9a1deec659e6be10d7709627b78a06dd8ce8e5526c0f831ec4891c21c126832c"}, "docker": "quay.io/biocontainers/bioconductor-egseadata", "aliases": {".bioconductor-egseadata-post-link.sh": "/usr/local/bin/.bioconductor-egseadata-post-link.sh", ".bioconductor-egseadata-pre-unlink.sh": "/usr/local/bin/.bioconductor-egseadata-pre-unlink.sh", "wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-egseadata.
shpc-registry automated BioContainers addition for bioconductor-egseadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-egseadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-egseadata:1.8.0--r341_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-egseadata/1.8.0--r341_0
$ module help quay.io/biocontainers/bioconductor-egseadata/1.8.0--r341_0
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


#### .bioconductor-egseadata-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-egseadata-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-egseadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-egseadata-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-egseadata-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-egseadata-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-egseadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-egseadata-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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