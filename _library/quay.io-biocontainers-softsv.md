---
layout: container
name:  "quay.io/biocontainers/softsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/softsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/softsv/container.yaml"
updated_at: "2025-12-18 04:17:05.009405"
latest: "1.4.2--hb891895_0"
container_url: "https://biocontainers.pro/tools/softsv"
aliases:
 - "SoftSV"
 - "bamtools"
versions:
 - "1.4.2--hb891895_0"
description: "singularity registry hpc automated addition for softsv"
config: {"url": "https://biocontainers.pro/tools/softsv", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for softsv", "latest": {"1.4.2--hb891895_0": "sha256:b2f6727d8b11029e33f5aa3b28fc15ac81d87eef5e5842e4c73ce271c8e5fb9f"}, "tags": {"1.4.2--hb891895_0": "sha256:b2f6727d8b11029e33f5aa3b28fc15ac81d87eef5e5842e4c73ce271c8e5fb9f"}, "docker": "quay.io/biocontainers/softsv", "aliases": {"SoftSV": "/usr/local/bin/SoftSV", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/softsv.
singularity registry hpc automated addition for softsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/softsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/softsv:1.4.2--hb891895_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/softsv/1.4.2--hb891895_0
$ module help quay.io/biocontainers/softsv/1.4.2--hb891895_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### softsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### softsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### softsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### softsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### softsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### softsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SoftSV

```bash
$ singularity exec <container> /usr/local/bin/SoftSV
$ podman run --it --rm --entrypoint /usr/local/bin/SoftSV   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SoftSV   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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