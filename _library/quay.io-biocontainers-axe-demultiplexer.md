---
layout: container
name:  "quay.io/biocontainers/axe-demultiplexer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/axe-demultiplexer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/axe-demultiplexer/container.yaml"
updated_at: "2025-08-01 04:14:01.002907"
latest: "0.3.3--h3a4d415_0"
container_url: "https://biocontainers.pro/tools/axe-demultiplexer"
aliases:
 - "axe-demux"
versions:
 - "0.3.3--h3a4d415_0"
description: "singularity registry hpc automated addition for axe-demultiplexer"
config: {"url": "https://biocontainers.pro/tools/axe-demultiplexer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for axe-demultiplexer", "latest": {"0.3.3--h3a4d415_0": "sha256:1d9892b922bb6940348d195289987402b27070dc4f52760aa2b35d75bba7092a"}, "tags": {"0.3.3--h3a4d415_0": "sha256:1d9892b922bb6940348d195289987402b27070dc4f52760aa2b35d75bba7092a"}, "docker": "quay.io/biocontainers/axe-demultiplexer", "aliases": {"axe-demux": "/usr/local/bin/axe-demux"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/axe-demultiplexer.
singularity registry hpc automated addition for axe-demultiplexer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/axe-demultiplexer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/axe-demultiplexer:0.3.3--h3a4d415_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/axe-demultiplexer/0.3.3--h3a4d415_0
$ module help quay.io/biocontainers/axe-demultiplexer/0.3.3--h3a4d415_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### axe-demultiplexer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### axe-demultiplexer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### axe-demultiplexer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### axe-demultiplexer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### axe-demultiplexer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### axe-demultiplexer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### axe-demux

```bash
$ singularity exec <container> /usr/local/bin/axe-demux
$ podman run --it --rm --entrypoint /usr/local/bin/axe-demux   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/axe-demux   -v ${PWD} -w ${PWD} <container> -c " $@"
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