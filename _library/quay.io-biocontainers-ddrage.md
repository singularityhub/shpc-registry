---
layout: container
name:  "quay.io/biocontainers/ddrage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ddrage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ddrage/container.yaml"
updated_at: "2024-07-06 02:39:43.815995"
latest: "1.8.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ddrage"

versions:
 - "1.7.1--py_0"
 - "1.8.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ddrage"
config: {"url": "https://biocontainers.pro/tools/ddrage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ddrage", "latest": {"1.8.1--pyhdfd78af_0": "sha256:babc7665fc2a709027145a2b9638db32560b009dbb299e0a9fd58bc36d6f19fc"}, "tags": {"1.7.1--py_0": "sha256:083ae9625a7c5e5f833bb3089e4084edbad20469b1f542774482b718454406e5", "1.8.1--pyhdfd78af_0": "sha256:babc7665fc2a709027145a2b9638db32560b009dbb299e0a9fd58bc36d6f19fc"}, "docker": "quay.io/biocontainers/ddrage"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ddrage.
shpc-registry automated BioContainers addition for ddrage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ddrage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ddrage:1.8.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ddrage/1.8.1--pyhdfd78af_0
$ module help quay.io/biocontainers/ddrage/1.8.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ddrage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ddrage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ddrage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ddrage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ddrage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ddrage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ddrage

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