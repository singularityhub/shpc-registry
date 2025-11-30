---
layout: container
name:  "quay.io/biocontainers/r-rtfbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rtfbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rtfbs/container.yaml"
updated_at: "2025-11-30 04:33:17.215798"
latest: "0.3.15--r42h56115f1_7"
container_url: "https://biocontainers.pro/tools/r-rtfbs"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "0.3.9--r36hcdcec82_3"
 - "0.3.15--r42h73dbb54_6"
 - "0.3.15--r42h56115f1_7"
description: "shpc-registry automated BioContainers addition for r-rtfbs"
config: {"url": "https://biocontainers.pro/tools/r-rtfbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rtfbs", "latest": {"0.3.15--r42h56115f1_7": "sha256:7073362f88cab5f9deed1faac45dce44148e1eee969188e712cf4caf0ddd5efa"}, "tags": {"0.3.9--r36hcdcec82_3": "sha256:a0016bff01e45416d44e637edc3a5acf475459cc8ca17ed17a42897f0ee41fce", "0.3.15--r42h73dbb54_6": "sha256:7e51e9020f2249bbc2a58f7ae9028fe616afcaf0f08c0dd2e24aa10fd071abc9", "0.3.15--r42h56115f1_7": "sha256:7073362f88cab5f9deed1faac45dce44148e1eee969188e712cf4caf0ddd5efa"}, "docker": "quay.io/biocontainers/r-rtfbs", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rtfbs.
shpc-registry automated BioContainers addition for r-rtfbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rtfbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rtfbs:0.3.15--r42h56115f1_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rtfbs/0.3.15--r42h56115f1_7
$ module help quay.io/biocontainers/r-rtfbs/0.3.15--r42h56115f1_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rtfbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rtfbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rtfbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rtfbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rtfbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rtfbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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