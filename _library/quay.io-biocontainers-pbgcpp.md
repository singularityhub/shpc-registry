---
layout: container
name:  "quay.io/biocontainers/pbgcpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbgcpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbgcpp/container.yaml"
updated_at: "2024-05-06 18:48:42.150851"
latest: "2.0.2--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/pbgcpp"
aliases:
 - "gcpp"
versions:
 - "2.0.2--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for pbgcpp"
config: {"url": "https://biocontainers.pro/tools/pbgcpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbgcpp", "latest": {"2.0.2--h9ee0642_1": "sha256:85d2c5e1d3927ab3bf76ce8ad0ed36e81724b464c7d1a7fe000eaf56df95683e"}, "tags": {"2.0.2--h9ee0642_1": "sha256:85d2c5e1d3927ab3bf76ce8ad0ed36e81724b464c7d1a7fe000eaf56df95683e"}, "docker": "quay.io/biocontainers/pbgcpp", "aliases": {"gcpp": "/usr/local/bin/gcpp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbgcpp.
shpc-registry automated BioContainers addition for pbgcpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbgcpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbgcpp:2.0.2--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbgcpp/2.0.2--h9ee0642_1
$ module help quay.io/biocontainers/pbgcpp/2.0.2--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbgcpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbgcpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbgcpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbgcpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbgcpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbgcpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gcpp

```bash
$ singularity exec <container> /usr/local/bin/gcpp
$ podman run --it --rm --entrypoint /usr/local/bin/gcpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcpp   -v ${PWD} -w ${PWD} <container> -c " $@"
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