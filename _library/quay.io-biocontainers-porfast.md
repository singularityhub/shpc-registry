---
layout: container
name:  "quay.io/biocontainers/porfast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/porfast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/porfast/container.yaml"
updated_at: "2025-11-08 03:13:55.246382"
latest: "0.8.0--hed695b0_1"
container_url: "https://biocontainers.pro/tools/porfast"
aliases:
 - "porfast"
versions:
 - "0.8.0--hed695b0_1"
description: "shpc-registry automated BioContainers addition for porfast"
config: {"url": "https://biocontainers.pro/tools/porfast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for porfast", "latest": {"0.8.0--hed695b0_1": "sha256:ce3353011864f153d8ecc15864b0b7b8f9565020864284a2d637a703ada16f4f"}, "tags": {"0.8.0--hed695b0_1": "sha256:ce3353011864f153d8ecc15864b0b7b8f9565020864284a2d637a703ada16f4f"}, "docker": "quay.io/biocontainers/porfast", "aliases": {"porfast": "/usr/local/bin/porfast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/porfast.
shpc-registry automated BioContainers addition for porfast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/porfast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/porfast:0.8.0--hed695b0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/porfast/0.8.0--hed695b0_1
$ module help quay.io/biocontainers/porfast/0.8.0--hed695b0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### porfast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### porfast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### porfast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### porfast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### porfast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### porfast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### porfast

```bash
$ singularity exec <container> /usr/local/bin/porfast
$ podman run --it --rm --entrypoint /usr/local/bin/porfast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/porfast   -v ${PWD} -w ${PWD} <container> -c " $@"
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