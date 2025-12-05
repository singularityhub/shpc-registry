---
layout: container
name:  "quay.io/biocontainers/r-base"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-base/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-base/container.yaml"
updated_at: "2025-12-05 03:28:18.830572"
latest: "4.4.1"
container_url: "https://biocontainers.pro/tools/r-base"

versions:
 - "4.2.1"
 - "4.4.1"
 - "4.3.1"
description: "shpc-registry automated BioContainers addition for r-base"
config: {"url": "https://biocontainers.pro/tools/r-base", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-base", "latest": {"4.4.1": "sha256:75ab52c56a3eb71b4dcab333b6c93614f805750f39d367854c710869f8694ba8"}, "tags": {"4.2.1": "sha256:6721ee8bfba2b2d326c709dc8096555304746e2cb706c28af69fbc7ea5bb3d79", "4.4.1": "sha256:75ab52c56a3eb71b4dcab333b6c93614f805750f39d367854c710869f8694ba8", "4.3.1": "sha256:af473d54a13752a376d79dca5534dc50968a217e9709368526d4b1d63c7a7443"}, "docker": "quay.io/biocontainers/r-base"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-base.
shpc-registry automated BioContainers addition for r-base
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-base
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-base:4.4.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-base/4.4.1
$ module help quay.io/biocontainers/r-base/4.4.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-base-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-base-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-base-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-base-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-base-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-base-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-base

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