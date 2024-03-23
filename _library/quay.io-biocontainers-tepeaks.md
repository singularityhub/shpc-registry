---
layout: container
name:  "quay.io/biocontainers/tepeaks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tepeaks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tepeaks/container.yaml"
updated_at: "2024-03-23 02:50:04.688135"
latest: "0.1--ha503a2d_5"
container_url: "https://biocontainers.pro/tools/tepeaks"
aliases:
 - "TEpeaks"
versions:
 - "0.1--h87262cc_3"
 - "0.1--ha503a2d_5"
description: "shpc-registry automated BioContainers addition for tepeaks"
config: {"url": "https://biocontainers.pro/tools/tepeaks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tepeaks", "latest": {"0.1--ha503a2d_5": "sha256:3b112a99935912bb03a4800cf4b58789544d133be963f5a515fd3b52063b8c8b"}, "tags": {"0.1--h87262cc_3": "sha256:fccac70deea34946f3ee5bbf089e575d551c011a3194b703125a4d0aed872eb4", "0.1--ha503a2d_5": "sha256:3b112a99935912bb03a4800cf4b58789544d133be963f5a515fd3b52063b8c8b"}, "docker": "quay.io/biocontainers/tepeaks", "aliases": {"TEpeaks": "/usr/local/bin/TEpeaks"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tepeaks.
shpc-registry automated BioContainers addition for tepeaks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tepeaks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tepeaks:0.1--ha503a2d_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tepeaks/0.1--ha503a2d_5
$ module help quay.io/biocontainers/tepeaks/0.1--ha503a2d_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tepeaks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tepeaks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tepeaks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tepeaks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tepeaks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tepeaks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TEpeaks

```bash
$ singularity exec <container> /usr/local/bin/TEpeaks
$ podman run --it --rm --entrypoint /usr/local/bin/TEpeaks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TEpeaks   -v ${PWD} -w ${PWD} <container> -c " $@"
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