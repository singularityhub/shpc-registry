---
layout: container
name:  "quay.io/biocontainers/mapseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mapseq/container.yaml"
updated_at: "2023-06-21 03:21:06.193225"
latest: "2.1.1--ha34dc8c_0"
container_url: "https://biocontainers.pro/tools/mapseq"
aliases:
 - "esh"
 - "eutils-config"
 - "mapseq"
versions:
 - "1.2.6--ha34dc8c_3"
 - "2.1.1--ha34dc8c_0"
description: "shpc-registry automated BioContainers addition for mapseq"
config: {"url": "https://biocontainers.pro/tools/mapseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mapseq", "latest": {"2.1.1--ha34dc8c_0": "sha256:326574bdad0e3e393976f93dd8d53077bf3d89d34c3d693dc0b996fa2de2bf00"}, "tags": {"1.2.6--ha34dc8c_3": "sha256:57426f4ee51d1bf56dc9ac01f2e1d34b6cb5b34992a7feb5a302b24f7d5f5fe2", "2.1.1--ha34dc8c_0": "sha256:326574bdad0e3e393976f93dd8d53077bf3d89d34c3d693dc0b996fa2de2bf00"}, "docker": "quay.io/biocontainers/mapseq", "aliases": {"esh": "/usr/local/bin/esh", "eutils-config": "/usr/local/bin/eutils-config", "mapseq": "/usr/local/bin/mapseq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapseq.
shpc-registry automated BioContainers addition for mapseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapseq:2.1.1--ha34dc8c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapseq/2.1.1--ha34dc8c_0
$ module help quay.io/biocontainers/mapseq/2.1.1--ha34dc8c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### esh

```bash
$ singularity exec <container> /usr/local/bin/esh
$ podman run --it --rm --entrypoint /usr/local/bin/esh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eutils-config

```bash
$ singularity exec <container> /usr/local/bin/eutils-config
$ podman run --it --rm --entrypoint /usr/local/bin/eutils-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eutils-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapseq

```bash
$ singularity exec <container> /usr/local/bin/mapseq
$ podman run --it --rm --entrypoint /usr/local/bin/mapseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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