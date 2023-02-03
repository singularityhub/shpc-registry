---
layout: container
name:  "quay.io/biocontainers/atlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/atlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/atlas/container.yaml"
updated_at: "2023-02-03 03:19:18.840217"
latest: "0.9.9--h42556f1_1"
container_url: "https://biocontainers.pro/tools/atlas"
aliases:
 - "atlas"
versions:
 - "0.9.9--h42556f1_1"
description: "shpc-registry automated BioContainers addition for atlas"
config: {"url": "https://biocontainers.pro/tools/atlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for atlas", "latest": {"0.9.9--h42556f1_1": "sha256:b356e7fa38d7c7a1cb110479105437c32084a33fedeebfe58c9d8f37fdc50383"}, "tags": {"0.9.9--h42556f1_1": "sha256:b356e7fa38d7c7a1cb110479105437c32084a33fedeebfe58c9d8f37fdc50383"}, "docker": "quay.io/biocontainers/atlas", "aliases": {"atlas": "/usr/local/bin/atlas"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/atlas.
shpc-registry automated BioContainers addition for atlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/atlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/atlas:0.9.9--h42556f1_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/atlas/0.9.9--h42556f1_1
$ module help quay.io/biocontainers/atlas/0.9.9--h42556f1_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### atlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### atlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### atlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### atlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### atlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### atlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atlas

```bash
$ singularity exec <container> /usr/local/bin/atlas
$ podman run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
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