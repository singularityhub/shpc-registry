---
layout: container
name:  "quay.io/biocontainers/lrge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrge/container.yaml"
updated_at: "2025-11-01 03:41:57.321117"
latest: "0.2.1--h9f13da3_0"
container_url: "https://biocontainers.pro/tools/lrge"
aliases:
 - "lrge"
versions:
 - "0.1.1--h53be72d_0"
 - "0.1.3--h9f13da3_1"
 - "0.2.0--h9f13da3_0"
 - "0.2.1--h9f13da3_0"
description: "singularity registry hpc automated addition for lrge"
config: {"url": "https://biocontainers.pro/tools/lrge", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lrge", "latest": {"0.2.1--h9f13da3_0": "sha256:5dc2d2bf7f6cbcf0ade9f64cbf032c65aa59332bc78d9b8cfe4bad29483bccfd"}, "tags": {"0.1.1--h53be72d_0": "sha256:05853c2e08978ceded69933b786da7cab85e8f773519a9ada60ea3fd440932fa", "0.1.3--h9f13da3_1": "sha256:6350ada8cc260bb87c8560c3876fca4c3ed536e78af28f841fb7b693cef3e957", "0.2.0--h9f13da3_0": "sha256:ee000b45459bf68582e399a3921c649cca3bac800cad8731dbf77af3c2d0fa36", "0.2.1--h9f13da3_0": "sha256:5dc2d2bf7f6cbcf0ade9f64cbf032c65aa59332bc78d9b8cfe4bad29483bccfd"}, "docker": "quay.io/biocontainers/lrge", "aliases": {"lrge": "/usr/local/bin/lrge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrge.
singularity registry hpc automated addition for lrge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrge:0.2.1--h9f13da3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrge/0.2.1--h9f13da3_0
$ module help quay.io/biocontainers/lrge/0.2.1--h9f13da3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lrge

```bash
$ singularity exec <container> /usr/local/bin/lrge
$ podman run --it --rm --entrypoint /usr/local/bin/lrge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrge   -v ${PWD} -w ${PWD} <container> -c " $@"
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