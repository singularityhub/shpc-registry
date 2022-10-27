---
layout: container
name:  "quay.io/biocontainers/flaimapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flaimapper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/flaimapper/container.yaml"
updated_at: "2022-10-27 00:35:11.992291"
latest: "3.0.0--py_2"
container_url: "https://biocontainers.pro/tools/flaimapper"
aliases:
 - "flaimapper"
 - "sslm2sam"
versions:
 - "3.0.0--py_2"
description: "shpc-registry automated BioContainers addition for flaimapper"
config: {"url": "https://biocontainers.pro/tools/flaimapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flaimapper", "latest": {"3.0.0--py_2": "sha256:fce1757d222c74e3fee7f9f998b81c97a95195ae2802a900920a2d47a01fa3a9"}, "tags": {"3.0.0--py_2": "sha256:fce1757d222c74e3fee7f9f998b81c97a95195ae2802a900920a2d47a01fa3a9"}, "docker": "quay.io/biocontainers/flaimapper", "aliases": {"flaimapper": "/usr/local/bin/flaimapper", "sslm2sam": "/usr/local/bin/sslm2sam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flaimapper.
shpc-registry automated BioContainers addition for flaimapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flaimapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flaimapper:3.0.0--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flaimapper/3.0.0--py_2
$ module help quay.io/biocontainers/flaimapper/3.0.0--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flaimapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flaimapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flaimapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flaimapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flaimapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flaimapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flaimapper

```bash
$ singularity exec <container> /usr/local/bin/flaimapper
$ podman run --it --rm --entrypoint /usr/local/bin/flaimapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flaimapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sslm2sam

```bash
$ singularity exec <container> /usr/local/bin/sslm2sam
$ podman run --it --rm --entrypoint /usr/local/bin/sslm2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sslm2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
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