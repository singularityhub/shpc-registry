---
layout: container
name:  "quay.io/biocontainers/fusioncatcher-seqtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fusioncatcher-seqtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fusioncatcher-seqtk/container.yaml"
updated_at: "2025-10-20 03:44:31.255128"
latest: "1.2--h577a1d6_7"
container_url: "https://biocontainers.pro/tools/fusioncatcher-seqtk"
aliases:
 - "seqtk"
versions:
 - "1.2--h7132678_3"
 - "1.2--he4a0461_5"
 - "1.2--h577a1d6_6"
 - "1.2--h577a1d6_7"
description: "shpc-registry automated BioContainers addition for fusioncatcher-seqtk"
config: {"url": "https://biocontainers.pro/tools/fusioncatcher-seqtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fusioncatcher-seqtk", "latest": {"1.2--h577a1d6_7": "sha256:d130107e6aaf0c0dc5aaf94906a9a31f168380f9739909e3f86fef88f4768489"}, "tags": {"1.2--h7132678_3": "sha256:8e6e89febcc6e68afa1057f56e393df260a663115091ad5dede94df658ac08b4", "1.2--he4a0461_5": "sha256:afe63fe3bac4e0d11d30d3a5b834a4f25e6c55c93478e6dd0f6e40b7004c505c", "1.2--h577a1d6_6": "sha256:358de80ce62632ec60e5ba962868922f6ca5750b4e7b1643d5bc326500522e96", "1.2--h577a1d6_7": "sha256:d130107e6aaf0c0dc5aaf94906a9a31f168380f9739909e3f86fef88f4768489"}, "docker": "quay.io/biocontainers/fusioncatcher-seqtk", "aliases": {"seqtk": "/usr/local/bin/seqtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fusioncatcher-seqtk.
shpc-registry automated BioContainers addition for fusioncatcher-seqtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fusioncatcher-seqtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fusioncatcher-seqtk:1.2--h577a1d6_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fusioncatcher-seqtk/1.2--h577a1d6_7
$ module help quay.io/biocontainers/fusioncatcher-seqtk/1.2--h577a1d6_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fusioncatcher-seqtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fusioncatcher-seqtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fusioncatcher-seqtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fusioncatcher-seqtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fusioncatcher-seqtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fusioncatcher-seqtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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