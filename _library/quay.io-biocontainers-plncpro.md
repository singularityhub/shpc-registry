---
layout: container
name:  "quay.io/biocontainers/plncpro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plncpro/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plncpro/container.yaml"
updated_at: "2022-10-27 01:07:16.194358"
latest: "1.2.2--py37h96cfd12_3"
container_url: "https://biocontainers.pro/tools/plncpro"
aliases:
 - "plncpro"
 - "plncpro_format_ff.sh"
versions:
 - "1.2.2--py37h96cfd12_3"
description: "shpc-registry automated BioContainers addition for plncpro"
config: {"url": "https://biocontainers.pro/tools/plncpro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plncpro", "latest": {"1.2.2--py37h96cfd12_3": "sha256:acc9acd73f65eb7343634cfb4e776e9e4a9ea8485df4c16eaeb1fc9a56c6bc6c"}, "tags": {"1.2.2--py37h96cfd12_3": "sha256:acc9acd73f65eb7343634cfb4e776e9e4a9ea8485df4c16eaeb1fc9a56c6bc6c"}, "docker": "quay.io/biocontainers/plncpro", "aliases": {"plncpro": "/usr/local/bin/plncpro", "plncpro_format_ff.sh": "/usr/local/bin/plncpro_format_ff.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plncpro.
shpc-registry automated BioContainers addition for plncpro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plncpro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plncpro:1.2.2--py37h96cfd12_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plncpro/1.2.2--py37h96cfd12_3
$ module help quay.io/biocontainers/plncpro/1.2.2--py37h96cfd12_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plncpro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plncpro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plncpro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plncpro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plncpro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plncpro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plncpro

```bash
$ singularity exec <container> /usr/local/bin/plncpro
$ podman run --it --rm --entrypoint /usr/local/bin/plncpro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plncpro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plncpro_format_ff.sh

```bash
$ singularity exec <container> /usr/local/bin/plncpro_format_ff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/plncpro_format_ff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plncpro_format_ff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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