---
layout: container
name:  "quay.io/biocontainers/bpp-seq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bpp-seq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bpp-seq/container.yaml"
updated_at: "2024-06-12 02:37:28.973439"
latest: "2.4.1--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/bpp-seq"

versions:
 - "2.4.1--h9f5acd7_3"
 - "2.4.1--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for bpp-seq"
config: {"url": "https://biocontainers.pro/tools/bpp-seq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bpp-seq", "latest": {"2.4.1--h4ac6f70_4": "sha256:a7cc354a72275009f10d11cd9ed6f2b13b2dcdaf04547d78e6ce11ac79b1da39"}, "tags": {"2.4.1--h9f5acd7_3": "sha256:489c03f1fd004953f07ddb923b369de9dff640c1c72d6caff8e3abdfc06560ae", "2.4.1--h4ac6f70_4": "sha256:a7cc354a72275009f10d11cd9ed6f2b13b2dcdaf04547d78e6ce11ac79b1da39"}, "docker": "quay.io/biocontainers/bpp-seq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bpp-seq.
shpc-registry automated BioContainers addition for bpp-seq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bpp-seq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bpp-seq:2.4.1--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bpp-seq/2.4.1--h4ac6f70_4
$ module help quay.io/biocontainers/bpp-seq/2.4.1--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bpp-seq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bpp-seq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bpp-seq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bpp-seq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bpp-seq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bpp-seq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bpp-seq

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