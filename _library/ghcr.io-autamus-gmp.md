---
layout: container
name:  "ghcr.io/autamus/gmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gmp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/gmp/container.yaml"
updated_at: "2024-09-02 04:15:22.914151"
latest: "6.2.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/gmp"
aliases:
 - "curl"
versions:
 - "6.2.1"
 - "latest"
description: "GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers."
config: {"docker": "ghcr.io/autamus/gmp", "url": "https://github.com/orgs/autamus/packages/container/package/gmp", "maintainer": "@vsoch", "description": "GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers.", "latest": {"6.2.1": "sha256:bc56a6c4d19be34d5ad9bc0533a281fd203565faad1d29640eb5b2cae85e59ef"}, "tags": {"6.2.1": "sha256:bc56a6c4d19be34d5ad9bc0533a281fd203565faad1d29640eb5b2cae85e59ef", "latest": "sha256:bc56a6c4d19be34d5ad9bc0533a281fd203565faad1d29640eb5b2cae85e59ef"}, "aliases": {"curl": "/opt/view/bin/curl"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gmp.
GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gmp
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gmp:6.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gmp/6.2.1
$ module help ghcr.io/autamus/gmp/6.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### curl

```bash
$ singularity exec <container> /opt/view/bin/curl
$ podman run --it --rm --entrypoint /opt/view/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
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