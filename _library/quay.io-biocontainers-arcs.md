---
layout: container
name:  "quay.io/biocontainers/arcs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arcs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arcs/container.yaml"
updated_at: "2024-08-03 03:10:41.500682"
latest: "1.2.6--h21ec9f0_0"
container_url: "https://biocontainers.pro/tools/arcs"
aliases:
 - "arcs"
 - "arcs-make"
 - "long-to-linked-pe"
versions:
 - "1.2.4--h7ff8a90_1"
 - "1.2.5--h7ff8a90_0"
 - "1.2.5--h21ec9f0_1"
 - "1.2.6--h21ec9f0_0"
description: "shpc-registry automated BioContainers addition for arcs"
config: {"url": "https://biocontainers.pro/tools/arcs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arcs", "latest": {"1.2.6--h21ec9f0_0": "sha256:e2c17c4413d139a315b1d64e287ecfb7bf2fabfc031e0b18eef24bc670ae1ab0"}, "tags": {"1.2.4--h7ff8a90_1": "sha256:7f7df36477d38e2d91073cf65ddc75f166a5b524c345cd21e227250b96be1f08", "1.2.5--h7ff8a90_0": "sha256:73cc6d0961c2767a5c4e76ee835fcfa729f35f2d0bbb57bec8c13e4e714ad562", "1.2.5--h21ec9f0_1": "sha256:75f18b711c44a71872f534732906aeba17730cdb0ddeb132d648caa576876559", "1.2.6--h21ec9f0_0": "sha256:e2c17c4413d139a315b1d64e287ecfb7bf2fabfc031e0b18eef24bc670ae1ab0"}, "docker": "quay.io/biocontainers/arcs", "aliases": {"arcs": "/usr/local/bin/arcs", "arcs-make": "/usr/local/bin/arcs-make", "long-to-linked-pe": "/usr/local/bin/long-to-linked-pe"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arcs.
shpc-registry automated BioContainers addition for arcs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arcs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arcs:1.2.6--h21ec9f0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arcs/1.2.6--h21ec9f0_0
$ module help quay.io/biocontainers/arcs/1.2.6--h21ec9f0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arcs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arcs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arcs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arcs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arcs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arcs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arcs

```bash
$ singularity exec <container> /usr/local/bin/arcs
$ podman run --it --rm --entrypoint /usr/local/bin/arcs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arcs-make

```bash
$ singularity exec <container> /usr/local/bin/arcs-make
$ podman run --it --rm --entrypoint /usr/local/bin/arcs-make   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcs-make   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### long-to-linked-pe

```bash
$ singularity exec <container> /usr/local/bin/long-to-linked-pe
$ podman run --it --rm --entrypoint /usr/local/bin/long-to-linked-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/long-to-linked-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
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