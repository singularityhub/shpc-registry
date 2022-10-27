---
layout: container
name:  "quay.io/biocontainers/pydotplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pydotplus/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pydotplus/container.yaml"
updated_at: "2022-10-27 01:10:05.922824"
latest: "2.0.2--py36_0"
container_url: "https://biocontainers.pro/tools/pydotplus"

versions:
 - "2.0.2--py36_0"
description: "shpc-registry automated BioContainers addition for pydotplus"
config: {"url": "https://biocontainers.pro/tools/pydotplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pydotplus", "latest": {"2.0.2--py36_0": "sha256:f0f7b42ed369c94bd13c4fefe29d373840618c08a52f74f7cb0e54ddf716b425"}, "tags": {"2.0.2--py36_0": "sha256:f0f7b42ed369c94bd13c4fefe29d373840618c08a52f74f7cb0e54ddf716b425"}, "docker": "quay.io/biocontainers/pydotplus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pydotplus.
shpc-registry automated BioContainers addition for pydotplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pydotplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pydotplus:2.0.2--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pydotplus/2.0.2--py36_0
$ module help quay.io/biocontainers/pydotplus/2.0.2--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pydotplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pydotplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pydotplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pydotplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pydotplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pydotplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pydotplus

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