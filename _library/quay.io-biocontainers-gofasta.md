---
layout: container
name:  "quay.io/biocontainers/gofasta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gofasta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gofasta/container.yaml"
updated_at: "2023-02-24 02:50:39.023453"
latest: "1.2.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/gofasta"
aliases:
 - "gofasta"
versions:
 - "1.1.0--h9ee0642_0"
 - "1.2.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for gofasta"
config: {"url": "https://biocontainers.pro/tools/gofasta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gofasta", "latest": {"1.2.0--h9ee0642_0": "sha256:8e6ea023c629b5f7b618cc381c4e2b81ed147642b2d59cfe9bdf3c535ac7cf8a"}, "tags": {"1.1.0--h9ee0642_0": "sha256:4806770f97a5054f5be40996e9dc13ba1b2882628869ecbd3152075252720091", "1.2.0--h9ee0642_0": "sha256:8e6ea023c629b5f7b618cc381c4e2b81ed147642b2d59cfe9bdf3c535ac7cf8a"}, "docker": "quay.io/biocontainers/gofasta", "aliases": {"gofasta": "/usr/local/bin/gofasta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gofasta.
shpc-registry automated BioContainers addition for gofasta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gofasta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gofasta:1.2.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gofasta/1.2.0--h9ee0642_0
$ module help quay.io/biocontainers/gofasta/1.2.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gofasta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gofasta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gofasta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gofasta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gofasta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gofasta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gofasta

```bash
$ singularity exec <container> /usr/local/bin/gofasta
$ podman run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gofasta   -v ${PWD} -w ${PWD} <container> -c " $@"
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