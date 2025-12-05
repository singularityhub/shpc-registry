---
layout: container
name:  "quay.io/biocontainers/reseek"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reseek/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reseek/container.yaml"
updated_at: "2025-12-05 03:36:47.454175"
latest: "2.6.1--h503566f_0"
container_url: "https://biocontainers.pro/tools/reseek"
aliases:
 - "reseek"
versions:
 - "2.0.1--hdbdd923_0"
 - "2.02--hdbdd923_0"
 - "2.3--h503566f_0"
 - "2.4--h503566f_0"
 - "2.5--h503566f_0"
 - "2.6.1--h503566f_0"
description: "singularity registry hpc automated addition for reseek"
config: {"url": "https://biocontainers.pro/tools/reseek", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reseek", "latest": {"2.6.1--h503566f_0": "sha256:24f7c37150dd2c2f2f322b1387a08d2d1a4a279f46f98f1051f1745417675752"}, "tags": {"2.0.1--hdbdd923_0": "sha256:e5c1a4aa7d0111dc5447fbd1aab901ccf85d869954be922c6fe121d1f40f651e", "2.02--hdbdd923_0": "sha256:69f027e649a341c4e3e69d6c792639d2049d250170de5b4d5936ae7bf4f08f8b", "2.3--h503566f_0": "sha256:c492c4ed79b242595bdfc09f376214010956e5c4af42633cb941b3c07612cdfb", "2.4--h503566f_0": "sha256:fe83355b376878d7ba38cae355cbf51cbd1b8b419d3af5cbd8da75b5b2d9fa4b", "2.5--h503566f_0": "sha256:f0a4ab43e7ed8c096b10b2c19f4d83d6e4068269454e24f8065cde27e56e1c6f", "2.6.1--h503566f_0": "sha256:24f7c37150dd2c2f2f322b1387a08d2d1a4a279f46f98f1051f1745417675752"}, "docker": "quay.io/biocontainers/reseek", "aliases": {"reseek": "/usr/local/bin/reseek"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reseek.
singularity registry hpc automated addition for reseek
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reseek
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reseek:2.6.1--h503566f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reseek/2.6.1--h503566f_0
$ module help quay.io/biocontainers/reseek/2.6.1--h503566f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reseek-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reseek-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reseek-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reseek-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reseek-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reseek-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### reseek

```bash
$ singularity exec <container> /usr/local/bin/reseek
$ podman run --it --rm --entrypoint /usr/local/bin/reseek   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reseek   -v ${PWD} -w ${PWD} <container> -c " $@"
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