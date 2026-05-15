---
layout: container
name:  "quay.io/biocontainers/hapfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hapfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hapfold/container.yaml"
updated_at: "2026-05-15 06:09:31.966762"
latest: "0.1.0--h5814d7d_0"
container_url: "https://biocontainers.pro/tools/hapfold"
aliases:
 - "HapFold"
 - "hapfold"
versions:
 - "0.1.0--h5814d7d_0"
description: "singularity registry hpc automated addition for hapfold"
config: {"url": "https://biocontainers.pro/tools/hapfold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hapfold", "latest": {"0.1.0--h5814d7d_0": "sha256:a4e30c0adfd9ab95db982baba1ef78b75452f9b2678125061de9c18c9caa70e0"}, "tags": {"0.1.0--h5814d7d_0": "sha256:a4e30c0adfd9ab95db982baba1ef78b75452f9b2678125061de9c18c9caa70e0"}, "docker": "quay.io/biocontainers/hapfold", "aliases": {"HapFold": "/usr/local/bin/HapFold", "hapfold": "/usr/local/bin/hapfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hapfold.
singularity registry hpc automated addition for hapfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hapfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hapfold:0.1.0--h5814d7d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hapfold/0.1.0--h5814d7d_0
$ module help quay.io/biocontainers/hapfold/0.1.0--h5814d7d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hapfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hapfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hapfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hapfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hapfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hapfold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HapFold

```bash
$ singularity exec <container> /usr/local/bin/HapFold
$ podman run --it --rm --entrypoint /usr/local/bin/HapFold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HapFold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapfold

```bash
$ singularity exec <container> /usr/local/bin/hapfold
$ podman run --it --rm --entrypoint /usr/local/bin/hapfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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