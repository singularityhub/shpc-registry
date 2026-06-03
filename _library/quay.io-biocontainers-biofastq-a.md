---
layout: container
name:  "quay.io/biocontainers/biofastq-a"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biofastq-a/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biofastq-a/container.yaml"
updated_at: "2026-06-03 07:18:21.419504"
latest: "2.2.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/biofastq-a"
aliases:
 - "biofastq-a"
versions:
 - "2.2.0--h4349ce8_0"
description: "singularity registry hpc automated addition for biofastq-a"
config: {"url": "https://biocontainers.pro/tools/biofastq-a", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biofastq-a", "latest": {"2.2.0--h4349ce8_0": "sha256:89ddc22438578f1d0a6bd73c32d7f1da3309e031eb729bbd73fe3acdea4cae6d"}, "tags": {"2.2.0--h4349ce8_0": "sha256:89ddc22438578f1d0a6bd73c32d7f1da3309e031eb729bbd73fe3acdea4cae6d"}, "docker": "quay.io/biocontainers/biofastq-a", "aliases": {"biofastq-a": "/usr/local/bin/biofastq-a"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biofastq-a.
singularity registry hpc automated addition for biofastq-a
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biofastq-a
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biofastq-a:2.2.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biofastq-a/2.2.0--h4349ce8_0
$ module help quay.io/biocontainers/biofastq-a/2.2.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biofastq-a-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biofastq-a-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biofastq-a-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biofastq-a-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biofastq-a-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biofastq-a-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biofastq-a

```bash
$ singularity exec <container> /usr/local/bin/biofastq-a
$ podman run --it --rm --entrypoint /usr/local/bin/biofastq-a   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biofastq-a   -v ${PWD} -w ${PWD} <container> -c " $@"
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