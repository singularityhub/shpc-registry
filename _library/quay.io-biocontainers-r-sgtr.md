---
layout: container
name:  "quay.io/biocontainers/r-sgtr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-sgtr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-sgtr/container.yaml"
updated_at: "2025-11-21 15:48:58.523068"
latest: "1.1.4--r44h503566f_8"
container_url: "https://biocontainers.pro/tools/r-sgtr"

versions:
 - "1.1.4--r41h87f3376_3"
 - "1.1.4--r42h87f3376_4"
 - "1.1.4--r42hdbdd923_6"
 - "1.1.4--r43hdbdd923_7"
 - "1.1.4--r44h503566f_8"
description: "shpc-registry automated BioContainers addition for r-sgtr"
config: {"url": "https://biocontainers.pro/tools/r-sgtr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-sgtr", "latest": {"1.1.4--r44h503566f_8": "sha256:546aa4cff1783e512bea3db353697e585c7f4afe055ac1c3c4bba1fdd654c63c"}, "tags": {"1.1.4--r41h87f3376_3": "sha256:7e1fd32eed4791e3467a5dee6917694b9f49b8149f5b4dddec0a28a515e5a9b1", "1.1.4--r42h87f3376_4": "sha256:d468226b192eff5e805cfc6aeeec4ad7fb523dcb03f9f0b3efb370deaa006748", "1.1.4--r42hdbdd923_6": "sha256:11cc1c1339ef77c123a288c0cfe3d4747f729498cf6e28d764a1aadf1b4141fd", "1.1.4--r43hdbdd923_7": "sha256:c33b0ae22e34c4e704f780059554ae9f3131f0b7cc457629b8a8299516db13d4", "1.1.4--r44h503566f_8": "sha256:546aa4cff1783e512bea3db353697e585c7f4afe055ac1c3c4bba1fdd654c63c"}, "docker": "quay.io/biocontainers/r-sgtr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-sgtr.
shpc-registry automated BioContainers addition for r-sgtr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-sgtr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-sgtr:1.1.4--r44h503566f_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-sgtr/1.1.4--r44h503566f_8
$ module help quay.io/biocontainers/r-sgtr/1.1.4--r44h503566f_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-sgtr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-sgtr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-sgtr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-sgtr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-sgtr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-sgtr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-sgtr

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