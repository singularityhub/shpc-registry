---
layout: container
name:  "quay.io/biocontainers/rust-gtars"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-gtars/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-gtars/container.yaml"
updated_at: "2025-04-07 03:31:54.403129"
latest: "0.2.4--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/rust-gtars"
aliases:
 - "gtars"
versions:
 - "0.2.0--h4349ce8_1"
 - "0.2.4--h4349ce8_0"
description: "singularity registry hpc automated addition for rust-gtars"
config: {"url": "https://biocontainers.pro/tools/rust-gtars", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rust-gtars", "latest": {"0.2.4--h4349ce8_0": "sha256:b4e254fdbc9952bf624ddafece0efca6e89ef1d7c7f78c34f95b71270ebee6eb"}, "tags": {"0.2.0--h4349ce8_1": "sha256:74c31e3f586b159c0a5b9a839a37d2c2878644f9e5b25974ba4c25394397c3c7", "0.2.4--h4349ce8_0": "sha256:b4e254fdbc9952bf624ddafece0efca6e89ef1d7c7f78c34f95b71270ebee6eb"}, "docker": "quay.io/biocontainers/rust-gtars", "aliases": {"gtars": "/usr/local/bin/gtars"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-gtars.
singularity registry hpc automated addition for rust-gtars
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-gtars
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-gtars:0.2.4--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-gtars/0.2.4--h4349ce8_0
$ module help quay.io/biocontainers/rust-gtars/0.2.4--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-gtars-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-gtars-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-gtars-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-gtars-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-gtars-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-gtars-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gtars

```bash
$ singularity exec <container> /usr/local/bin/gtars
$ podman run --it --rm --entrypoint /usr/local/bin/gtars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtars   -v ${PWD} -w ${PWD} <container> -c " $@"
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