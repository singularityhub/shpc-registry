---
layout: container
name:  "quay.io/biocontainers/pbpigeon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbpigeon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbpigeon/container.yaml"
updated_at: "2023-07-04 03:49:16.508793"
latest: "1.0.0--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/pbpigeon"
aliases:
 - "pigeon"
versions:
 - "0.1.2--hdfd78af_0"
 - "1.0.0--h9f5acd7_1"
 - "1.0.0--h4ac6f70_2"
description: "singularity registry hpc automated addition for pbpigeon"
config: {"url": "https://biocontainers.pro/tools/pbpigeon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbpigeon", "latest": {"1.0.0--h4ac6f70_2": "sha256:13ff2f6b2c421ea7c6283bfff4e4841291383e58b35c1c4a079f43cc798e861b"}, "tags": {"0.1.2--hdfd78af_0": "sha256:15bbdf5c521e568fb265799e162856315dbaf42809827fb8e4175a57e521466e", "1.0.0--h9f5acd7_1": "sha256:957abc67c1a77c8a814710e36dc8ff2d1a3b5be2d27ab0768d4ba6de7804107f", "1.0.0--h4ac6f70_2": "sha256:13ff2f6b2c421ea7c6283bfff4e4841291383e58b35c1c4a079f43cc798e861b"}, "docker": "quay.io/biocontainers/pbpigeon", "aliases": {"pigeon": "/usr/local/bin/pigeon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbpigeon.
singularity registry hpc automated addition for pbpigeon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbpigeon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbpigeon:1.0.0--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbpigeon/1.0.0--h4ac6f70_2
$ module help quay.io/biocontainers/pbpigeon/1.0.0--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbpigeon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbpigeon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbpigeon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbpigeon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbpigeon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbpigeon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pigeon

```bash
$ singularity exec <container> /usr/local/bin/pigeon
$ podman run --it --rm --entrypoint /usr/local/bin/pigeon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigeon   -v ${PWD} -w ${PWD} <container> -c " $@"
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