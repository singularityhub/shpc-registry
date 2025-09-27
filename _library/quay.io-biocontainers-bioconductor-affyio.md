---
layout: container
name:  "quay.io/biocontainers/bioconductor-affyio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affyio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affyio/container.yaml"
updated_at: "2025-09-27 03:44:11.227135"
latest: "1.76.0--r44h15a9599_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affyio"

versions:
 - "1.64.0--r41hc0cfd56_2"
 - "1.68.0--r42hc0cfd56_0"
 - "1.68.0--r42ha9d7317_1"
 - "1.70.0--r43ha9d7317_0"
 - "1.72.0--r43ha9d7317_0"
 - "1.72.0--r43ha9d7317_1"
 - "1.76.0--r44h15a9599_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affyio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affyio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affyio", "latest": {"1.76.0--r44h15a9599_0": "sha256:79c4d4fccfcec851da80a7b07efd8e9c907783e593d467fed22d4ced50728bb2"}, "tags": {"1.64.0--r41hc0cfd56_2": "sha256:07e979c261f9a7e21f73aa7b06bc50fd78e60be422df35c880a650bac85087d7", "1.68.0--r42hc0cfd56_0": "sha256:4fc4b4083c4c7e8146676cbcf60f0173b5d36169334e0f9f5596f53a97a836c1", "1.68.0--r42ha9d7317_1": "sha256:ece51aa11a6cc140057f42438846c73e07f8cc9cc5a9831f10b99a1267d4bd02", "1.70.0--r43ha9d7317_0": "sha256:fa2c8a252c338b5c277fe617f640009ea0c58d55db3daa58fc5549dca4350fb4", "1.72.0--r43ha9d7317_0": "sha256:77ac166c5c87b9394e5879d8f1d2edd2f74d4fe1eab10d50d08e94a4a9764085", "1.72.0--r43ha9d7317_1": "sha256:74a5796ff0487d1a8035dc98d6c56f239469886e7cfb07c795d47ec54cc9e137", "1.76.0--r44h15a9599_0": "sha256:79c4d4fccfcec851da80a7b07efd8e9c907783e593d467fed22d4ced50728bb2"}, "docker": "quay.io/biocontainers/bioconductor-affyio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affyio.
shpc-registry automated BioContainers addition for bioconductor-affyio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affyio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affyio:1.76.0--r44h15a9599_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affyio/1.76.0--r44h15a9599_0
$ module help quay.io/biocontainers/bioconductor-affyio/1.76.0--r44h15a9599_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affyio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affyio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affyio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affyio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affyio

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