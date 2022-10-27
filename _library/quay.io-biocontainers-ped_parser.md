---
layout: container
name:  "quay.io/biocontainers/ped_parser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ped_parser/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ped_parser/container.yaml"
updated_at: "2022-10-27 00:31:04.507357"
latest: "1.6.6--py_2"
container_url: "https://biocontainers.pro/tools/ped_parser"
aliases:
 - "ped_parser"
versions:
 - "1.6.6--py_2"
description: "shpc-registry automated BioContainers addition for ped_parser"
config: {"url": "https://biocontainers.pro/tools/ped_parser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ped_parser", "latest": {"1.6.6--py_2": "sha256:0462154a5b51e8539cf23492ce01f8858e03cbf23e803b8931c62fab9d7a2d3b"}, "tags": {"1.6.6--py_2": "sha256:0462154a5b51e8539cf23492ce01f8858e03cbf23e803b8931c62fab9d7a2d3b"}, "docker": "quay.io/biocontainers/ped_parser", "aliases": {"ped_parser": "/usr/local/bin/ped_parser"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ped_parser.
shpc-registry automated BioContainers addition for ped_parser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ped_parser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ped_parser:1.6.6--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ped_parser/1.6.6--py_2
$ module help quay.io/biocontainers/ped_parser/1.6.6--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ped_parser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ped_parser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ped_parser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ped_parser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ped_parser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ped_parser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ped_parser

```bash
$ singularity exec <container> /usr/local/bin/ped_parser
$ podman run --it --rm --entrypoint /usr/local/bin/ped_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ped_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
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