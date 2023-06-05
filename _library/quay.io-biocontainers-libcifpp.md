---
layout: container
name:  "quay.io/biocontainers/libcifpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libcifpp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libcifpp/container.yaml"
updated_at: "2023-06-05 03:24:22.263850"
latest: "5.0.0--hd9a51b5_2"
container_url: "https://biocontainers.pro/tools/libcifpp"

versions:
 - "5.0.0--h46c59ee_0"
 - "5.0.0--hd9a51b5_2"
description: "singularity registry hpc automated addition for libcifpp"
config: {"url": "https://biocontainers.pro/tools/libcifpp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for libcifpp", "latest": {"5.0.0--hd9a51b5_2": "sha256:f5870c8cea236d1e532de1024f55ec92a8b0b29cc2e4e55b2b5609cf42578cef"}, "tags": {"5.0.0--h46c59ee_0": "sha256:339abdd36e61aeb29221d0de8d0ceb05f96eec657ca3ffb0d4ba86cb568f2734", "5.0.0--hd9a51b5_2": "sha256:f5870c8cea236d1e532de1024f55ec92a8b0b29cc2e4e55b2b5609cf42578cef"}, "docker": "quay.io/biocontainers/libcifpp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libcifpp.
singularity registry hpc automated addition for libcifpp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libcifpp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libcifpp:5.0.0--hd9a51b5_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libcifpp/5.0.0--hd9a51b5_2
$ module help quay.io/biocontainers/libcifpp/5.0.0--hd9a51b5_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libcifpp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libcifpp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libcifpp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libcifpp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libcifpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libcifpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libcifpp

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