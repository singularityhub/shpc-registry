---
layout: container
name:  "rocker/r-ver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rocker/r-ver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rocker/r-ver/container.yaml"
updated_at: "2024-04-22 03:44:25.744645"
latest: "4.3.3"
container_url: "https://hub.docker.com/r/rocker/r-ver"
aliases:
 - "R"
 - "Rscript"
versions:
 - "4.2.2"
 - "3.6.3"
 - "4.1.3"
 - "4.0.5"
 - "4.2.3"
 - "4.3.0"
 - "4.3.1"
 - "4.3.2"
 - "4.3.3"
description: "Version-stable build of R"
config: {"docker": "rocker/r-ver", "url": "https://hub.docker.com/r/rocker/r-ver", "maintainer": "@marcodelapierre", "description": "Version-stable build of R", "latest": {"4.3.3": "sha256:1478c0bd3dfc26618eb032fa86ba969bd497d1752786f4b89dcc4c6f98d9f2d8"}, "tags": {"4.2.2": "sha256:e868e617f2adb9740983d5fed65032afa9632308ab94bde02da09182e46f9389", "3.6.3": "sha256:9414f76c5f91f24617b5275b8fe4f4ff1313b3b10698a525cac0063c01f2ca6d", "4.1.3": "sha256:7b41672ff49a216a65068f10267e6ae8ca954ff7146fb40ea5a82266d0ef2fb6", "4.0.5": "sha256:39f3e1bf6613b436b69e5b018273b36067325fb5aec20c4409a40c48af835461", "4.2.3": "sha256:9cbdac7f3737507638bd69ccf88bf9acb72c8b96ee16cba7ad88a0865b74d663", "4.3.0": "sha256:090046ca60f4d1c177616b77ea23f1d4ad7316c864bf27b26b2fa10f65bf00c5", "4.3.1": "sha256:f5f2d67b72a0fd0912222c2cf8eedfff809195775039e8f1701665322b1a8089", "4.3.2": "sha256:74e06e98f2b03d1b086caec243add1ea964f40a59b99195cfd3e99dd1264d632", "4.3.3": "sha256:1478c0bd3dfc26618eb032fa86ba969bd497d1752786f4b89dcc4c6f98d9f2d8"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"R": "/usr/local/bin/R", "Rscript": "/usr/local/bin/Rscript"}}
---

This module is a singularity container wrapper for rocker/r-ver.
Version-stable build of R
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rocker/r-ver
```

Or a specific version:

```bash
$ shpc install rocker/r-ver:4.3.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/r-ver/4.3.3
$ module help rocker/r-ver/4.3.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R

```bash
$ singularity exec <container> /usr/local/bin/R
$ podman run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript

```bash
$ singularity exec <container> /usr/local/bin/Rscript
$ podman run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
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