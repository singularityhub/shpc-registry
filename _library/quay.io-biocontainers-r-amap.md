---
layout: container
name:  "quay.io/biocontainers/r-amap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-amap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-amap/container.yaml"
updated_at: "2022-10-27 00:45:38.926907"
latest: "0.8_14--r3.3.2_1"
container_url: "https://biocontainers.pro/tools/r-amap"

versions:
 - "0.8_14--r3.3.2_1"
description: "shpc-registry automated BioContainers addition for r-amap"
config: {"url": "https://biocontainers.pro/tools/r-amap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-amap", "latest": {"0.8_14--r3.3.2_1": "sha256:7ba9675375f41b24f0835c201ce86d54bf283ea32cdc097b3d2f4ad8a57edae1"}, "tags": {"0.8_14--r3.3.2_1": "sha256:7ba9675375f41b24f0835c201ce86d54bf283ea32cdc097b3d2f4ad8a57edae1"}, "docker": "quay.io/biocontainers/r-amap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-amap.
shpc-registry automated BioContainers addition for r-amap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-amap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-amap:0.8_14--r3.3.2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-amap/0.8_14--r3.3.2_1
$ module help quay.io/biocontainers/r-amap/0.8_14--r3.3.2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-amap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-amap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-amap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-amap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-amap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-amap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-amap

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