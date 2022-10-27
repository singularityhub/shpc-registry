---
layout: container
name:  "quay.io/biocontainers/deepbinner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepbinner/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepbinner/container.yaml"
updated_at: "2022-10-27 00:44:52.164954"
latest: "0.2.0--pyh24bf2e0_1"
container_url: "https://biocontainers.pro/tools/deepbinner"
aliases:
 - "deepbinner"
versions:
 - "0.2.0--pyh24bf2e0_1"
description: "shpc-registry automated BioContainers addition for deepbinner"
config: {"url": "https://biocontainers.pro/tools/deepbinner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepbinner", "latest": {"0.2.0--pyh24bf2e0_1": "sha256:ba3b0b553d43de57dedf56e11276213997ed5fa3eb9400675bbe5c4bb670e7b2"}, "tags": {"0.2.0--pyh24bf2e0_1": "sha256:ba3b0b553d43de57dedf56e11276213997ed5fa3eb9400675bbe5c4bb670e7b2"}, "docker": "quay.io/biocontainers/deepbinner", "aliases": {"deepbinner": "/usr/local/bin/deepbinner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepbinner.
shpc-registry automated BioContainers addition for deepbinner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepbinner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepbinner:0.2.0--pyh24bf2e0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepbinner/0.2.0--pyh24bf2e0_1
$ module help quay.io/biocontainers/deepbinner/0.2.0--pyh24bf2e0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepbinner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepbinner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepbinner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepbinner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepbinner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepbinner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepbinner

```bash
$ singularity exec <container> /usr/local/bin/deepbinner
$ podman run --it --rm --entrypoint /usr/local/bin/deepbinner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepbinner   -v ${PWD} -w ${PWD} <container> -c " $@"
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