---
layout: container
name:  "ghcr.io/autamus/trilinos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/trilinos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/trilinos/container.yaml"
updated_at: "2023-12-16 03:12:03.572225"
latest: "13.2.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/trilinos"

versions:
 - "13.0.1"
 - "13.2.0"
 - "latest"
description: "The Trilinos Project is an effort to develop algorithms and enabling technologies within an object-oriented software framework for the solution of large-scale, complex multi-physics engineering and scientific problems. A unique design feature of Trilinos is its focus on packages."
config: {"docker": "ghcr.io/autamus/trilinos", "url": "https://github.com/orgs/autamus/packages/container/package/trilinos", "maintainer": "@vsoch", "description": "The Trilinos Project is an effort to develop algorithms and enabling technologies within an object-oriented software framework for the solution of large-scale, complex multi-physics engineering and scientific problems. A unique design feature of Trilinos is its focus on packages.", "latest": {"13.2.0": "sha256:c5f4396266806c4bd8a12fe04a2d25aafc0ac034e4c2b1d965d2cbbaef5a31c8"}, "tags": {"13.0.1": "sha256:cef95b0d22c12d952c3100caa85cb12fd8f976aa4e34ed584f9e3d3c1c4340e7", "13.2.0": "sha256:c5f4396266806c4bd8a12fe04a2d25aafc0ac034e4c2b1d965d2cbbaef5a31c8", "latest": "sha256:c5f4396266806c4bd8a12fe04a2d25aafc0ac034e4c2b1d965d2cbbaef5a31c8"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/trilinos.
The Trilinos Project is an effort to develop algorithms and enabling technologies within an object-oriented software framework for the solution of large-scale, complex multi-physics engineering and scientific problems. A unique design feature of Trilinos is its focus on packages.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/trilinos
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/trilinos:13.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/trilinos/13.2.0
$ module help ghcr.io/autamus/trilinos/13.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trilinos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trilinos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trilinos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trilinos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trilinos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trilinos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### trilinos

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