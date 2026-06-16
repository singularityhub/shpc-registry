---
layout: container
name:  "quay.io/biocontainers/prinseq-rust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prinseq-rust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prinseq-rust/container.yaml"
updated_at: "2026-06-16 08:17:19.710381"
latest: "1.1.1--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/prinseq-rust"
aliases:
 - "prinseq-rust"
versions:
 - "1.1.1--hab7d0fd_0"
description: "singularity registry hpc automated addition for prinseq-rust"
config: {"url": "https://biocontainers.pro/tools/prinseq-rust", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for prinseq-rust", "latest": {"1.1.1--hab7d0fd_0": "sha256:56f6a505ad26e2d15cb7bb99d1303169ff2c54001721aafa541c5408b2c1bb13"}, "tags": {"1.1.1--hab7d0fd_0": "sha256:56f6a505ad26e2d15cb7bb99d1303169ff2c54001721aafa541c5408b2c1bb13"}, "docker": "quay.io/biocontainers/prinseq-rust", "aliases": {"prinseq-rust": "/usr/local/bin/prinseq-rust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prinseq-rust.
singularity registry hpc automated addition for prinseq-rust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prinseq-rust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prinseq-rust:1.1.1--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prinseq-rust/1.1.1--hab7d0fd_0
$ module help quay.io/biocontainers/prinseq-rust/1.1.1--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prinseq-rust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prinseq-rust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prinseq-rust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prinseq-rust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prinseq-rust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prinseq-rust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prinseq-rust

```bash
$ singularity exec <container> /usr/local/bin/prinseq-rust
$ podman run --it --rm --entrypoint /usr/local/bin/prinseq-rust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prinseq-rust   -v ${PWD} -w ${PWD} <container> -c " $@"
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