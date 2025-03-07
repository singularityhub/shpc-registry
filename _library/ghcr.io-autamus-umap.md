---
layout: container
name:  "ghcr.io/autamus/umap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/umap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/umap/container.yaml"
updated_at: "2025-03-07 03:48:13.523850"
latest: "2.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/umap"

versions:
 - "2.1.0"
 - "latest"
description: "Umap is a library that provides an mmap()-like interface to a simple, user-space page fault handler based on the userfaultfd Linux feature (starting with 4.3 linux kernel)."
config: {"docker": "ghcr.io/autamus/umap", "url": "https://github.com/orgs/autamus/packages/container/package/umap", "maintainer": "@vsoch", "description": "Umap is a library that provides an mmap()-like interface to a simple, user-space page fault handler based on the userfaultfd Linux feature (starting with 4.3 linux kernel).", "latest": {"2.1.0": "sha256:44db85ad345ca7d1f40b6ce5bb78b0f49d60a80ab7a78f248973b69902c7079c"}, "tags": {"2.1.0": "sha256:44db85ad345ca7d1f40b6ce5bb78b0f49d60a80ab7a78f248973b69902c7079c", "latest": "sha256:44db85ad345ca7d1f40b6ce5bb78b0f49d60a80ab7a78f248973b69902c7079c"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/umap.
Umap is a library that provides an mmap()-like interface to a simple, user-space page fault handler based on the userfaultfd Linux feature (starting with 4.3 linux kernel).
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/umap
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/umap:2.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/umap/2.1.0
$ module help ghcr.io/autamus/umap/2.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### umap

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