---
layout: container
name:  "quay.io/biocontainers/ecoprimers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ecoprimers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ecoprimers/container.yaml"
updated_at: "2026-01-14 04:03:36.209655"
latest: "1.0--h577a1d6_8"
container_url: "https://biocontainers.pro/tools/ecoprimers"
aliases:
 - "ecoPrimers"
versions:
 - "1.0--h7132678_5"
 - "1.0--he4a0461_7"
 - "1.0--h577a1d6_8"
description: "shpc-registry automated BioContainers addition for ecoprimers"
config: {"url": "https://biocontainers.pro/tools/ecoprimers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ecoprimers", "latest": {"1.0--h577a1d6_8": "sha256:96c7a7fb99587b27e7ade742d087707181e75c07d6704f9f2c0a05ea62d93e54"}, "tags": {"1.0--h7132678_5": "sha256:7c28d6e30b6303f9796697b511a4356cfe02ac319cc208bd467a0398060de06e", "1.0--he4a0461_7": "sha256:1c286ee950420b8c573ebd2837145ec71c90a393eff58af25e8928020446bb66", "1.0--h577a1d6_8": "sha256:96c7a7fb99587b27e7ade742d087707181e75c07d6704f9f2c0a05ea62d93e54"}, "docker": "quay.io/biocontainers/ecoprimers", "aliases": {"ecoPrimers": "/usr/local/bin/ecoPrimers"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ecoprimers.
shpc-registry automated BioContainers addition for ecoprimers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ecoprimers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ecoprimers:1.0--h577a1d6_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ecoprimers/1.0--h577a1d6_8
$ module help quay.io/biocontainers/ecoprimers/1.0--h577a1d6_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ecoprimers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ecoprimers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ecoprimers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ecoprimers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ecoprimers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ecoprimers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ecoPrimers

```bash
$ singularity exec <container> /usr/local/bin/ecoPrimers
$ podman run --it --rm --entrypoint /usr/local/bin/ecoPrimers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecoPrimers   -v ${PWD} -w ${PWD} <container> -c " $@"
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