---
layout: container
name:  "quay.io/biocontainers/mft-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mft-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mft-tools/container.yaml"
updated_at: "2026-06-16 08:06:22.784922"
latest: "0.1.1--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/mft-tools"
aliases:
 - "mft"
versions:
 - "0.1.0--hab7d0fd_0"
 - "0.1.1--hab7d0fd_0"
description: "singularity registry hpc automated addition for mft-tools"
config: {"url": "https://biocontainers.pro/tools/mft-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mft-tools", "latest": {"0.1.1--hab7d0fd_0": "sha256:df899efa62a147b8a713c8f58a772e23649c51018d66b7868664d9d19e2bd598"}, "tags": {"0.1.0--hab7d0fd_0": "sha256:ed58b3e2cbfab2ff4735797c3399e23d48fe07988c205a6ad47430b47309cc47", "0.1.1--hab7d0fd_0": "sha256:df899efa62a147b8a713c8f58a772e23649c51018d66b7868664d9d19e2bd598"}, "docker": "quay.io/biocontainers/mft-tools", "aliases": {"mft": "/usr/local/bin/mft"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mft-tools.
singularity registry hpc automated addition for mft-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mft-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mft-tools:0.1.1--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mft-tools/0.1.1--hab7d0fd_0
$ module help quay.io/biocontainers/mft-tools/0.1.1--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mft-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mft-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mft-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mft-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mft-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mft-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mft

```bash
$ singularity exec <container> /usr/local/bin/mft
$ podman run --it --rm --entrypoint /usr/local/bin/mft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mft   -v ${PWD} -w ${PWD} <container> -c " $@"
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