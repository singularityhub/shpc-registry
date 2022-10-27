---
layout: container
name:  "quay.io/biocontainers/r-velocyto.r"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-velocyto.r/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-velocyto.r/container.yaml"
updated_at: "2022-10-27 00:23:55.902284"
latest: "0.6--r41h46c59ee_4"
container_url: "https://biocontainers.pro/tools/r-velocyto.r"

versions:
 - "0.6--r41h46c59ee_4"
description: "shpc-registry automated BioContainers addition for r-velocyto.r"
config: {"url": "https://biocontainers.pro/tools/r-velocyto.r", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-velocyto.r", "latest": {"0.6--r41h46c59ee_4": "sha256:035375e26022e0f01f6c46c53c956bfb8e7f20672ce50a41dca3602f8f2ab58d"}, "tags": {"0.6--r41h46c59ee_4": "sha256:035375e26022e0f01f6c46c53c956bfb8e7f20672ce50a41dca3602f8f2ab58d"}, "docker": "quay.io/biocontainers/r-velocyto.r"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-velocyto.r.
shpc-registry automated BioContainers addition for r-velocyto.r
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-velocyto.r
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-velocyto.r:0.6--r41h46c59ee_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-velocyto.r/0.6--r41h46c59ee_4
$ module help quay.io/biocontainers/r-velocyto.r/0.6--r41h46c59ee_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-velocyto.r-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-velocyto.r-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-velocyto.r-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-velocyto.r-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-velocyto.r-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-velocyto.r-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-velocyto.r

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