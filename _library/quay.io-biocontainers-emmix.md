---
layout: container
name:  "quay.io/biocontainers/emmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/emmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/emmix/container.yaml"
updated_at: "2023-08-03 02:51:28.004633"
latest: "1.3--he991be0_4"
container_url: "https://biocontainers.pro/tools/emmix"
aliases:
 - "EMMIX"
versions:
 - "1.3--he991be0_4"
description: "shpc-registry automated BioContainers addition for emmix"
config: {"url": "https://biocontainers.pro/tools/emmix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for emmix", "latest": {"1.3--he991be0_4": "sha256:99ae966276f246c47e5323b54af95577572a662efff6ee912356c0e83a7e5293"}, "tags": {"1.3--he991be0_4": "sha256:99ae966276f246c47e5323b54af95577572a662efff6ee912356c0e83a7e5293"}, "docker": "quay.io/biocontainers/emmix", "aliases": {"EMMIX": "/usr/local/bin/EMMIX"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/emmix.
shpc-registry automated BioContainers addition for emmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/emmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/emmix:1.3--he991be0_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/emmix/1.3--he991be0_4
$ module help quay.io/biocontainers/emmix/1.3--he991be0_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EMMIX

```bash
$ singularity exec <container> /usr/local/bin/EMMIX
$ podman run --it --rm --entrypoint /usr/local/bin/EMMIX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EMMIX   -v ${PWD} -w ${PWD} <container> -c " $@"
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