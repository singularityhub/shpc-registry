---
layout: container
name:  "quay.io/biocontainers/msisensor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msisensor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/msisensor/container.yaml"
updated_at: "2024-06-11 02:55:04.398610"
latest: "0.5--h264e753_6"
container_url: "https://biocontainers.pro/tools/msisensor"

versions:
 - "0.5--h360a1d4_4"
 - "0.5--h360a1d4_5"
 - "0.5--h264e753_6"
description: "shpc-registry automated BioContainers addition for msisensor"
config: {"url": "https://biocontainers.pro/tools/msisensor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msisensor", "latest": {"0.5--h264e753_6": "sha256:f6229b88bb27675d2c6d1242995843738668d22933fa613805e3722cf8338d51"}, "tags": {"0.5--h360a1d4_4": "sha256:8b39953718d53c5b4f809531f750f7d0708a72275cb3028ec7d6c7ad2538c118", "0.5--h360a1d4_5": "sha256:d59efa5c10dceaf5545f744ca69bb8969538d75e2cfd9d7167cd300b1d35d2e2", "0.5--h264e753_6": "sha256:f6229b88bb27675d2c6d1242995843738668d22933fa613805e3722cf8338d51"}, "docker": "quay.io/biocontainers/msisensor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/msisensor.
shpc-registry automated BioContainers addition for msisensor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msisensor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msisensor:0.5--h264e753_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msisensor/0.5--h264e753_6
$ module help quay.io/biocontainers/msisensor/0.5--h264e753_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msisensor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msisensor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msisensor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msisensor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msisensor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msisensor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### msisensor

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