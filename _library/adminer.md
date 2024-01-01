---
layout: container
name:  "adminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/adminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/adminer/container.yaml"
updated_at: "2024-01-01 02:33:32.267551"
latest: "4.8.1"
container_url: "https://hub.docker.com/_/adminer"

versions:
 - "4.8.0-fastcgi"
 - "4.8.1"
 - "4.8.1-fastcgi"
 - "latest"
 - "4"
description: "Database management in a single PHP file."
config: {"docker": "adminer", "url": "https://hub.docker.com/_/adminer", "maintainer": "@vsoch", "description": "Database management in a single PHP file.", "latest": {"4.8.1": "sha256:0ce7583815dabdd9f560ee0afed630ecb33df6756f4b66c85c197011559a0248"}, "tags": {"4.8.0-fastcgi": "sha256:5368f087fed03f49e9de8731ee3d9998d7e78391720d500309b5bcde2a401058", "4.8.1": "sha256:0ce7583815dabdd9f560ee0afed630ecb33df6756f4b66c85c197011559a0248", "4.8.1-fastcgi": "sha256:daa291dff0f15be3ba5d0a8cfdcf137d8dd0b1f9304d132c686a4e95dcd489dd", "latest": "sha256:0ce7583815dabdd9f560ee0afed630ecb33df6756f4b66c85c197011559a0248", "4": "sha256:0ce7583815dabdd9f560ee0afed630ecb33df6756f4b66c85c197011559a0248"}}
---

This module is a singularity container wrapper for adminer.
Database management in a single PHP file.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install adminer
```

Or a specific version:

```bash
$ shpc install adminer:4.8.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load adminer/4.8.1
$ module help adminer/4.8.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### adminer

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