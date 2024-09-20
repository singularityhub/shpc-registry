---
layout: container
name:  "quay.io/biocontainers/prodigal-gv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prodigal-gv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prodigal-gv/container.yaml"
updated_at: "2024-09-20 03:50:54.594562"
latest: "2.11.0--he4a0461_2"
container_url: "https://biocontainers.pro/tools/prodigal-gv"
aliases:
 - "prodigal-gv"
versions:
 - "2.9.0--h7132678_0"
 - "2.10.0--h7132678_0"
 - "2.11.0--h7132678_0"
 - "2.11.0--he4a0461_2"
description: "singularity registry hpc automated addition for prodigal-gv"
config: {"url": "https://biocontainers.pro/tools/prodigal-gv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for prodigal-gv", "latest": {"2.11.0--he4a0461_2": "sha256:7e6bdc37b9354dbef7f25ea66f6963ac3897415748536923bf3572c17b0155db"}, "tags": {"2.9.0--h7132678_0": "sha256:0dc5f2817890c8606a131c36ee0a68d821da45caa113d6f286702ae1bfd004c7", "2.10.0--h7132678_0": "sha256:a8455963b9aef96b7507d4e29e7bf3f93584aabee6dc74ae6425d33dc3046c1e", "2.11.0--h7132678_0": "sha256:78f582d3532af710bc6b6ab8dd7baa363f613be85df91f968e706bdd2a81e3a4", "2.11.0--he4a0461_2": "sha256:7e6bdc37b9354dbef7f25ea66f6963ac3897415748536923bf3572c17b0155db"}, "docker": "quay.io/biocontainers/prodigal-gv", "aliases": {"prodigal-gv": "/usr/local/bin/prodigal-gv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prodigal-gv.
singularity registry hpc automated addition for prodigal-gv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prodigal-gv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prodigal-gv:2.11.0--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prodigal-gv/2.11.0--he4a0461_2
$ module help quay.io/biocontainers/prodigal-gv/2.11.0--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prodigal-gv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-gv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prodigal-gv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prodigal-gv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prodigal-gv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prodigal-gv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/prodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
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