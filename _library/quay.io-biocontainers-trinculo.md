---
layout: container
name:  "quay.io/biocontainers/trinculo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trinculo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trinculo/container.yaml"
updated_at: "2023-07-05 03:27:11.470371"
latest: "0.96--h2b92225_7"
container_url: "https://biocontainers.pro/tools/trinculo"
aliases:
 - "trinculo"
versions:
 - "0.96--h2b92225_6"
 - "0.96--h2b92225_7"
description: "shpc-registry automated BioContainers addition for trinculo"
config: {"url": "https://biocontainers.pro/tools/trinculo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trinculo", "latest": {"0.96--h2b92225_7": "sha256:e1f48735941ddb1501e5e0e4ef6e940a924f38a2d83a4b1b34738806e792ab32"}, "tags": {"0.96--h2b92225_6": "sha256:eb8160f618b752e153ada51f1900255493a994fe5d71d26810f4883e2444ac9a", "0.96--h2b92225_7": "sha256:e1f48735941ddb1501e5e0e4ef6e940a924f38a2d83a4b1b34738806e792ab32"}, "docker": "quay.io/biocontainers/trinculo", "aliases": {"trinculo": "/usr/local/bin/trinculo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trinculo.
shpc-registry automated BioContainers addition for trinculo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trinculo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trinculo:0.96--h2b92225_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trinculo/0.96--h2b92225_7
$ module help quay.io/biocontainers/trinculo/0.96--h2b92225_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trinculo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trinculo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trinculo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trinculo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trinculo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trinculo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trinculo

```bash
$ singularity exec <container> /usr/local/bin/trinculo
$ podman run --it --rm --entrypoint /usr/local/bin/trinculo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trinculo   -v ${PWD} -w ${PWD} <container> -c " $@"
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