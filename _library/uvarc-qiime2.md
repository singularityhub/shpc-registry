---
layout: container
name:  "uvarc/qiime2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/uvarc/qiime2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/uvarc/qiime2/container.yaml"
updated_at: "2024-07-15 03:17:17.023794"
latest: "2022.2"
container_url: "https://hub.docker.com/r/uvarc/qiime2"

versions:
 - "2020.8"
 - "2022.2"
description: "QIIME2. Same functionality as the official image but less than half the size. Includes packages Empress and PICRUSt2."
config: {"docker": "uvarc/qiime2", "latest": {"2022.2": "sha256:fc9cd107f07edeacdc1d1a633cfd0546bb982c3f6f40fc0fb721954589ea13f8"}, "tags": {"2020.8": "sha256:7b380f190ae5de431a9b350b6b7edef1bc718e5d2fc4412a543a7201d95c4999", "2022.2": "sha256:fc9cd107f07edeacdc1d1a633cfd0546bb982c3f6f40fc0fb721954589ea13f8"}, "filter": ["2021*"], "maintainer": "@vsoch", "url": "https://hub.docker.com/r/uvarc/qiime2", "description": "QIIME2. Same functionality as the official image but less than half the size. Includes packages Empress and PICRUSt2."}
---

This module is a singularity container wrapper for uvarc/qiime2.
QIIME2. Same functionality as the official image but less than half the size. Includes packages Empress and PICRUSt2.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install uvarc/qiime2
```

Or a specific version:

```bash
$ shpc install uvarc/qiime2:2022.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load uvarc/qiime2/2022.2
$ module help uvarc/qiime2/2022.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qiime2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qiime2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qiime2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qiime2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qiime2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qiime2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### qiime2

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