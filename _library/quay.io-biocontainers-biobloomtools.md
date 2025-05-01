---
layout: container
name:  "quay.io/biocontainers/biobloomtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobloomtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobloomtools/container.yaml"
updated_at: "2025-05-01 03:51:21.629723"
latest: "2.3.5--h077b44d_6"
container_url: "https://biocontainers.pro/tools/biobloomtools"
aliases:
 - "biobloomcategorizer"
 - "biobloommaker"
 - "biobloommicategorizer"
 - "biobloommimaker"
versions:
 - "2.3.5--hb7da652_0"
 - "2.3.5--h4056dc3_2"
 - "2.3.5--hdcf5f25_5"
 - "2.3.5--h077b44d_6"
description: "singularity registry hpc automated addition for biobloomtools"
config: {"url": "https://biocontainers.pro/tools/biobloomtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobloomtools", "latest": {"2.3.5--h077b44d_6": "sha256:83962f123b2d3d413b411bfb65326629d9a99007579b2de1e337ebc610d16562"}, "tags": {"2.3.5--hb7da652_0": "sha256:3eb5c822c7ea2d65c8b60b571580858a3187e20d2a8c3f53cd065f7db48e8957", "2.3.5--h4056dc3_2": "sha256:bcbb6d0fb08621ad3a79c05343e1a43e483bd5036a02c5df35b3692c1a6bed52", "2.3.5--hdcf5f25_5": "sha256:2bf489ef793df4b27c30ba99e8c6073fad512f87c9e3cee27797e81d911dca3d", "2.3.5--h077b44d_6": "sha256:83962f123b2d3d413b411bfb65326629d9a99007579b2de1e337ebc610d16562"}, "docker": "quay.io/biocontainers/biobloomtools", "aliases": {"biobloomcategorizer": "/usr/local/bin/biobloomcategorizer", "biobloommaker": "/usr/local/bin/biobloommaker", "biobloommicategorizer": "/usr/local/bin/biobloommicategorizer", "biobloommimaker": "/usr/local/bin/biobloommimaker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobloomtools.
singularity registry hpc automated addition for biobloomtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobloomtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobloomtools:2.3.5--h077b44d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobloomtools/2.3.5--h077b44d_6
$ module help quay.io/biocontainers/biobloomtools/2.3.5--h077b44d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobloomtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobloomtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobloomtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobloomtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobloomtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobloomtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biobloomcategorizer

```bash
$ singularity exec <container> /usr/local/bin/biobloomcategorizer
$ podman run --it --rm --entrypoint /usr/local/bin/biobloomcategorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biobloomcategorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biobloommaker

```bash
$ singularity exec <container> /usr/local/bin/biobloommaker
$ podman run --it --rm --entrypoint /usr/local/bin/biobloommaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biobloommaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biobloommicategorizer

```bash
$ singularity exec <container> /usr/local/bin/biobloommicategorizer
$ podman run --it --rm --entrypoint /usr/local/bin/biobloommicategorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biobloommicategorizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biobloommimaker

```bash
$ singularity exec <container> /usr/local/bin/biobloommimaker
$ podman run --it --rm --entrypoint /usr/local/bin/biobloommimaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biobloommimaker   -v ${PWD} -w ${PWD} <container> -c " $@"
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