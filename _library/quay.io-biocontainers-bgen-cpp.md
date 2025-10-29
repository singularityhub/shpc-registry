---
layout: container
name:  "quay.io/biocontainers/bgen-cpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bgen-cpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bgen-cpp/container.yaml"
updated_at: "2025-10-29 03:48:18.830008"
latest: "1.1.7--h5ca1c30_0"
container_url: "https://biocontainers.pro/tools/bgen-cpp"
aliases:
 - "bgenix"
 - "cat-bgen"
 - "edit-bgen"
versions:
 - "1.1.7--h5ca1c30_0"
description: "singularity registry hpc automated addition for bgen-cpp"
config: {"url": "https://biocontainers.pro/tools/bgen-cpp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bgen-cpp", "latest": {"1.1.7--h5ca1c30_0": "sha256:1449d6740ad546c197fc9a4c85ade48a0f4b6dc714a070b097c451fa26957dac"}, "tags": {"1.1.7--h5ca1c30_0": "sha256:1449d6740ad546c197fc9a4c85ade48a0f4b6dc714a070b097c451fa26957dac"}, "docker": "quay.io/biocontainers/bgen-cpp", "aliases": {"bgenix": "/usr/local/bin/bgenix", "cat-bgen": "/usr/local/bin/cat-bgen", "edit-bgen": "/usr/local/bin/edit-bgen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bgen-cpp.
singularity registry hpc automated addition for bgen-cpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bgen-cpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bgen-cpp:1.1.7--h5ca1c30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bgen-cpp/1.1.7--h5ca1c30_0
$ module help quay.io/biocontainers/bgen-cpp/1.1.7--h5ca1c30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bgen-cpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bgen-cpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bgen-cpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bgen-cpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bgen-cpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bgen-cpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgenix

```bash
$ singularity exec <container> /usr/local/bin/bgenix
$ podman run --it --rm --entrypoint /usr/local/bin/bgenix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgenix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat-bgen

```bash
$ singularity exec <container> /usr/local/bin/cat-bgen
$ podman run --it --rm --entrypoint /usr/local/bin/cat-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edit-bgen

```bash
$ singularity exec <container> /usr/local/bin/edit-bgen
$ podman run --it --rm --entrypoint /usr/local/bin/edit-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit-bgen   -v ${PWD} -w ${PWD} <container> -c " $@"
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