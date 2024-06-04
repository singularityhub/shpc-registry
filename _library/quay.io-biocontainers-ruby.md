---
layout: container
name:  "quay.io/biocontainers/ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ruby/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ruby/container.yaml"
updated_at: "2024-06-04 03:12:04.283884"
latest: "2.2.3--1"
container_url: "https://biocontainers.pro/tools/ruby"

versions:
 - "2.2.3--1"
description: "shpc-registry automated BioContainers addition for ruby"
config: {"url": "https://biocontainers.pro/tools/ruby", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ruby", "latest": {"2.2.3--1": "sha256:c7015376a384281c15601d1224703b6c986d5bb318fddc3b8eb938969a04e44a"}, "tags": {"2.2.3--1": "sha256:c7015376a384281c15601d1224703b6c986d5bb318fddc3b8eb938969a04e44a"}, "docker": "quay.io/biocontainers/ruby"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ruby.
shpc-registry automated BioContainers addition for ruby
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ruby
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ruby:2.2.3--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ruby/2.2.3--1
$ module help quay.io/biocontainers/ruby/2.2.3--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ruby-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ruby-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ruby-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ruby-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ruby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruby-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ruby

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