---
layout: container
name:  "quay.io/biocontainers/music"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/music/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/music/container.yaml"
updated_at: "2023-10-19 02:41:42.451323"
latest: "1.0.0--h2d50403_2"
container_url: "https://biocontainers.pro/tools/music"

versions:
 - "1.0.0--h2d50403_2"
description: "shpc-registry automated BioContainers addition for music"
config: {"url": "https://biocontainers.pro/tools/music", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for music", "latest": {"1.0.0--h2d50403_2": "sha256:2d027510d85133a2c36cf0a244e5fa6e8fe1ac610c789a24e032bdae6ba22560"}, "tags": {"1.0.0--h2d50403_2": "sha256:2d027510d85133a2c36cf0a244e5fa6e8fe1ac610c789a24e032bdae6ba22560"}, "docker": "quay.io/biocontainers/music"}
---

This module is a singularity container wrapper for quay.io/biocontainers/music.
shpc-registry automated BioContainers addition for music
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/music
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/music:1.0.0--h2d50403_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/music/1.0.0--h2d50403_2
$ module help quay.io/biocontainers/music/1.0.0--h2d50403_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### music-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### music-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### music-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### music-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### music-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### music-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### music

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