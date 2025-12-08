---
layout: container
name:  "quay.io/biocontainers/rust-proseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-proseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-proseg/container.yaml"
updated_at: "2025-12-08 05:25:09.120216"
latest: "2.0.6--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/rust-proseg"
aliases:
 - "proseg"
 - "proseg-to-baysor"
versions:
 - "2.0.5--h4349ce8_0"
 - "2.0.6--h4349ce8_0"
description: "singularity registry hpc automated addition for rust-proseg"
config: {"url": "https://biocontainers.pro/tools/rust-proseg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rust-proseg", "latest": {"2.0.6--h4349ce8_0": "sha256:fe53ec715b3fb6f044d9de9646d73b650200b59a1f9ade506ab255c1c10d28ef"}, "tags": {"2.0.5--h4349ce8_0": "sha256:41468b8a80a377ddf4ce2d0d48406ce881087651fbe10b7aed4d5f5dd399c085", "2.0.6--h4349ce8_0": "sha256:fe53ec715b3fb6f044d9de9646d73b650200b59a1f9ade506ab255c1c10d28ef"}, "docker": "quay.io/biocontainers/rust-proseg", "aliases": {"proseg": "/usr/local/bin/proseg", "proseg-to-baysor": "/usr/local/bin/proseg-to-baysor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-proseg.
singularity registry hpc automated addition for rust-proseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-proseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-proseg:2.0.6--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-proseg/2.0.6--h4349ce8_0
$ module help quay.io/biocontainers/rust-proseg/2.0.6--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-proseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-proseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-proseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-proseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-proseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-proseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proseg

```bash
$ singularity exec <container> /usr/local/bin/proseg
$ podman run --it --rm --entrypoint /usr/local/bin/proseg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proseg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proseg-to-baysor

```bash
$ singularity exec <container> /usr/local/bin/proseg-to-baysor
$ podman run --it --rm --entrypoint /usr/local/bin/proseg-to-baysor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proseg-to-baysor   -v ${PWD} -w ${PWD} <container> -c " $@"
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