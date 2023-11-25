---
layout: container
name:  "quay.io/biocontainers/piler-cr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piler-cr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piler-cr/container.yaml"
updated_at: "2023-11-25 02:33:45.278561"
latest: "1.06--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/piler-cr"
aliases:
 - "pilercr"
versions:
 - "1.06--h9f5acd7_2"
 - "1.06--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for piler-cr"
config: {"url": "https://biocontainers.pro/tools/piler-cr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for piler-cr", "latest": {"1.06--h4ac6f70_4": "sha256:81d4e8b220fd9d93e7a17712bf3f384e6c0e0802c724f25c70046b0c40ea4717"}, "tags": {"1.06--h9f5acd7_2": "sha256:1d7c387480eb9d86d16e70708c9e08d826982b2cfb28b985c9cc6bc7520c8eb9", "1.06--h4ac6f70_4": "sha256:81d4e8b220fd9d93e7a17712bf3f384e6c0e0802c724f25c70046b0c40ea4717"}, "docker": "quay.io/biocontainers/piler-cr", "aliases": {"pilercr": "/usr/local/bin/pilercr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piler-cr.
shpc-registry automated BioContainers addition for piler-cr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piler-cr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piler-cr:1.06--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piler-cr/1.06--h4ac6f70_4
$ module help quay.io/biocontainers/piler-cr/1.06--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piler-cr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piler-cr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piler-cr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piler-cr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piler-cr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piler-cr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pilercr

```bash
$ singularity exec <container> /usr/local/bin/pilercr
$ podman run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
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