---
layout: container
name:  "quay.io/biocontainers/crnsimulator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crnsimulator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/crnsimulator/container.yaml"
updated_at: "2022-10-27 00:21:30.305350"
latest: "0.9--pyh5bfb8f1_0"
container_url: "https://biocontainers.pro/tools/crnsimulator"
aliases:
 - "crnsimulator"
versions:
 - "0.9--pyh5bfb8f1_0"
description: "shpc-registry automated BioContainers addition for crnsimulator"
config: {"url": "https://biocontainers.pro/tools/crnsimulator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crnsimulator", "latest": {"0.9--pyh5bfb8f1_0": "sha256:009167f69f138a1a0a196b1ffd09b92420e7a072cfb642e1e6afd418a2bd5f92"}, "tags": {"0.9--pyh5bfb8f1_0": "sha256:009167f69f138a1a0a196b1ffd09b92420e7a072cfb642e1e6afd418a2bd5f92"}, "docker": "quay.io/biocontainers/crnsimulator", "aliases": {"crnsimulator": "/usr/local/bin/crnsimulator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crnsimulator.
shpc-registry automated BioContainers addition for crnsimulator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crnsimulator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crnsimulator:0.9--pyh5bfb8f1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crnsimulator/0.9--pyh5bfb8f1_0
$ module help quay.io/biocontainers/crnsimulator/0.9--pyh5bfb8f1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crnsimulator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crnsimulator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crnsimulator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crnsimulator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crnsimulator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crnsimulator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crnsimulator

```bash
$ singularity exec <container> /usr/local/bin/crnsimulator
$ podman run --it --rm --entrypoint /usr/local/bin/crnsimulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crnsimulator   -v ${PWD} -w ${PWD} <container> -c " $@"
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