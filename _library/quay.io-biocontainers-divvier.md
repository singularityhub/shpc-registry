---
layout: container
name:  "quay.io/biocontainers/divvier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/divvier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/divvier/container.yaml"
updated_at: "2024-07-29 03:23:25.160461"
latest: "1.01--h5b5514e_3"
container_url: "https://biocontainers.pro/tools/divvier"
aliases:
 - "divvier"
versions:
 - "1.01--h5b5514e_2"
 - "1.01--h5b5514e_3"
description: "shpc-registry automated BioContainers addition for divvier"
config: {"url": "https://biocontainers.pro/tools/divvier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for divvier", "latest": {"1.01--h5b5514e_3": "sha256:996ecdf6416677fe77736aae9b4a48d3247758607ce03174f9a02d6fa45508cc"}, "tags": {"1.01--h5b5514e_2": "sha256:b3484d47d0b889140177b6d3358d43fd9ede5273a69c0468932be30df64e0082", "1.01--h5b5514e_3": "sha256:996ecdf6416677fe77736aae9b4a48d3247758607ce03174f9a02d6fa45508cc"}, "docker": "quay.io/biocontainers/divvier", "aliases": {"divvier": "/usr/local/bin/divvier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/divvier.
shpc-registry automated BioContainers addition for divvier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/divvier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/divvier:1.01--h5b5514e_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/divvier/1.01--h5b5514e_3
$ module help quay.io/biocontainers/divvier/1.01--h5b5514e_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### divvier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### divvier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### divvier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### divvier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### divvier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### divvier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### divvier

```bash
$ singularity exec <container> /usr/local/bin/divvier
$ podman run --it --rm --entrypoint /usr/local/bin/divvier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/divvier   -v ${PWD} -w ${PWD} <container> -c " $@"
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