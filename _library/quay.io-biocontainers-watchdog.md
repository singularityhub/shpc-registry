---
layout: container
name:  "quay.io/biocontainers/watchdog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/watchdog/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/watchdog/container.yaml"
updated_at: "2024-12-21 03:14:27.400493"
latest: "0.8.3--py36_0"
container_url: "https://biocontainers.pro/tools/watchdog"

versions:
 - "0.8.3--py36_0"
 - "0.8.3--py35_0"
description: "shpc-registry automated BioContainers addition for watchdog"
config: {"url": "https://biocontainers.pro/tools/watchdog", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for watchdog", "latest": {"0.8.3--py36_0": "sha256:1e33b8ae6b970d3719d552a4242a750bfa3d0ecdd21999542980d90fcdaa2b1a"}, "tags": {"0.8.3--py36_0": "sha256:1e33b8ae6b970d3719d552a4242a750bfa3d0ecdd21999542980d90fcdaa2b1a", "0.8.3--py35_0": "sha256:0370da3d796083ce5c30de8a6e8ef5ba08d220ef7f15c7aa640c5af4fb0040f2"}, "docker": "quay.io/biocontainers/watchdog"}
---

This module is a singularity container wrapper for quay.io/biocontainers/watchdog.
shpc-registry automated BioContainers addition for watchdog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/watchdog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/watchdog:0.8.3--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/watchdog/0.8.3--py36_0
$ module help quay.io/biocontainers/watchdog/0.8.3--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### watchdog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### watchdog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### watchdog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### watchdog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### watchdog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### watchdog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### watchdog

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