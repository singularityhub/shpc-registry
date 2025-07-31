---
layout: container
name:  "quay.io/biocontainers/r-seqmagick"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-seqmagick/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-seqmagick/container.yaml"
updated_at: "2025-07-31 11:23:06.441138"
latest: "0.1.7--r44h3121a25_1"
container_url: "https://biocontainers.pro/tools/r-seqmagick"

versions:
 - "0.1.5--r41h3121a25_0"
 - "0.1.5--r42h3121a25_1"
 - "0.1.6--r43h3121a25_1"
 - "0.1.7--r43h3121a25_0"
 - "0.1.7--r44h3121a25_1"
description: "shpc-registry automated BioContainers addition for r-seqmagick"
config: {"url": "https://biocontainers.pro/tools/r-seqmagick", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-seqmagick", "latest": {"0.1.7--r44h3121a25_1": "sha256:7d1a1e1de5941cd07152ac995360bc6752f4bc68834dfde73b0dfbdcb4f04434"}, "tags": {"0.1.5--r41h3121a25_0": "sha256:2e4cb2e0a3b297764d50646e15e35971330fb7b9a403e4c9b5854faa3a6aa1f7", "0.1.5--r42h3121a25_1": "sha256:bf796d4ffb9cad584b8f940f660d9b95fa792e0e8ffe34c758bf8b4733f040e0", "0.1.6--r43h3121a25_1": "sha256:f2a352b8ea3c80596c7dc975df0d546e15359e789373aff2293fe94c57ed2c8f", "0.1.7--r43h3121a25_0": "sha256:7416ab59210ff7b8476ef50f0ef6ad42a46fa7fae816f1ba2933b06a18f6b23d", "0.1.7--r44h3121a25_1": "sha256:7d1a1e1de5941cd07152ac995360bc6752f4bc68834dfde73b0dfbdcb4f04434"}, "docker": "quay.io/biocontainers/r-seqmagick"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-seqmagick.
shpc-registry automated BioContainers addition for r-seqmagick
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-seqmagick
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-seqmagick:0.1.7--r44h3121a25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-seqmagick/0.1.7--r44h3121a25_1
$ module help quay.io/biocontainers/r-seqmagick/0.1.7--r44h3121a25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-seqmagick-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-seqmagick-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-seqmagick-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-seqmagick-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-seqmagick-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-seqmagick-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-seqmagick

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