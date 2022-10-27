---
layout: container
name:  "quay.io/biocontainers/r-rpmg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rpmg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-rpmg/container.yaml"
updated_at: "2022-10-27 01:05:05.728618"
latest: "2.2_1--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-rpmg"

versions:
 - "2.2_1--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-rpmg"
config: {"url": "https://biocontainers.pro/tools/r-rpmg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rpmg", "latest": {"2.2_1--r3.2.2_0": "sha256:5dd7b8a2f56aa6c3976776c3bb730d30d8c0f9d64f72e76e39cf198e07eafa71"}, "tags": {"2.2_1--r3.2.2_0": "sha256:5dd7b8a2f56aa6c3976776c3bb730d30d8c0f9d64f72e76e39cf198e07eafa71"}, "docker": "quay.io/biocontainers/r-rpmg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rpmg.
shpc-registry automated BioContainers addition for r-rpmg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rpmg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rpmg:2.2_1--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rpmg/2.2_1--r3.2.2_0
$ module help quay.io/biocontainers/r-rpmg/2.2_1--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rpmg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rpmg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rpmg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rpmg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rpmg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rpmg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-rpmg

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