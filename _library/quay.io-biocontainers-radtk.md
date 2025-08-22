---
layout: container
name:  "quay.io/biocontainers/radtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/radtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/radtk/container.yaml"
updated_at: "2025-08-22 03:41:22.910720"
latest: "0.2.0--ha6fb395_1"
container_url: "https://biocontainers.pro/tools/radtk"
aliases:
 - "radtk"
versions:
 - "0.2.0--h919a2d8_0"
 - "0.2.0--ha6fb395_1"
description: "singularity registry hpc automated addition for radtk"
config: {"url": "https://biocontainers.pro/tools/radtk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for radtk", "latest": {"0.2.0--ha6fb395_1": "sha256:1942e79803789d32313723339fd063c220627a181b65adaac5a604660f4574a6"}, "tags": {"0.2.0--h919a2d8_0": "sha256:60862e78c43b8b9e353ac675974cbe88d5aaf131f2ce914af1d35f1efc91b5e4", "0.2.0--ha6fb395_1": "sha256:1942e79803789d32313723339fd063c220627a181b65adaac5a604660f4574a6"}, "docker": "quay.io/biocontainers/radtk", "aliases": {"radtk": "/usr/local/bin/radtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/radtk.
singularity registry hpc automated addition for radtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/radtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/radtk:0.2.0--ha6fb395_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/radtk/0.2.0--ha6fb395_1
$ module help quay.io/biocontainers/radtk/0.2.0--ha6fb395_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### radtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### radtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### radtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### radtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### radtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### radtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### radtk

```bash
$ singularity exec <container> /usr/local/bin/radtk
$ podman run --it --rm --entrypoint /usr/local/bin/radtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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