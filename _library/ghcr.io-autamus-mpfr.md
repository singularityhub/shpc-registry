---
layout: container
name:  "ghcr.io/autamus/mpfr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mpfr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/mpfr/container.yaml"
updated_at: "2023-10-09 03:29:20.473026"
latest: "4.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/mpfr"

versions:
 - "4.1.0"
 - "latest"
description: "The MPFR library is a C library for multiple-precision floating-point computations with correct rounding."
config: {"docker": "ghcr.io/autamus/mpfr", "url": "https://github.com/orgs/autamus/packages/container/package/mpfr", "maintainer": "@vsoch", "description": "The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.", "latest": {"4.1.0": "sha256:0488b3e49fd691fd513eb626715007628a90ef32fe7ec48b790b0e0a9b97b1de"}, "tags": {"4.1.0": "sha256:0488b3e49fd691fd513eb626715007628a90ef32fe7ec48b790b0e0a9b97b1de", "latest": "sha256:0488b3e49fd691fd513eb626715007628a90ef32fe7ec48b790b0e0a9b97b1de"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mpfr.
The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mpfr
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mpfr:4.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mpfr/4.1.0
$ module help ghcr.io/autamus/mpfr/4.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mpfr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mpfr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mpfr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mpfr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mpfr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mpfr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mpfr

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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