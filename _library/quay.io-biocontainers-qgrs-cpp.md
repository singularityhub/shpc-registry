---
layout: container
name:  "quay.io/biocontainers/qgrs-cpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/qgrs-cpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/qgrs-cpp/container.yaml"
updated_at: "2023-06-16 03:14:55.018178"
latest: "1.0--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/qgrs-cpp"
aliases:
 - "qgrs"
versions:
 - "1.0--h87f3376_2"
 - "1.0--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for qgrs-cpp"
config: {"url": "https://biocontainers.pro/tools/qgrs-cpp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for qgrs-cpp", "latest": {"1.0--hdbdd923_4": "sha256:37a513bf2aef84bd075e9649501ace9cc028c1590aa787a40063d2d7efefecdf"}, "tags": {"1.0--h87f3376_2": "sha256:a521ba710442d28ccbe42a533925121e948d2a80503e6580e47fa9fad5d2e53e", "1.0--hdbdd923_4": "sha256:37a513bf2aef84bd075e9649501ace9cc028c1590aa787a40063d2d7efefecdf"}, "docker": "quay.io/biocontainers/qgrs-cpp", "aliases": {"qgrs": "/usr/local/bin/qgrs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/qgrs-cpp.
shpc-registry automated BioContainers addition for qgrs-cpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/qgrs-cpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/qgrs-cpp:1.0--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/qgrs-cpp/1.0--hdbdd923_4
$ module help quay.io/biocontainers/qgrs-cpp/1.0--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qgrs-cpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qgrs-cpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qgrs-cpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qgrs-cpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qgrs-cpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qgrs-cpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qgrs

```bash
$ singularity exec <container> /usr/local/bin/qgrs
$ podman run --it --rm --entrypoint /usr/local/bin/qgrs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgrs   -v ${PWD} -w ${PWD} <container> -c " $@"
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