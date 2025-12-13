---
layout: container
name:  "quay.io/biocontainers/sfs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sfs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sfs/container.yaml"
updated_at: "2025-12-13 04:04:32.591450"
latest: "0.1.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/sfs"
aliases:
 - "sfs"
versions:
 - "0.1.0--h9ee0642_0"
description: "singularity registry hpc automated addition for sfs"
config: {"url": "https://biocontainers.pro/tools/sfs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sfs", "latest": {"0.1.0--h9ee0642_0": "sha256:f3fa17e52637017c9fb399b500438b571a06d228a553ea8b6305488c92e82bca"}, "tags": {"0.1.0--h9ee0642_0": "sha256:f3fa17e52637017c9fb399b500438b571a06d228a553ea8b6305488c92e82bca"}, "docker": "quay.io/biocontainers/sfs", "aliases": {"sfs": "/usr/local/bin/sfs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sfs.
singularity registry hpc automated addition for sfs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sfs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sfs:0.1.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sfs/0.1.0--h9ee0642_0
$ module help quay.io/biocontainers/sfs/0.1.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sfs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sfs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sfs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sfs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sfs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sfs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sfs

```bash
$ singularity exec <container> /usr/local/bin/sfs
$ podman run --it --rm --entrypoint /usr/local/bin/sfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sfs   -v ${PWD} -w ${PWD} <container> -c " $@"
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