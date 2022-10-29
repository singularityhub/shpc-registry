---
layout: container
name:  "quay.io/biocontainers/r-gamlss.dist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gamlss.dist/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-gamlss.dist/container.yaml"
updated_at: "2022-10-29 05:57:57.174126"
latest: "5.0_0--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-gamlss.dist"
aliases:
 - "tclsh8.5"
 - "uconv"
 - "wish8.5"
versions:
 - "5.0_0--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-gamlss.dist"
config: {"url": "https://biocontainers.pro/tools/r-gamlss.dist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gamlss.dist", "latest": {"5.0_0--r3.3.2_0": "sha256:9a9880c59652eccdda42d19404ed6ae5aaebd7f2b8d05a260404b571c44e9c43"}, "tags": {"5.0_0--r3.3.2_0": "sha256:9a9880c59652eccdda42d19404ed6ae5aaebd7f2b8d05a260404b571c44e9c43"}, "docker": "quay.io/biocontainers/r-gamlss.dist", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "uconv": "/usr/local/bin/uconv", "wish8.5": "/usr/local/bin/wish8.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gamlss.dist.
shpc-registry automated BioContainers addition for r-gamlss.dist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gamlss.dist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gamlss.dist:5.0_0--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gamlss.dist/5.0_0--r3.3.2_0
$ module help quay.io/biocontainers/r-gamlss.dist/5.0_0--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gamlss.dist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gamlss.dist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gamlss.dist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gamlss.dist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gamlss.dist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gamlss.dist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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