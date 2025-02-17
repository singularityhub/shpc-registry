---
layout: container
name:  "quay.io/biocontainers/geco3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/geco3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/geco3/container.yaml"
updated_at: "2025-02-17 03:00:24.151485"
latest: "1.0--h7b50bb2_5"
container_url: "https://biocontainers.pro/tools/geco3"
aliases:
 - "GeCo3"
 - "GeDe3"
versions:
 - "1.0--hec16e2b_2"
 - "1.0--h031d066_4"
 - "1.0--h7b50bb2_5"
description: "shpc-registry automated BioContainers addition for geco3"
config: {"url": "https://biocontainers.pro/tools/geco3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for geco3", "latest": {"1.0--h7b50bb2_5": "sha256:90a57dd39bf3e5424a4674b1bafa5dffcde29c928156745012c46b4043761a00"}, "tags": {"1.0--hec16e2b_2": "sha256:5272443167985ac059e2cafb1dbcfa3424d38b47a6f6daf487c4a1f694509436", "1.0--h031d066_4": "sha256:e11849f82e41170a733f4e04a2b0ad533218647dcca2020e6d07dc3e665fa5a8", "1.0--h7b50bb2_5": "sha256:90a57dd39bf3e5424a4674b1bafa5dffcde29c928156745012c46b4043761a00"}, "docker": "quay.io/biocontainers/geco3", "aliases": {"GeCo3": "/usr/local/bin/GeCo3", "GeDe3": "/usr/local/bin/GeDe3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/geco3.
shpc-registry automated BioContainers addition for geco3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/geco3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/geco3:1.0--h7b50bb2_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/geco3/1.0--h7b50bb2_5
$ module help quay.io/biocontainers/geco3/1.0--h7b50bb2_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geco3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geco3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geco3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geco3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geco3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geco3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeCo3

```bash
$ singularity exec <container> /usr/local/bin/GeCo3
$ podman run --it --rm --entrypoint /usr/local/bin/GeCo3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeCo3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeDe3

```bash
$ singularity exec <container> /usr/local/bin/GeDe3
$ podman run --it --rm --entrypoint /usr/local/bin/GeDe3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeDe3   -v ${PWD} -w ${PWD} <container> -c " $@"
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