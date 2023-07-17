---
layout: container
name:  "quay.io/biocontainers/agc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/agc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/agc/container.yaml"
updated_at: "2023-07-17 03:53:57.586766"
latest: "3.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/agc"
aliases:
 - "agc"
versions:
 - "3.0--h9ee0642_0"
description: "singularity registry hpc automated addition for agc"
config: {"url": "https://biocontainers.pro/tools/agc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for agc", "latest": {"3.0--h9ee0642_0": "sha256:e1a8b39f5300aa149ce90358b372f48a67881a80b1ad7e0c356f16e20b76f3f9"}, "tags": {"3.0--h9ee0642_0": "sha256:e1a8b39f5300aa149ce90358b372f48a67881a80b1ad7e0c356f16e20b76f3f9"}, "docker": "quay.io/biocontainers/agc", "aliases": {"agc": "/usr/local/bin/agc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/agc.
singularity registry hpc automated addition for agc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/agc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/agc:3.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/agc/3.0--h9ee0642_0
$ module help quay.io/biocontainers/agc/3.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### agc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### agc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### agc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### agc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### agc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### agc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agc

```bash
$ singularity exec <container> /usr/local/bin/agc
$ podman run --it --rm --entrypoint /usr/local/bin/agc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agc   -v ${PWD} -w ${PWD} <container> -c " $@"
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