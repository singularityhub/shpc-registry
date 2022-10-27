---
layout: container
name:  "quay.io/biocontainers/barcode_splitter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/barcode_splitter/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/barcode_splitter/container.yaml"
updated_at: "2022-10-27 00:36:00.667431"
latest: "0.18.6--py_0"
container_url: "https://biocontainers.pro/tools/barcode_splitter"
aliases:
 - "barcode_splitter"
versions:
 - "0.18.6--py_0"
description: "shpc-registry automated BioContainers addition for barcode_splitter"
config: {"url": "https://biocontainers.pro/tools/barcode_splitter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for barcode_splitter", "latest": {"0.18.6--py_0": "sha256:9793d3e815752d640feeaee8f55b7171e247bbbb8ceb8e86d8bbbbfc69a0f650"}, "tags": {"0.18.6--py_0": "sha256:9793d3e815752d640feeaee8f55b7171e247bbbb8ceb8e86d8bbbbfc69a0f650"}, "docker": "quay.io/biocontainers/barcode_splitter", "aliases": {"barcode_splitter": "/usr/local/bin/barcode_splitter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/barcode_splitter.
shpc-registry automated BioContainers addition for barcode_splitter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/barcode_splitter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/barcode_splitter:0.18.6--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/barcode_splitter/0.18.6--py_0
$ module help quay.io/biocontainers/barcode_splitter/0.18.6--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### barcode_splitter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### barcode_splitter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### barcode_splitter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### barcode_splitter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### barcode_splitter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### barcode_splitter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### barcode_splitter

```bash
$ singularity exec <container> /usr/local/bin/barcode_splitter
$ podman run --it --rm --entrypoint /usr/local/bin/barcode_splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barcode_splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
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