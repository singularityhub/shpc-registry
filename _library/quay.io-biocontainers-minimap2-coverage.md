---
layout: container
name:  "quay.io/biocontainers/minimap2-coverage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minimap2-coverage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minimap2-coverage/container.yaml"
updated_at: "2024-04-30 02:34:40.280361"
latest: "1.2.0c--he4a0461_3"
container_url: "https://biocontainers.pro/tools/minimap2-coverage"
aliases:
 - "minimap2-coverage"
versions:
 - "1.2.0c--h7132678_1"
 - "1.2.0c--he4a0461_3"
description: "shpc-registry automated BioContainers addition for minimap2-coverage"
config: {"url": "https://biocontainers.pro/tools/minimap2-coverage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minimap2-coverage", "latest": {"1.2.0c--he4a0461_3": "sha256:fabbbab508cce0ec5f08d0c03ba3711e0e4e34c7c303b68d64138e9339b4dbb7"}, "tags": {"1.2.0c--h7132678_1": "sha256:7d1b30706d8c3d12c97fda057cf7278cca18cad4548f62a12150c2f4e9cedd73", "1.2.0c--he4a0461_3": "sha256:fabbbab508cce0ec5f08d0c03ba3711e0e4e34c7c303b68d64138e9339b4dbb7"}, "docker": "quay.io/biocontainers/minimap2-coverage", "aliases": {"minimap2-coverage": "/usr/local/bin/minimap2-coverage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/minimap2-coverage.
shpc-registry automated BioContainers addition for minimap2-coverage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minimap2-coverage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minimap2-coverage:1.2.0c--he4a0461_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minimap2-coverage/1.2.0c--he4a0461_3
$ module help quay.io/biocontainers/minimap2-coverage/1.2.0c--he4a0461_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimap2-coverage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimap2-coverage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimap2-coverage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimap2-coverage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimap2-coverage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimap2-coverage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### minimap2-coverage

```bash
$ singularity exec <container> /usr/local/bin/minimap2-coverage
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
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