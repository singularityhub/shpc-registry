---
layout: container
name:  "quay.io/biocontainers/micro_razers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/micro_razers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/micro_razers/container.yaml"
updated_at: "2023-12-24 03:06:45.759356"
latest: "1.0.6--h6dccd9a_7"
container_url: "https://biocontainers.pro/tools/micro_razers"
aliases:
 - "micro_razers"
versions:
 - "1.0.6--h19e8d03_5"
 - "1.0.6--h6dccd9a_7"
description: "shpc-registry automated BioContainers addition for micro_razers"
config: {"url": "https://biocontainers.pro/tools/micro_razers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for micro_razers", "latest": {"1.0.6--h6dccd9a_7": "sha256:d9707b9769187165acc3f51a8ff0f401817f332af5d8e91daaec3274022cc7b2"}, "tags": {"1.0.6--h19e8d03_5": "sha256:6b722f7caeadfedb9649b97cf68f519bb9f2af4974a83e2c917cef72d2b97851", "1.0.6--h6dccd9a_7": "sha256:d9707b9769187165acc3f51a8ff0f401817f332af5d8e91daaec3274022cc7b2"}, "docker": "quay.io/biocontainers/micro_razers", "aliases": {"micro_razers": "/usr/local/bin/micro_razers"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/micro_razers.
shpc-registry automated BioContainers addition for micro_razers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/micro_razers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/micro_razers:1.0.6--h6dccd9a_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/micro_razers/1.0.6--h6dccd9a_7
$ module help quay.io/biocontainers/micro_razers/1.0.6--h6dccd9a_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### micro_razers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### micro_razers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### micro_razers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### micro_razers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### micro_razers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### micro_razers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### micro_razers

```bash
$ singularity exec <container> /usr/local/bin/micro_razers
$ podman run --it --rm --entrypoint /usr/local/bin/micro_razers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/micro_razers   -v ${PWD} -w ${PWD} <container> -c " $@"
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