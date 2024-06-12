---
layout: container
name:  "quay.io/biocontainers/r-firebrowser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-firebrowser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-firebrowser/container.yaml"
updated_at: "2024-06-12 02:48:59.314013"
latest: "1.1.35--r43hdfd78af_5"
container_url: "https://biocontainers.pro/tools/r-firebrowser"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.35--r41hdfd78af_3"
 - "1.1.35--r42hdfd78af_4"
 - "1.1.35--r43hdfd78af_5"
description: "shpc-registry automated BioContainers addition for r-firebrowser"
config: {"url": "https://biocontainers.pro/tools/r-firebrowser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-firebrowser", "latest": {"1.1.35--r43hdfd78af_5": "sha256:0b4e610eccdef3ded253114bc475ca3ed25eb330d11ea0cfbd805f2964a91c0a"}, "tags": {"1.1.35--r41hdfd78af_3": "sha256:b7434e714be97ced7ae28c9471144a4c199f481561d063a34dc53056cb2e4f5b", "1.1.35--r42hdfd78af_4": "sha256:21677c6daa74488b8e1ec5c3b98784dbf4bb8efc43bf7a545300d55e7951bfb9", "1.1.35--r43hdfd78af_5": "sha256:0b4e610eccdef3ded253114bc475ca3ed25eb330d11ea0cfbd805f2964a91c0a"}, "docker": "quay.io/biocontainers/r-firebrowser", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-firebrowser.
shpc-registry automated BioContainers addition for r-firebrowser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-firebrowser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-firebrowser:1.1.35--r43hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-firebrowser/1.1.35--r43hdfd78af_5
$ module help quay.io/biocontainers/r-firebrowser/1.1.35--r43hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-firebrowser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-firebrowser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-firebrowser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-firebrowser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-firebrowser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-firebrowser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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