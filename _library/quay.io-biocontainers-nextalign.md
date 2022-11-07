---
layout: container
name:  "quay.io/biocontainers/nextalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nextalign/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nextalign/container.yaml"
updated_at: "2022-11-06 23:59:58.354261"
latest: "2.8.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/nextalign"
aliases:
 - "nextalign"
versions:
 - "2.7.0--h9ee0642_0"
 - "2.8.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for nextalign"
config: {"url": "https://biocontainers.pro/tools/nextalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nextalign", "latest": {"2.8.0--h9ee0642_0": "sha256:1e1f96e33a05809cae185848a27fcc8f0691c32c34973eefa90af331df5d2ebd"}, "tags": {"2.7.0--h9ee0642_0": "sha256:d7d53b9e97bf7b17d8c3d2e6b6ec964a992be6d00dc54ff67614f0d1fe9b7c4e", "2.8.0--h9ee0642_0": "sha256:1e1f96e33a05809cae185848a27fcc8f0691c32c34973eefa90af331df5d2ebd"}, "docker": "quay.io/biocontainers/nextalign", "aliases": {"nextalign": "/usr/local/bin/nextalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nextalign.
shpc-registry automated BioContainers addition for nextalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nextalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nextalign:2.8.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nextalign/2.8.0--h9ee0642_0
$ module help quay.io/biocontainers/nextalign/2.8.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nextalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nextalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nextalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nextalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nextalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nextalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nextalign

```bash
$ singularity exec <container> /usr/local/bin/nextalign
$ podman run --it --rm --entrypoint /usr/local/bin/nextalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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