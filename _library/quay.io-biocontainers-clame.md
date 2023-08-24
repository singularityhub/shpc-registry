---
layout: container
name:  "quay.io/biocontainers/clame"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clame/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clame/container.yaml"
updated_at: "2023-08-24 02:54:40.489059"
latest: "1.0--he1b5a44_1"
container_url: "https://biocontainers.pro/tools/clame"
aliases:
 - "binning"
 - "clame"
 - "genFm9"
 - "mapping"
versions:
 - "1.0--he1b5a44_1"
description: "shpc-registry automated BioContainers addition for clame"
config: {"url": "https://biocontainers.pro/tools/clame", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clame", "latest": {"1.0--he1b5a44_1": "sha256:1bcbdfe0d6a46941f48f832083d57d046c81d47d85c35c8cd7f2edff08043c3a"}, "tags": {"1.0--he1b5a44_1": "sha256:1bcbdfe0d6a46941f48f832083d57d046c81d47d85c35c8cd7f2edff08043c3a"}, "docker": "quay.io/biocontainers/clame", "aliases": {"binning": "/usr/local/bin/binning", "clame": "/usr/local/bin/clame", "genFm9": "/usr/local/bin/genFm9", "mapping": "/usr/local/bin/mapping"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clame.
shpc-registry automated BioContainers addition for clame
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clame
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clame:1.0--he1b5a44_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clame/1.0--he1b5a44_1
$ module help quay.io/biocontainers/clame/1.0--he1b5a44_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clame-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clame-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clame-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clame-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clame-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clame-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binning

```bash
$ singularity exec <container> /usr/local/bin/binning
$ podman run --it --rm --entrypoint /usr/local/bin/binning   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binning   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clame

```bash
$ singularity exec <container> /usr/local/bin/clame
$ podman run --it --rm --entrypoint /usr/local/bin/clame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genFm9

```bash
$ singularity exec <container> /usr/local/bin/genFm9
$ podman run --it --rm --entrypoint /usr/local/bin/genFm9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genFm9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapping

```bash
$ singularity exec <container> /usr/local/bin/mapping
$ podman run --it --rm --entrypoint /usr/local/bin/mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapping   -v ${PWD} -w ${PWD} <container> -c " $@"
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