---
layout: container
name:  "quay.io/biocontainers/mbg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mbg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mbg/container.yaml"
updated_at: "2023-01-19 02:48:24.590000"
latest: "1.0.12--hd03093a_0"
container_url: "https://biocontainers.pro/tools/mbg"
aliases:
 - "MBG"
versions:
 - "1.0.9--hd03093a_1"
 - "1.0.12--hd03093a_0"
description: "shpc-registry automated BioContainers addition for mbg"
config: {"url": "https://biocontainers.pro/tools/mbg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mbg", "latest": {"1.0.12--hd03093a_0": "sha256:c04d2b07415150cc012f658df97479cc122fc67d11205b7cf6e94ef6e7c59408"}, "tags": {"1.0.9--hd03093a_1": "sha256:457ccc886389b3879ec1be1fa49d840e2abfbce1c2ea20720eed40737d6c7b3d", "1.0.12--hd03093a_0": "sha256:c04d2b07415150cc012f658df97479cc122fc67d11205b7cf6e94ef6e7c59408"}, "docker": "quay.io/biocontainers/mbg", "aliases": {"MBG": "/usr/local/bin/MBG"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mbg.
shpc-registry automated BioContainers addition for mbg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mbg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mbg:1.0.12--hd03093a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mbg/1.0.12--hd03093a_0
$ module help quay.io/biocontainers/mbg/1.0.12--hd03093a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mbg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mbg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mbg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mbg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mbg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mbg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MBG

```bash
$ singularity exec <container> /usr/local/bin/MBG
$ podman run --it --rm --entrypoint /usr/local/bin/MBG   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MBG   -v ${PWD} -w ${PWD} <container> -c " $@"
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