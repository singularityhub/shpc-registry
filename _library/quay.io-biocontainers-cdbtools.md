---
layout: container
name:  "quay.io/biocontainers/cdbtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cdbtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cdbtools/container.yaml"
updated_at: "2025-04-12 03:10:20.092733"
latest: "0.99--hdcf5f25_10"
container_url: "https://biocontainers.pro/tools/cdbtools"
aliases:
 - "cdbfasta"
 - "cdbyank"
versions:
 - "0.99--hd03093a_7"
 - "0.99--hd03093a_8"
 - "0.99--hdcf5f25_9"
 - "0.99--hdcf5f25_10"
description: "shpc-registry automated BioContainers addition for cdbtools"
config: {"url": "https://biocontainers.pro/tools/cdbtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cdbtools", "latest": {"0.99--hdcf5f25_10": "sha256:7e233b5a547398aada67dbd02e68340212b8bb369c16bcb02347d48f46c0c0cc"}, "tags": {"0.99--hd03093a_7": "sha256:f3024dcb89fa94850824379687816d4964f1bbc2e4c8431df88e4d0b9b6d4570", "0.99--hd03093a_8": "sha256:43d3098ede010b7cdd493ee0fe4b3650df84c89419a2642a2095356d26a8423f", "0.99--hdcf5f25_9": "sha256:7f8776cf60345014e3040c965f8379f40d61e3d35492a89868a7d5a2b852dea8", "0.99--hdcf5f25_10": "sha256:7e233b5a547398aada67dbd02e68340212b8bb369c16bcb02347d48f46c0c0cc"}, "docker": "quay.io/biocontainers/cdbtools", "aliases": {"cdbfasta": "/usr/local/bin/cdbfasta", "cdbyank": "/usr/local/bin/cdbyank"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cdbtools.
shpc-registry automated BioContainers addition for cdbtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cdbtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cdbtools:0.99--hdcf5f25_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cdbtools/0.99--hdcf5f25_10
$ module help quay.io/biocontainers/cdbtools/0.99--hdcf5f25_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cdbtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cdbtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cdbtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cdbtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cdbtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cdbtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cdbfasta

```bash
$ singularity exec <container> /usr/local/bin/cdbfasta
$ podman run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdbyank

```bash
$ singularity exec <container> /usr/local/bin/cdbyank
$ podman run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdbyank   -v ${PWD} -w ${PWD} <container> -c " $@"
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