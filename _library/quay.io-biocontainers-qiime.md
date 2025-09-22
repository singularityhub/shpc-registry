---
layout: container
name:  "quay.io/biocontainers/qiime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/qiime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/qiime/container.yaml"
updated_at: "2025-09-22 03:18:54.871083"
latest: "1.9.1--py_3"
container_url: "https://biocontainers.pro/tools/qiime"

versions:
 - "1.9.1--py_3"
description: "shpc-registry automated BioContainers addition for qiime"
config: {"url": "https://biocontainers.pro/tools/qiime", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for qiime", "latest": {"1.9.1--py_3": "sha256:8caaf6dd51b3a1231b182223110f1d67a43f68fec24b87805a03a541bde8c7ae"}, "tags": {"1.9.1--py_3": "sha256:8caaf6dd51b3a1231b182223110f1d67a43f68fec24b87805a03a541bde8c7ae"}, "docker": "quay.io/biocontainers/qiime"}
---

This module is a singularity container wrapper for quay.io/biocontainers/qiime.
shpc-registry automated BioContainers addition for qiime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/qiime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/qiime:1.9.1--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/qiime/1.9.1--py_3
$ module help quay.io/biocontainers/qiime/1.9.1--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qiime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qiime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qiime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qiime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qiime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qiime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### qiime

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