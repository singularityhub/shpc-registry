---
layout: container
name:  "quay.io/biocontainers/razers3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/razers3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/razers3/container.yaml"
updated_at: "2023-12-15 02:36:32.524953"
latest: "3.5.8--h6dccd9a_4"
container_url: "https://biocontainers.pro/tools/razers3"
aliases:
 - "razers3"
versions:
 - "3.5.8--h19e8d03_2"
 - "3.5.8--h19e8d03_3"
 - "3.5.8--h6dccd9a_4"
description: "shpc-registry automated BioContainers addition for razers3"
config: {"url": "https://biocontainers.pro/tools/razers3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for razers3", "latest": {"3.5.8--h6dccd9a_4": "sha256:2d65a111d157a968ab96dbdd23ca6bdc4e7f69a4114c0c60f3197b99ca379b31"}, "tags": {"3.5.8--h19e8d03_2": "sha256:6fa1a8edecb657c83c35570973ccffb55309006e0b9f68e8c32ee7300b055cae", "3.5.8--h19e8d03_3": "sha256:3b029bec8af6bdd00a79a510927e89179cee6f388b1f8355e99df0809f3d6945", "3.5.8--h6dccd9a_4": "sha256:2d65a111d157a968ab96dbdd23ca6bdc4e7f69a4114c0c60f3197b99ca379b31"}, "docker": "quay.io/biocontainers/razers3", "aliases": {"razers3": "/usr/local/bin/razers3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/razers3.
shpc-registry automated BioContainers addition for razers3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/razers3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/razers3:3.5.8--h6dccd9a_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/razers3/3.5.8--h6dccd9a_4
$ module help quay.io/biocontainers/razers3/3.5.8--h6dccd9a_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### razers3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### razers3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### razers3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### razers3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### razers3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### razers3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### razers3

```bash
$ singularity exec <container> /usr/local/bin/razers3
$ podman run --it --rm --entrypoint /usr/local/bin/razers3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/razers3   -v ${PWD} -w ${PWD} <container> -c " $@"
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