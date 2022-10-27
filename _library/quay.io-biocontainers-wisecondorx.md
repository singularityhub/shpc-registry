---
layout: container
name:  "quay.io/biocontainers/wisecondorx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wisecondorx/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/wisecondorx/container.yaml"
updated_at: "2022-10-27 00:34:36.632300"
latest: "1.2.5--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/wisecondorx"
aliases:
 - "WisecondorX"
versions:
 - "1.2.5--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for wisecondorx"
config: {"url": "https://biocontainers.pro/tools/wisecondorx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wisecondorx", "latest": {"1.2.5--pyh5e36f6f_0": "sha256:8e2557f4bea29f796cd0eff1bcaf3f4fe3c52a0ea45c2ae685833715732d0bcb"}, "tags": {"1.2.5--pyh5e36f6f_0": "sha256:8e2557f4bea29f796cd0eff1bcaf3f4fe3c52a0ea45c2ae685833715732d0bcb"}, "docker": "quay.io/biocontainers/wisecondorx", "aliases": {"WisecondorX": "/usr/local/bin/WisecondorX"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wisecondorx.
shpc-registry automated BioContainers addition for wisecondorx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wisecondorx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wisecondorx:1.2.5--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wisecondorx/1.2.5--pyh5e36f6f_0
$ module help quay.io/biocontainers/wisecondorx/1.2.5--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wisecondorx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wisecondorx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wisecondorx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wisecondorx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wisecondorx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wisecondorx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### WisecondorX

```bash
$ singularity exec <container> /usr/local/bin/WisecondorX
$ podman run --it --rm --entrypoint /usr/local/bin/WisecondorX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/WisecondorX   -v ${PWD} -w ${PWD} <container> -c " $@"
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