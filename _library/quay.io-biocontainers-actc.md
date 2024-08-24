---
layout: container
name:  "quay.io/biocontainers/actc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/actc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/actc/container.yaml"
updated_at: "2024-08-24 03:13:33.125283"
latest: "0.6.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/actc"
aliases:
 - "actc"
versions:
 - "0.2.0--h9ee0642_0"
 - "0.5.0--h9ee0642_0"
 - "0.6.0--h9ee0642_0"
description: "singularity registry hpc automated addition for actc"
config: {"url": "https://biocontainers.pro/tools/actc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for actc", "latest": {"0.6.0--h9ee0642_0": "sha256:95d652d98a2cc6322b69346fda7b6ca588797454021f840ffbbc9239aa3a5bce"}, "tags": {"0.2.0--h9ee0642_0": "sha256:6dbd50ab8bd39f6b3e8a7dc18075b799e77e39035b5c963535b06864e671c261", "0.5.0--h9ee0642_0": "sha256:1753703e1fbf2ef04e1dbda4041e9277abf7ad595bb841085957acf137a71ed3", "0.6.0--h9ee0642_0": "sha256:95d652d98a2cc6322b69346fda7b6ca588797454021f840ffbbc9239aa3a5bce"}, "docker": "quay.io/biocontainers/actc", "aliases": {"actc": "/usr/local/bin/actc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/actc.
singularity registry hpc automated addition for actc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/actc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/actc:0.6.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/actc/0.6.0--h9ee0642_0
$ module help quay.io/biocontainers/actc/0.6.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### actc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### actc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### actc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### actc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### actc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### actc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### actc

```bash
$ singularity exec <container> /usr/local/bin/actc
$ podman run --it --rm --entrypoint /usr/local/bin/actc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/actc   -v ${PWD} -w ${PWD} <container> -c " $@"
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