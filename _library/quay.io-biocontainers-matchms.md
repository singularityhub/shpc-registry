---
layout: container
name:  "quay.io/biocontainers/matchms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/matchms/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/matchms/container.yaml"
updated_at: "2022-10-27 01:12:37.768415"
latest: "0.9.2--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/matchms"

versions:
 - "0.9.2--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for matchms"
config: {"url": "https://biocontainers.pro/tools/matchms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for matchms", "latest": {"0.9.2--pyh5e36f6f_0": "sha256:d1a8f1d785b8993724305e4684caae5bc194b9fbb99053883eacfead753f20c0"}, "tags": {"0.9.2--pyh5e36f6f_0": "sha256:d1a8f1d785b8993724305e4684caae5bc194b9fbb99053883eacfead753f20c0"}, "docker": "quay.io/biocontainers/matchms"}
---

This module is a singularity container wrapper for quay.io/biocontainers/matchms.
shpc-registry automated BioContainers addition for matchms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/matchms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/matchms:0.9.2--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/matchms/0.9.2--pyh5e36f6f_0
$ module help quay.io/biocontainers/matchms/0.9.2--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### matchms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### matchms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### matchms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### matchms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### matchms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### matchms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### matchms

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