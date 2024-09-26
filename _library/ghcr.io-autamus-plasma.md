---
layout: container
name:  "ghcr.io/autamus/plasma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/plasma/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/plasma/container.yaml"
updated_at: "2024-09-26 03:39:25.148835"
latest: "22.9.29"
container_url: "https://github.com/orgs/autamus/packages/container/package/plasma"
aliases:
 - "plasmatest"
versions:
 - "20.9.20"
 - "21.8.29"
 - "latest"
 - "22.9.29"
description: "Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors."
config: {"docker": "ghcr.io/autamus/plasma", "url": "https://github.com/orgs/autamus/packages/container/package/plasma", "maintainer": "@vsoch", "description": "Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors.", "latest": {"22.9.29": "sha256:efaad7801d4a4e3da5f53cc6e5d4432e087a15f0f92385aff4986cf114d94152"}, "tags": {"20.9.20": "sha256:a4490385c99235b80515bc9f0c2e26ce236f74087df82f114665aba72668e516", "21.8.29": "sha256:0115c8cecced1fdffdadc8417a5a88cdbd887ffd487774ee80278bca2a1b0b91", "latest": "sha256:efaad7801d4a4e3da5f53cc6e5d4432e087a15f0f92385aff4986cf114d94152", "22.9.29": "sha256:efaad7801d4a4e3da5f53cc6e5d4432e087a15f0f92385aff4986cf114d94152"}, "aliases": {"plasmatest": "/opt/view/bin/plasmatest"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/plasma.
Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/plasma
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/plasma:22.9.29
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/plasma/22.9.29
$ module help ghcr.io/autamus/plasma/22.9.29
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plasmatest

```bash
$ singularity exec <container> /opt/view/bin/plasmatest
$ podman run --it --rm --entrypoint /opt/view/bin/plasmatest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/plasmatest   -v ${PWD} -w ${PWD} <container> -c " $@"
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