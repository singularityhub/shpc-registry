---
layout: container
name:  "quay.io/biocontainers/oligomap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oligomap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oligomap/container.yaml"
updated_at: "2025-10-02 04:01:50.624977"
latest: "1.0.1--h077b44d_2"
container_url: "https://biocontainers.pro/tools/oligomap"
aliases:
 - "oligomap"
versions:
 - "1.0.1--hdcf5f25_0"
 - "1.0.1--h077b44d_1"
 - "1.0.1--h077b44d_2"
description: "singularity registry hpc automated addition for oligomap"
config: {"url": "https://biocontainers.pro/tools/oligomap", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for oligomap", "latest": {"1.0.1--h077b44d_2": "sha256:05609b50b39fd28f17834d66be0244be883b49f28c0d4b8698e9ec916e58354c"}, "tags": {"1.0.1--hdcf5f25_0": "sha256:3c0108ddd21099f961359844a4590a7b88b02be92a952e0ecc36a48597a1599c", "1.0.1--h077b44d_1": "sha256:5d3a54804a4538167363b256fa247275431ea62289aeb7ce50c2d169801734ac", "1.0.1--h077b44d_2": "sha256:05609b50b39fd28f17834d66be0244be883b49f28c0d4b8698e9ec916e58354c"}, "docker": "quay.io/biocontainers/oligomap", "aliases": {"oligomap": "/usr/local/bin/oligomap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oligomap.
singularity registry hpc automated addition for oligomap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oligomap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oligomap:1.0.1--h077b44d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oligomap/1.0.1--h077b44d_2
$ module help quay.io/biocontainers/oligomap/1.0.1--h077b44d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oligomap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oligomap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oligomap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oligomap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oligomap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oligomap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oligomap

```bash
$ singularity exec <container> /usr/local/bin/oligomap
$ podman run --it --rm --entrypoint /usr/local/bin/oligomap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oligomap   -v ${PWD} -w ${PWD} <container> -c " $@"
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