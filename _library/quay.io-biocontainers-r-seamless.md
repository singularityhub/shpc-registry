---
layout: container
name:  "quay.io/biocontainers/r-seamless"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-seamless/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-seamless/container.yaml"
updated_at: "2025-01-27 07:25:58.574159"
latest: "0.1.1--r44h3121a25_1"
container_url: "https://biocontainers.pro/tools/r-seamless"

versions:
 - "0.1.0--r41h3121a25_1"
 - "0.1.0--r42h3121a25_2"
 - "0.1.0--r43h3121a25_3"
 - "0.1.1--r43h3121a25_0"
 - "0.1.1--r44h3121a25_1"
description: "shpc-registry automated BioContainers addition for r-seamless"
config: {"url": "https://biocontainers.pro/tools/r-seamless", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-seamless", "latest": {"0.1.1--r44h3121a25_1": "sha256:5eb75b6f101dbf0c39e14a9428a44cc88c2db12de37e58611661280e3b3799ee"}, "tags": {"0.1.0--r41h3121a25_1": "sha256:3b80315470029dee11b16c3171bff233ad9825e3aa03b193aea016fdefbce1ae", "0.1.0--r42h3121a25_2": "sha256:3c108832bdd1b842f7ccdaf43018532b4c7e6f1d497f1dca37c8627d53376100", "0.1.0--r43h3121a25_3": "sha256:7870576e91c024d67381a127d611ad2f9ed120de9f2949d62dcbd2f08020d0b2", "0.1.1--r43h3121a25_0": "sha256:5b450bbe2e74ae299e5653fc00d70eaf46c8b388b2338586291249522806e667", "0.1.1--r44h3121a25_1": "sha256:5eb75b6f101dbf0c39e14a9428a44cc88c2db12de37e58611661280e3b3799ee"}, "docker": "quay.io/biocontainers/r-seamless"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-seamless.
shpc-registry automated BioContainers addition for r-seamless
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-seamless
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-seamless:0.1.1--r44h3121a25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-seamless/0.1.1--r44h3121a25_1
$ module help quay.io/biocontainers/r-seamless/0.1.1--r44h3121a25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-seamless-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-seamless-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-seamless-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-seamless-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-seamless-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-seamless-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-seamless

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