---
layout: container
name:  "quay.io/biocontainers/r-bc3net"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-bc3net/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-bc3net/container.yaml"
updated_at: "2022-10-27 00:59:56.075166"
latest: "1.0.4--r36h6115d3f_1"
container_url: "https://biocontainers.pro/tools/r-bc3net"

versions:
 - "1.0.4--r36h6115d3f_1"
description: "shpc-registry automated BioContainers addition for r-bc3net"
config: {"url": "https://biocontainers.pro/tools/r-bc3net", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-bc3net", "latest": {"1.0.4--r36h6115d3f_1": "sha256:63a880f7da65a14edaff0c7db4b5c498e4cf91c5ab6e50c25404cc777ac6b0ca"}, "tags": {"1.0.4--r36h6115d3f_1": "sha256:63a880f7da65a14edaff0c7db4b5c498e4cf91c5ab6e50c25404cc777ac6b0ca"}, "docker": "quay.io/biocontainers/r-bc3net"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-bc3net.
shpc-registry automated BioContainers addition for r-bc3net
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-bc3net
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-bc3net:1.0.4--r36h6115d3f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-bc3net/1.0.4--r36h6115d3f_1
$ module help quay.io/biocontainers/r-bc3net/1.0.4--r36h6115d3f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-bc3net-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-bc3net-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-bc3net-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-bc3net-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-bc3net-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-bc3net-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-bc3net

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