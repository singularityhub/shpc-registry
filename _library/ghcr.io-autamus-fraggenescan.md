---
layout: container
name:  "ghcr.io/autamus/fraggenescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/fraggenescan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/fraggenescan/container.yaml"
updated_at: "2024-01-10 03:13:10.383551"
latest: "1.31"
container_url: "https://github.com/orgs/autamus/packages/container/package/fraggenescan"

versions:
 - "1.31"
 - "latest"
description: "An application for finding (fragmented) genes in short reads."
config: {"docker": "ghcr.io/autamus/fraggenescan", "url": "https://github.com/orgs/autamus/packages/container/package/fraggenescan", "maintainer": "@vsoch", "description": "An application for finding (fragmented) genes in short reads.", "latest": {"1.31": "sha256:8b24bdf1e4bc2b8d3a79b45736adf2293db279a743db1e5ea1f2f5f43ca8a772"}, "tags": {"1.31": "sha256:8b24bdf1e4bc2b8d3a79b45736adf2293db279a743db1e5ea1f2f5f43ca8a772", "latest": "sha256:8b24bdf1e4bc2b8d3a79b45736adf2293db279a743db1e5ea1f2f5f43ca8a772"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/fraggenescan.
An application for finding (fragmented) genes in short reads.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/fraggenescan
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/fraggenescan:1.31
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/fraggenescan/1.31
$ module help ghcr.io/autamus/fraggenescan/1.31
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fraggenescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fraggenescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fraggenescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fraggenescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fraggenescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fraggenescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fraggenescan

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