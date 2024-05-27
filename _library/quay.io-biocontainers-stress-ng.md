---
layout: container
name:  "quay.io/biocontainers/stress-ng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stress-ng/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/stress-ng/container.yaml"
updated_at: "2024-05-27 02:48:03.576232"
latest: "0.12.04"
container_url: "https://biocontainers.pro/tools/stress-ng"
aliases:
 - "stress-ng"
versions:
 - "0.12.04"
description: "shpc-registry automated BioContainers addition for stress-ng"
config: {"url": "https://biocontainers.pro/tools/stress-ng", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stress-ng", "latest": {"0.12.04": "sha256:88a031810226041116cf47aa6ed03bd47ee49f7ad448a294dbcab09f3e88f8f6"}, "tags": {"0.12.04": "sha256:88a031810226041116cf47aa6ed03bd47ee49f7ad448a294dbcab09f3e88f8f6"}, "docker": "quay.io/biocontainers/stress-ng", "aliases": {"stress-ng": "/usr/local/bin/stress-ng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stress-ng.
shpc-registry automated BioContainers addition for stress-ng
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stress-ng
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stress-ng:0.12.04
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stress-ng/0.12.04
$ module help quay.io/biocontainers/stress-ng/0.12.04
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stress-ng-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stress-ng-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stress-ng-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stress-ng-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stress-ng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stress-ng-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stress-ng

```bash
$ singularity exec <container> /usr/local/bin/stress-ng
$ podman run --it --rm --entrypoint /usr/local/bin/stress-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stress-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
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