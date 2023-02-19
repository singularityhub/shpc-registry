---
layout: container
name:  "quay.io/biocontainers/imseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/imseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/imseq/container.yaml"
updated_at: "2023-02-19 03:20:22.517891"
latest: "1.1.0--hd03093a_5"
container_url: "https://biocontainers.pro/tools/imseq"
aliases:
 - "imseq"
versions:
 - "1.1.0--hd03093a_5"
description: "shpc-registry automated BioContainers addition for imseq"
config: {"url": "https://biocontainers.pro/tools/imseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for imseq", "latest": {"1.1.0--hd03093a_5": "sha256:2a881fa617299402bebd37dd28631206dbad8b74fd556b601a2419d05521f88c"}, "tags": {"1.1.0--hd03093a_5": "sha256:2a881fa617299402bebd37dd28631206dbad8b74fd556b601a2419d05521f88c"}, "docker": "quay.io/biocontainers/imseq", "aliases": {"imseq": "/usr/local/bin/imseq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/imseq.
shpc-registry automated BioContainers addition for imseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/imseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/imseq:1.1.0--hd03093a_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/imseq/1.1.0--hd03093a_5
$ module help quay.io/biocontainers/imseq/1.1.0--hd03093a_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### imseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### imseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### imseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### imseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### imseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### imseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### imseq

```bash
$ singularity exec <container> /usr/local/bin/imseq
$ podman run --it --rm --entrypoint /usr/local/bin/imseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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