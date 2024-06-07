---
layout: container
name:  "quay.io/biocontainers/minimap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minimap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minimap/container.yaml"
updated_at: "2024-06-07 02:35:36.127358"
latest: "0.2_r124--he4a0461_7"
container_url: "https://biocontainers.pro/tools/minimap"

versions:
 - "0.2_r124--h7132678_5"
 - "0.2_r124--he4a0461_7"
description: "shpc-registry automated BioContainers addition for minimap"
config: {"url": "https://biocontainers.pro/tools/minimap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minimap", "latest": {"0.2_r124--he4a0461_7": "sha256:7a74cd991e5bf37ebef6b05eef29a1c6f8514db911a997c8c49129a682b1593f"}, "tags": {"0.2_r124--h7132678_5": "sha256:9c29e2f2f305f9eec90e3a45b08fb0a292d77a8e2de8b7426f47d735fcec53ce", "0.2_r124--he4a0461_7": "sha256:7a74cd991e5bf37ebef6b05eef29a1c6f8514db911a997c8c49129a682b1593f"}, "docker": "quay.io/biocontainers/minimap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/minimap.
shpc-registry automated BioContainers addition for minimap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minimap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minimap:0.2_r124--he4a0461_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minimap/0.2_r124--he4a0461_7
$ module help quay.io/biocontainers/minimap/0.2_r124--he4a0461_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### minimap

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