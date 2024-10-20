---
layout: container
name:  "quay.io/biocontainers/gfainject"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfainject/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfainject/container.yaml"
updated_at: "2024-10-20 03:00:49.933028"
latest: "0.1.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/gfainject"
aliases:
 - "gfainject"
versions:
 - "0.1.0--h4349ce8_0"
description: "singularity registry hpc automated addition for gfainject"
config: {"url": "https://biocontainers.pro/tools/gfainject", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfainject", "latest": {"0.1.0--h4349ce8_0": "sha256:3248af85b4a73103eac9b5fa8f5da7f3918377cbf41173c7a900302f68a041cb"}, "tags": {"0.1.0--h4349ce8_0": "sha256:3248af85b4a73103eac9b5fa8f5da7f3918377cbf41173c7a900302f68a041cb"}, "docker": "quay.io/biocontainers/gfainject", "aliases": {"gfainject": "/usr/local/bin/gfainject"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfainject.
singularity registry hpc automated addition for gfainject
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfainject
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfainject:0.1.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfainject/0.1.0--h4349ce8_0
$ module help quay.io/biocontainers/gfainject/0.1.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfainject-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfainject-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfainject-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfainject-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfainject-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfainject-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gfainject

```bash
$ singularity exec <container> /usr/local/bin/gfainject
$ podman run --it --rm --entrypoint /usr/local/bin/gfainject   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfainject   -v ${PWD} -w ${PWD} <container> -c " $@"
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