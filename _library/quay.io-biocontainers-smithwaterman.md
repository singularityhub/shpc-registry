---
layout: container
name:  "quay.io/biocontainers/smithwaterman"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smithwaterman/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smithwaterman/container.yaml"
updated_at: "2025-10-01 03:57:09.565266"
latest: "1.0.0--h9948957_0"
container_url: "https://biocontainers.pro/tools/smithwaterman"
aliases:
 - "smithwaterman"
versions:
 - "1.0.0--h9948957_0"
description: "singularity registry hpc automated addition for smithwaterman"
config: {"url": "https://biocontainers.pro/tools/smithwaterman", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for smithwaterman", "latest": {"1.0.0--h9948957_0": "sha256:87cc7439f8312e49192dc934bad7f55ce66140c97f1d888662b50fe25b851d8e"}, "tags": {"1.0.0--h9948957_0": "sha256:87cc7439f8312e49192dc934bad7f55ce66140c97f1d888662b50fe25b851d8e"}, "docker": "quay.io/biocontainers/smithwaterman", "aliases": {"smithwaterman": "/usr/local/bin/smithwaterman"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smithwaterman.
singularity registry hpc automated addition for smithwaterman
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smithwaterman
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smithwaterman:1.0.0--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smithwaterman/1.0.0--h9948957_0
$ module help quay.io/biocontainers/smithwaterman/1.0.0--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smithwaterman-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smithwaterman-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smithwaterman-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smithwaterman-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smithwaterman-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smithwaterman-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smithwaterman

```bash
$ singularity exec <container> /usr/local/bin/smithwaterman
$ podman run --it --rm --entrypoint /usr/local/bin/smithwaterman   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smithwaterman   -v ${PWD} -w ${PWD} <container> -c " $@"
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