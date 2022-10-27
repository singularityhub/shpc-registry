---
layout: container
name:  "quay.io/biocontainers/easydev"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/easydev/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/easydev/container.yaml"
updated_at: "2022-10-27 00:47:46.240671"
latest: "0.9.31--py35_1"
container_url: "https://biocontainers.pro/tools/easydev"

versions:
 - "0.9.31--py35_1"
description: "shpc-registry automated BioContainers addition for easydev"
config: {"url": "https://biocontainers.pro/tools/easydev", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for easydev", "latest": {"0.9.31--py35_1": "sha256:cd5de468b98c07c4277201fe5b4464a5a25343df8dc27239772bd9fdb7728e02"}, "tags": {"0.9.31--py35_1": "sha256:cd5de468b98c07c4277201fe5b4464a5a25343df8dc27239772bd9fdb7728e02"}, "docker": "quay.io/biocontainers/easydev"}
---

This module is a singularity container wrapper for quay.io/biocontainers/easydev.
shpc-registry automated BioContainers addition for easydev
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/easydev
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/easydev:0.9.31--py35_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/easydev/0.9.31--py35_1
$ module help quay.io/biocontainers/easydev/0.9.31--py35_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### easydev-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### easydev-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### easydev-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### easydev-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### easydev-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### easydev-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### easydev

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