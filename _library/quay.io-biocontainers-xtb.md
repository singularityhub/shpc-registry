---
layout: container
name:  "quay.io/biocontainers/xtb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xtb/container.yaml"
updated_at: "2025-04-19 03:21:51.535570"
latest: "6.6.1"
container_url: "https://biocontainers.pro/tools/xtb"
aliases:
 - "dftd4"
 - "s-dftd3"
 - "tblite"
 - "xtb"
versions:
 - "6.6.1"
description: "singularity registry hpc automated addition for xtb"
config: {"url": "https://biocontainers.pro/tools/xtb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for xtb", "latest": {"6.6.1": "sha256:d5e65f1a111bf7ba461073a7968aeeb6360c4a11cd0887972959abd3d72b26df"}, "tags": {"6.6.1": "sha256:d5e65f1a111bf7ba461073a7968aeeb6360c4a11cd0887972959abd3d72b26df"}, "docker": "quay.io/biocontainers/xtb", "aliases": {"dftd4": "/usr/local/bin/dftd4", "s-dftd3": "/usr/local/bin/s-dftd3", "tblite": "/usr/local/bin/tblite", "xtb": "/usr/local/bin/xtb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtb.
singularity registry hpc automated addition for xtb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtb:6.6.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtb/6.6.1
$ module help quay.io/biocontainers/xtb/6.6.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dftd4

```bash
$ singularity exec <container> /usr/local/bin/dftd4
$ podman run --it --rm --entrypoint /usr/local/bin/dftd4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dftd4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### s-dftd3

```bash
$ singularity exec <container> /usr/local/bin/s-dftd3
$ podman run --it --rm --entrypoint /usr/local/bin/s-dftd3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/s-dftd3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblite

```bash
$ singularity exec <container> /usr/local/bin/tblite
$ podman run --it --rm --entrypoint /usr/local/bin/tblite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtb

```bash
$ singularity exec <container> /usr/local/bin/xtb
$ podman run --it --rm --entrypoint /usr/local/bin/xtb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtb   -v ${PWD} -w ${PWD} <container> -c " $@"
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