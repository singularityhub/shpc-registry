---
layout: container
name:  "quay.io/biocontainers/bxtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bxtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bxtools/container.yaml"
updated_at: "2024-04-23 02:36:55.164224"
latest: "0.1.0--hf5e1c6e_5"
container_url: "https://biocontainers.pro/tools/bxtools"
aliases:
 - "bxtools"
versions:
 - "0.1.0--h468198e_3"
 - "0.1.0--hf5e1c6e_5"
description: "shpc-registry automated BioContainers addition for bxtools"
config: {"url": "https://biocontainers.pro/tools/bxtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bxtools", "latest": {"0.1.0--hf5e1c6e_5": "sha256:ac0f562769b0be477f8d91e488262d710021d5814831481e6ab95f197b7f9671"}, "tags": {"0.1.0--h468198e_3": "sha256:d76f399d5ef3018291ce05240dd19d4ee569d16080da5ef85149cabaf1fbeb0d", "0.1.0--hf5e1c6e_5": "sha256:ac0f562769b0be477f8d91e488262d710021d5814831481e6ab95f197b7f9671"}, "docker": "quay.io/biocontainers/bxtools", "aliases": {"bxtools": "/usr/local/bin/bxtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bxtools.
shpc-registry automated BioContainers addition for bxtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bxtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bxtools:0.1.0--hf5e1c6e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bxtools/0.1.0--hf5e1c6e_5
$ module help quay.io/biocontainers/bxtools/0.1.0--hf5e1c6e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bxtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bxtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bxtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bxtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bxtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bxtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bxtools

```bash
$ singularity exec <container> /usr/local/bin/bxtools
$ podman run --it --rm --entrypoint /usr/local/bin/bxtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bxtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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