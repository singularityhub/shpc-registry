---
layout: container
name:  "quay.io/biocontainers/gerp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gerp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gerp/container.yaml"
updated_at: "2025-11-21 04:00:20.747694"
latest: "2.1--h1b792b2_2"
container_url: "https://biocontainers.pro/tools/gerp"
aliases:
 - "gerpcol"
 - "gerpelem"
versions:
 - "2.1--h1b792b2_2"
description: "shpc-registry automated BioContainers addition for gerp"
config: {"url": "https://biocontainers.pro/tools/gerp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gerp", "latest": {"2.1--h1b792b2_2": "sha256:f4db0e9f5652ae4b6796621f094b0a126a71a4d0ba7a7f702ca15cedfc81c9f1"}, "tags": {"2.1--h1b792b2_2": "sha256:f4db0e9f5652ae4b6796621f094b0a126a71a4d0ba7a7f702ca15cedfc81c9f1"}, "docker": "quay.io/biocontainers/gerp", "aliases": {"gerpcol": "/usr/local/bin/gerpcol", "gerpelem": "/usr/local/bin/gerpelem"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gerp.
shpc-registry automated BioContainers addition for gerp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gerp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gerp:2.1--h1b792b2_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gerp/2.1--h1b792b2_2
$ module help quay.io/biocontainers/gerp/2.1--h1b792b2_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gerp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gerp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gerp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gerp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gerp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gerp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gerpcol

```bash
$ singularity exec <container> /usr/local/bin/gerpcol
$ podman run --it --rm --entrypoint /usr/local/bin/gerpcol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gerpcol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gerpelem

```bash
$ singularity exec <container> /usr/local/bin/gerpelem
$ podman run --it --rm --entrypoint /usr/local/bin/gerpelem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gerpelem   -v ${PWD} -w ${PWD} <container> -c " $@"
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