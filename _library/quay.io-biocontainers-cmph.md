---
layout: container
name:  "quay.io/biocontainers/cmph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmph/container.yaml"
updated_at: "2026-01-07 04:26:53.240240"
latest: "2.0--h7b50bb2_7"
container_url: "https://biocontainers.pro/tools/cmph"
aliases:
 - "cmph"
versions:
 - "2.0--hec16e2b_4"
 - "2.0--h031d066_6"
 - "2.0--h7b50bb2_7"
description: "shpc-registry automated BioContainers addition for cmph"
config: {"url": "https://biocontainers.pro/tools/cmph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmph", "latest": {"2.0--h7b50bb2_7": "sha256:3e285789ac1c6e4522696b7517384639e20851f502ba3287af28a98401143389"}, "tags": {"2.0--hec16e2b_4": "sha256:27d98fd34f53a01049952c0f677cdd0132aa3915d7924673bb1533ce088a3f1b", "2.0--h031d066_6": "sha256:99507504300c0347b4e2647743e002c40a3464d5220e5c7f70c63a44379574da", "2.0--h7b50bb2_7": "sha256:3e285789ac1c6e4522696b7517384639e20851f502ba3287af28a98401143389"}, "docker": "quay.io/biocontainers/cmph", "aliases": {"cmph": "/usr/local/bin/cmph"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmph.
shpc-registry automated BioContainers addition for cmph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmph:2.0--h7b50bb2_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmph/2.0--h7b50bb2_7
$ module help quay.io/biocontainers/cmph/2.0--h7b50bb2_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cmph

```bash
$ singularity exec <container> /usr/local/bin/cmph
$ podman run --it --rm --entrypoint /usr/local/bin/cmph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmph   -v ${PWD} -w ${PWD} <container> -c " $@"
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