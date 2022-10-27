---
layout: container
name:  "quay.io/biocontainers/schema-salad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/schema-salad/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/schema-salad/container.yaml"
updated_at: "2022-10-27 00:47:15.466449"
latest: "2.7.20180809223002--py_0"
container_url: "https://biocontainers.pro/tools/schema-salad"

versions:
 - "2.7.20180809223002--py_0"
description: "shpc-registry automated BioContainers addition for schema-salad"
config: {"url": "https://biocontainers.pro/tools/schema-salad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for schema-salad", "latest": {"2.7.20180809223002--py_0": "sha256:30b092bba2f1edac1cd7bbe46d0f89d706a6cfa6ecf2a327fce6ebe91953d8e6"}, "tags": {"2.7.20180809223002--py_0": "sha256:30b092bba2f1edac1cd7bbe46d0f89d706a6cfa6ecf2a327fce6ebe91953d8e6"}, "docker": "quay.io/biocontainers/schema-salad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/schema-salad.
shpc-registry automated BioContainers addition for schema-salad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/schema-salad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/schema-salad:2.7.20180809223002--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/schema-salad/2.7.20180809223002--py_0
$ module help quay.io/biocontainers/schema-salad/2.7.20180809223002--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### schema-salad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### schema-salad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### schema-salad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### schema-salad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### schema-salad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### schema-salad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### schema-salad

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