---
layout: container
name:  "quay.io/biocontainers/nest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nest/container.yaml"
updated_at: "2025-07-17 04:05:37.256821"
latest: "2.14.0--py35h060fc9d_3"
container_url: "https://biocontainers.pro/tools/nest"

versions:
 - "2.14.0--py35h060fc9d_3"
 - "2.14.0--py27h060fc9d_3"
description: "shpc-registry automated BioContainers addition for nest"
config: {"url": "https://biocontainers.pro/tools/nest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nest", "latest": {"2.14.0--py35h060fc9d_3": "sha256:2060e95b6445bb726e8828482f04f74f6b0e2646ebd5998e26df55552f8f9a9a"}, "tags": {"2.14.0--py35h060fc9d_3": "sha256:2060e95b6445bb726e8828482f04f74f6b0e2646ebd5998e26df55552f8f9a9a", "2.14.0--py27h060fc9d_3": "sha256:dbdab9cd07feb4e90458a306182e3412877ba2d588ac94e7f2fd998c698a52b3"}, "docker": "quay.io/biocontainers/nest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/nest.
shpc-registry automated BioContainers addition for nest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nest:2.14.0--py35h060fc9d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nest/2.14.0--py35h060fc9d_3
$ module help quay.io/biocontainers/nest/2.14.0--py35h060fc9d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nest

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