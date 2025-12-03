---
layout: container
name:  "quay.io/biocontainers/smakcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/smakcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/smakcr/container.yaml"
updated_at: "2025-12-03 03:42:50.119771"
latest: "0.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/smakcr"
aliases:
 - "smakcr"
versions:
 - "0.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for smakcr"
config: {"url": "https://biocontainers.pro/tools/smakcr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for smakcr", "latest": {"0.1.0--h4349ce8_0": "sha256:9c30a249a44b76b978390f750e45c231b62b0a39e104b2210ab23398753f3c9f"}, "tags": {"0.1.0--h4349ce8_0": "sha256:9c30a249a44b76b978390f750e45c231b62b0a39e104b2210ab23398753f3c9f"}, "docker": "quay.io/biocontainers/smakcr", "aliases": {"smakcr": "/usr/local/bin/smakcr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/smakcr.
singularity registry hpc automated addition for smakcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/smakcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/smakcr:0.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/smakcr/0.1.0--h4349ce8_0
$ module help quay.io/biocontainers/smakcr/0.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### smakcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### smakcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### smakcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### smakcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### smakcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### smakcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### smakcr

```bash
$ singularity exec <container> /usr/local/bin/smakcr
$ podman run --it --rm --entrypoint /usr/local/bin/smakcr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smakcr   -v ${PWD} -w ${PWD} <container> -c " $@"
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