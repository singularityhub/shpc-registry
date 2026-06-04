---
layout: container
name:  "quay.io/biocontainers/motif-bridge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/motif-bridge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/motif-bridge/container.yaml"
updated_at: "2026-06-04 07:16:18.486478"
latest: "0.1.0--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/motif-bridge"
aliases:
 - "homer2meme"
 - "meme2homer"
versions:
 - "0.1.0--hab7d0fd_0"
description: "singularity registry hpc automated addition for motif-bridge"
config: {"url": "https://biocontainers.pro/tools/motif-bridge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for motif-bridge", "latest": {"0.1.0--hab7d0fd_0": "sha256:edb9d5228e6ec7d26f929d93df8ddfdea506957241317b436bbfc41af28291b4"}, "tags": {"0.1.0--hab7d0fd_0": "sha256:edb9d5228e6ec7d26f929d93df8ddfdea506957241317b436bbfc41af28291b4"}, "docker": "quay.io/biocontainers/motif-bridge", "aliases": {"homer2meme": "/usr/local/bin/homer2meme", "meme2homer": "/usr/local/bin/meme2homer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/motif-bridge.
singularity registry hpc automated addition for motif-bridge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/motif-bridge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/motif-bridge:0.1.0--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/motif-bridge/0.1.0--hab7d0fd_0
$ module help quay.io/biocontainers/motif-bridge/0.1.0--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### motif-bridge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### motif-bridge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### motif-bridge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### motif-bridge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### motif-bridge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### motif-bridge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### homer2meme

```bash
$ singularity exec <container> /usr/local/bin/homer2meme
$ podman run --it --rm --entrypoint /usr/local/bin/homer2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/homer2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meme2homer

```bash
$ singularity exec <container> /usr/local/bin/meme2homer
$ podman run --it --rm --entrypoint /usr/local/bin/meme2homer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meme2homer   -v ${PWD} -w ${PWD} <container> -c " $@"
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