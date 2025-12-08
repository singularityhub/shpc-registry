---
layout: container
name:  "quay.io/biocontainers/survivor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/survivor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/survivor/container.yaml"
updated_at: "2025-12-08 04:06:34.915519"
latest: "1.0.7--h077b44d_7"
container_url: "https://biocontainers.pro/tools/survivor"
aliases:
 - "SURVIVOR"
versions:
 - "1.0.7--hd03093a_2"
 - "1.0.7--hdcf5f25_4"
 - "1.0.7--hdcf5f25_5"
 - "1.0.7--h077b44d_6"
 - "1.0.7--h077b44d_7"
description: "shpc-registry automated BioContainers addition for survivor"
config: {"url": "https://biocontainers.pro/tools/survivor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for survivor", "latest": {"1.0.7--h077b44d_7": "sha256:76e60eb826113b26e15ec62db42358bdeb88d718f74c5c3dd01c186c8c9a8497"}, "tags": {"1.0.7--hd03093a_2": "sha256:3ffd3f36743cb173a0938e5b13622508e4a358c039a4560bc4526e381e2c72b8", "1.0.7--hdcf5f25_4": "sha256:5fc77af8408d251df2c53de2aa471a8cb0bb2c641bb76ee2dad588dd687068c0", "1.0.7--hdcf5f25_5": "sha256:bd407315f2b3bec09782c1b9fbea906f49e7366a839a8a776b55ecd76dd19fc6", "1.0.7--h077b44d_6": "sha256:0075ff6e8a26e4d97177f641b21bd563ef86476c284c9df0d62b560e30d27ac6", "1.0.7--h077b44d_7": "sha256:76e60eb826113b26e15ec62db42358bdeb88d718f74c5c3dd01c186c8c9a8497"}, "docker": "quay.io/biocontainers/survivor", "aliases": {"SURVIVOR": "/usr/local/bin/SURVIVOR"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/survivor.
shpc-registry automated BioContainers addition for survivor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/survivor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/survivor:1.0.7--h077b44d_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/survivor/1.0.7--h077b44d_7
$ module help quay.io/biocontainers/survivor/1.0.7--h077b44d_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### survivor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### survivor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### survivor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### survivor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### survivor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### survivor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SURVIVOR

```bash
$ singularity exec <container> /usr/local/bin/SURVIVOR
$ podman run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SURVIVOR   -v ${PWD} -w ${PWD} <container> -c " $@"
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