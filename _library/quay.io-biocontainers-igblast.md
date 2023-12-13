---
layout: container
name:  "quay.io/biocontainers/igblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/igblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/igblast/container.yaml"
updated_at: "2023-12-13 02:41:40.969195"
latest: "1.21.0--pl5321h6a68c12_1"
container_url: "https://biocontainers.pro/tools/igblast"

versions:
 - "1.9.0--hab87656_0"
 - "1.19.0--pl5321h3928612_0"
 - "1.17.1--pl5321h3928612_1"
 - "1.15.0--h18cd00f_0"
 - "1.10.0--h6ac72b6_1"
 - "1.20.0--pl5321hf1761c0_0"
 - "1.21.0--pl5321h6a68c12_1"
description: "shpc-registry automated BioContainers addition for igblast"
config: {"url": "https://biocontainers.pro/tools/igblast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for igblast", "latest": {"1.21.0--pl5321h6a68c12_1": "sha256:6a1ab60783c73c7953d2e758e27cb3a0c4e09fe5516134dc5c845190c19a7141"}, "tags": {"1.9.0--hab87656_0": "sha256:2253ac59f465ec415feede6a43b244fd7ed36a1ded3263603b5ea43be3cb2fed", "1.19.0--pl5321h3928612_0": "sha256:0cc5a7bd4b964ccd096fdd91a843abf14cd5f1a0b14b40eb964442e501841621", "1.17.1--pl5321h3928612_1": "sha256:9e268b2be74b82a7fc6297c86ed4fca244ceae4e290c25df734c4d1cbc6962e3", "1.15.0--h18cd00f_0": "sha256:13eba2ad6d1a9d500d84beb1eeb51c8341b2c3b3b6279bdc86dc81955c347c31", "1.10.0--h6ac72b6_1": "sha256:fe26238d113f5abc6ce3c34c6a336e0286f90fb32a4ef4362a13daba88f222f3", "1.20.0--pl5321hf1761c0_0": "sha256:4ef1a38be836d223f1740ac4a93d1bd3dd1713233a149436793438bd4edfada9", "1.21.0--pl5321h6a68c12_1": "sha256:6a1ab60783c73c7953d2e758e27cb3a0c4e09fe5516134dc5c845190c19a7141"}, "docker": "quay.io/biocontainers/igblast"}
---

This module is a singularity container wrapper for quay.io/biocontainers/igblast.
shpc-registry automated BioContainers addition for igblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/igblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/igblast:1.21.0--pl5321h6a68c12_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/igblast/1.21.0--pl5321h6a68c12_1
$ module help quay.io/biocontainers/igblast/1.21.0--pl5321h6a68c12_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### igblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### igblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### igblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### igblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### igblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### igblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### igblast

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