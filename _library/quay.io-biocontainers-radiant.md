---
layout: container
name:  "quay.io/biocontainers/radiant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/radiant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/radiant/container.yaml"
updated_at: "2025-01-12 03:49:35.386459"
latest: "1.1.5--h2a31222_0"
container_url: "https://biocontainers.pro/tools/radiant"
aliases:
 - "makeRadiantDB"
 - "radiant"
versions:
 - "1.1.5--h2a31222_0"
description: "singularity registry hpc automated addition for radiant"
config: {"url": "https://biocontainers.pro/tools/radiant", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for radiant", "latest": {"1.1.5--h2a31222_0": "sha256:d94ae5d9381b3f5621fbba37919f64e8f774958a7eccc56d2d4a437d8cd7f8b4"}, "tags": {"1.1.5--h2a31222_0": "sha256:d94ae5d9381b3f5621fbba37919f64e8f774958a7eccc56d2d4a437d8cd7f8b4"}, "docker": "quay.io/biocontainers/radiant", "aliases": {"makeRadiantDB": "/usr/local/bin/makeRadiantDB", "radiant": "/usr/local/bin/radiant"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/radiant.
singularity registry hpc automated addition for radiant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/radiant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/radiant:1.1.5--h2a31222_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/radiant/1.1.5--h2a31222_0
$ module help quay.io/biocontainers/radiant/1.1.5--h2a31222_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### radiant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### radiant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### radiant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### radiant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### radiant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### radiant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### makeRadiantDB

```bash
$ singularity exec <container> /usr/local/bin/makeRadiantDB
$ podman run --it --rm --entrypoint /usr/local/bin/makeRadiantDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeRadiantDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### radiant

```bash
$ singularity exec <container> /usr/local/bin/radiant
$ podman run --it --rm --entrypoint /usr/local/bin/radiant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/radiant   -v ${PWD} -w ${PWD} <container> -c " $@"
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