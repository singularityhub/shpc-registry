---
layout: container
name:  "quay.io/biocontainers/spydrpick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spydrpick/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spydrpick/container.yaml"
updated_at: "2024-12-05 03:10:43.571955"
latest: "1.2.0--h78a066a_0"
container_url: "https://biocontainers.pro/tools/spydrpick"
aliases:
 - "SpydrPick"
versions:
 - "1.2.0--h78a066a_0"
description: "shpc-registry automated BioContainers addition for spydrpick"
config: {"url": "https://biocontainers.pro/tools/spydrpick", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spydrpick", "latest": {"1.2.0--h78a066a_0": "sha256:40cff2b3eb29468368902ec79e028ad06e7c69dab6aad405b6ae42931633cecd"}, "tags": {"1.2.0--h78a066a_0": "sha256:40cff2b3eb29468368902ec79e028ad06e7c69dab6aad405b6ae42931633cecd"}, "docker": "quay.io/biocontainers/spydrpick", "aliases": {"SpydrPick": "/usr/local/bin/SpydrPick"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spydrpick.
shpc-registry automated BioContainers addition for spydrpick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spydrpick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spydrpick:1.2.0--h78a066a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spydrpick/1.2.0--h78a066a_0
$ module help quay.io/biocontainers/spydrpick/1.2.0--h78a066a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spydrpick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spydrpick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spydrpick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spydrpick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spydrpick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spydrpick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SpydrPick

```bash
$ singularity exec <container> /usr/local/bin/SpydrPick
$ podman run --it --rm --entrypoint /usr/local/bin/SpydrPick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SpydrPick   -v ${PWD} -w ${PWD} <container> -c " $@"
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