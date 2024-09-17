---
layout: container
name:  "quay.io/biocontainers/est-sfs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/est-sfs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/est-sfs/container.yaml"
updated_at: "2024-09-17 02:29:46.687993"
latest: "2.04--h245ed52_0"
container_url: "https://biocontainers.pro/tools/est-sfs"
aliases:
 - "est-sfs"
versions:
 - "2.04--h245ed52_0"
description: "singularity registry hpc automated addition for est-sfs"
config: {"url": "https://biocontainers.pro/tools/est-sfs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for est-sfs", "latest": {"2.04--h245ed52_0": "sha256:6963c02bf8a28926bbd00e20e488d9698dd08b9fd8ae00faf85aa8ce95f4b3ef"}, "tags": {"2.04--h245ed52_0": "sha256:6963c02bf8a28926bbd00e20e488d9698dd08b9fd8ae00faf85aa8ce95f4b3ef"}, "docker": "quay.io/biocontainers/est-sfs", "aliases": {"est-sfs": "/usr/local/bin/est-sfs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/est-sfs.
singularity registry hpc automated addition for est-sfs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/est-sfs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/est-sfs:2.04--h245ed52_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/est-sfs/2.04--h245ed52_0
$ module help quay.io/biocontainers/est-sfs/2.04--h245ed52_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### est-sfs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### est-sfs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### est-sfs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### est-sfs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### est-sfs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### est-sfs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### est-sfs

```bash
$ singularity exec <container> /usr/local/bin/est-sfs
$ podman run --it --rm --entrypoint /usr/local/bin/est-sfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/est-sfs   -v ${PWD} -w ${PWD} <container> -c " $@"
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