---
layout: container
name:  "quay.io/biocontainers/bioconductor-biovizbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biovizbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biovizbase/container.yaml"
updated_at: "2023-10-30 03:21:06.579876"
latest: "1.48.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biovizbase"

versions:
 - "1.42.0--r41hc0cfd56_2"
 - "1.46.0--r42hc0cfd56_0"
 - "1.46.0--r42ha9d7317_1"
 - "1.48.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biovizbase"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biovizbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biovizbase", "latest": {"1.48.0--r43ha9d7317_0": "sha256:05a6f01c8e39011606a22584421a5276406e017a989ca5c3d50cefb6608004ef"}, "tags": {"1.42.0--r41hc0cfd56_2": "sha256:6b594d9993080c90a7caf8a1d0c95ab56ed0dde405d8b166da363a9036de5a52", "1.46.0--r42hc0cfd56_0": "sha256:7fe72d129a30a78a678d12504a43a54829e684d60347c40b8c2c8f67ea271773", "1.46.0--r42ha9d7317_1": "sha256:a471ed6aa0b9007fb6b2a6a3d5063feed4c8a3574ec7f6b14fd162545bc18aef", "1.48.0--r43ha9d7317_0": "sha256:05a6f01c8e39011606a22584421a5276406e017a989ca5c3d50cefb6608004ef"}, "docker": "quay.io/biocontainers/bioconductor-biovizbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biovizbase.
shpc-registry automated BioContainers addition for bioconductor-biovizbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biovizbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biovizbase:1.48.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biovizbase/1.48.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-biovizbase/1.48.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biovizbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biovizbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biovizbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biovizbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biovizbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biovizbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biovizbase

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