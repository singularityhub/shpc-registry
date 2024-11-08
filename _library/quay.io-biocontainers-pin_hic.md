---
layout: container
name:  "quay.io/biocontainers/pin_hic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pin_hic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pin_hic/container.yaml"
updated_at: "2024-11-08 03:38:25.173728"
latest: "3.0.0--he4a0461_3"
container_url: "https://biocontainers.pro/tools/pin_hic"
aliases:
 - "pin_hic"
 - "pin_hic_it"
versions:
 - "3.0.0--h7132678_1"
 - "3.0.0--he4a0461_3"
description: "singularity registry hpc automated addition for pin_hic"
config: {"url": "https://biocontainers.pro/tools/pin_hic", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pin_hic", "latest": {"3.0.0--he4a0461_3": "sha256:6bb37fac9efa6b9907d54c0b0da04978c8251e6fa835fbe9f3c9feb5fc0bfd40"}, "tags": {"3.0.0--h7132678_1": "sha256:60a3ff5788a957dab57d6622c67ce5b13668b56f0ebbb47b6cf5e520322e708f", "3.0.0--he4a0461_3": "sha256:6bb37fac9efa6b9907d54c0b0da04978c8251e6fa835fbe9f3c9feb5fc0bfd40"}, "docker": "quay.io/biocontainers/pin_hic", "aliases": {"pin_hic": "/usr/local/bin/pin_hic", "pin_hic_it": "/usr/local/bin/pin_hic_it"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pin_hic.
singularity registry hpc automated addition for pin_hic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pin_hic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pin_hic:3.0.0--he4a0461_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pin_hic/3.0.0--he4a0461_3
$ module help quay.io/biocontainers/pin_hic/3.0.0--he4a0461_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pin_hic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pin_hic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pin_hic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pin_hic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pin_hic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pin_hic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pin_hic

```bash
$ singularity exec <container> /usr/local/bin/pin_hic
$ podman run --it --rm --entrypoint /usr/local/bin/pin_hic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pin_hic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pin_hic_it

```bash
$ singularity exec <container> /usr/local/bin/pin_hic_it
$ podman run --it --rm --entrypoint /usr/local/bin/pin_hic_it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pin_hic_it   -v ${PWD} -w ${PWD} <container> -c " $@"
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