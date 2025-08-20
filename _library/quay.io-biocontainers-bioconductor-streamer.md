---
layout: container
name:  "quay.io/biocontainers/bioconductor-streamer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-streamer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-streamer/container.yaml"
updated_at: "2025-08-20 03:57:21.572406"
latest: "1.52.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-streamer"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.46.0--r43ha9d7317_0"
 - "1.48.0--r43ha9d7317_0"
 - "1.52.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-streamer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-streamer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-streamer", "latest": {"1.52.0--r44h3df3fcb_0": "sha256:47425dd901e4dea7550b11ec84e8360a9748782dc8b5db59159eb73fc7fa2dc6"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:acb2801c86ce7a05513b7acd766bc8f96f85b26178579da76d322a40fdc78eaa", "1.44.0--r42hc0cfd56_0": "sha256:232f1ab70bcdf8b662df96692b50288c8565a83fbcf078ef1d8203f1da87fdfe", "1.44.0--r42ha9d7317_1": "sha256:e814eeb7dc994277271294612efc7f8dc8e9f99c74fbfa0df28f67bd37b90459", "1.46.0--r43ha9d7317_0": "sha256:f559cfcba4f95d6f34068057bbef845fef72523eaae4b07fff8aa373b2e22d9c", "1.48.0--r43ha9d7317_0": "sha256:5b362c93af5de3654ed9931b447dc2c513e71463aa626dde4c5271ae6346a304", "1.52.0--r44h3df3fcb_0": "sha256:47425dd901e4dea7550b11ec84e8360a9748782dc8b5db59159eb73fc7fa2dc6"}, "docker": "quay.io/biocontainers/bioconductor-streamer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-streamer.
shpc-registry automated BioContainers addition for bioconductor-streamer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-streamer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-streamer:1.52.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-streamer/1.52.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-streamer/1.52.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-streamer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-streamer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-streamer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-streamer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-streamer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-streamer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-streamer

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