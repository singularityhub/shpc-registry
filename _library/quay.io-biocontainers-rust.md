---
layout: container
name:  "quay.io/biocontainers/rust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust/container.yaml"
updated_at: "2024-09-22 03:41:29.198829"
latest: "1.14.0--0"
container_url: "https://biocontainers.pro/tools/rust"

versions:
 - "1.14.0--0"
description: "shpc-registry automated BioContainers addition for rust"
config: {"url": "https://biocontainers.pro/tools/rust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rust", "latest": {"1.14.0--0": "sha256:3a45f0b41af427e6d0be19b183f1969c292e47d27becdc1b72ca7801c58d139c"}, "tags": {"1.14.0--0": "sha256:3a45f0b41af427e6d0be19b183f1969c292e47d27becdc1b72ca7801c58d139c"}, "docker": "quay.io/biocontainers/rust"}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust.
shpc-registry automated BioContainers addition for rust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust:1.14.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust/1.14.0--0
$ module help quay.io/biocontainers/rust/1.14.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### rust

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