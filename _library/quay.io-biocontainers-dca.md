---
layout: container
name:  "quay.io/biocontainers/dca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dca/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dca/container.yaml"
updated_at: "2022-10-27 00:46:54.486685"
latest: "0.3.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dca"
aliases:
 - "dca"
 - "dunamai"
 - "hyperopt-mongo-worker"
versions:
 - "0.3.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dca"
config: {"url": "https://biocontainers.pro/tools/dca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dca", "latest": {"0.3.4--pyhdfd78af_0": "sha256:5d2aef32017ba7fbc576b42aa527a4d8c36956aef442803af50444d521a234db"}, "tags": {"0.3.4--pyhdfd78af_0": "sha256:5d2aef32017ba7fbc576b42aa527a4d8c36956aef442803af50444d521a234db"}, "docker": "quay.io/biocontainers/dca", "aliases": {"dca": "/usr/local/bin/dca", "dunamai": "/usr/local/bin/dunamai", "hyperopt-mongo-worker": "/usr/local/bin/hyperopt-mongo-worker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dca.
shpc-registry automated BioContainers addition for dca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dca:0.3.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dca/0.3.4--pyhdfd78af_0
$ module help quay.io/biocontainers/dca/0.3.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dca

```bash
$ singularity exec <container> /usr/local/bin/dca
$ podman run --it --rm --entrypoint /usr/local/bin/dca   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dca   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hyperopt-mongo-worker

```bash
$ singularity exec <container> /usr/local/bin/hyperopt-mongo-worker
$ podman run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hyperopt-mongo-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
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