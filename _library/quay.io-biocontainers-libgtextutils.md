---
layout: container
name:  "quay.io/biocontainers/libgtextutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libgtextutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libgtextutils/container.yaml"
updated_at: "2024-03-22 03:01:41.350114"
latest: "0.7--hdbdd923_11"
container_url: "https://biocontainers.pro/tools/libgtextutils"

versions:
 - "0.7--h87f3376_9"
 - "0.7--hdbdd923_11"
description: "shpc-registry automated BioContainers addition for libgtextutils"
config: {"url": "https://biocontainers.pro/tools/libgtextutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libgtextutils", "latest": {"0.7--hdbdd923_11": "sha256:21f213713d3c59cccb13a5a5493e904012084a8d540393dea5ca6ef94844639e"}, "tags": {"0.7--h87f3376_9": "sha256:e0db5758a99daecf61134b07ec0d60f8086ec3be275199d0b9a2ac098bb985ec", "0.7--hdbdd923_11": "sha256:21f213713d3c59cccb13a5a5493e904012084a8d540393dea5ca6ef94844639e"}, "docker": "quay.io/biocontainers/libgtextutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libgtextutils.
shpc-registry automated BioContainers addition for libgtextutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libgtextutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libgtextutils:0.7--hdbdd923_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libgtextutils/0.7--hdbdd923_11
$ module help quay.io/biocontainers/libgtextutils/0.7--hdbdd923_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libgtextutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libgtextutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libgtextutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libgtextutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libgtextutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libgtextutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libgtextutils

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