---
layout: container
name:  "quay.io/biocontainers/r-genenet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-genenet/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-genenet/container.yaml"
updated_at: "2022-10-27 00:45:36.345237"
latest: "1.2.13--r3.2.2_0"
container_url: "https://biocontainers.pro/tools/r-genenet"

versions:
 - "1.2.13--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-genenet"
config: {"url": "https://biocontainers.pro/tools/r-genenet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-genenet", "latest": {"1.2.13--r3.2.2_0": "sha256:1764541c6612fb18ea61dbff6d45f859db2d5d69e017e973e79cbac02137dff8"}, "tags": {"1.2.13--r3.2.2_0": "sha256:1764541c6612fb18ea61dbff6d45f859db2d5d69e017e973e79cbac02137dff8"}, "docker": "quay.io/biocontainers/r-genenet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-genenet.
shpc-registry automated BioContainers addition for r-genenet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-genenet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-genenet:1.2.13--r3.2.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-genenet/1.2.13--r3.2.2_0
$ module help quay.io/biocontainers/r-genenet/1.2.13--r3.2.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-genenet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-genenet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-genenet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-genenet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-genenet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-genenet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-genenet

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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