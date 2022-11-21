---
layout: container
name:  "quay.io/biocontainers/bindash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bindash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bindash/container.yaml"
updated_at: "2022-11-21 00:20:42.514246"
latest: "1.0--h5b5514e_2"
container_url: "https://biocontainers.pro/tools/bindash"
aliases:
 - "bindash"
versions:
 - "1.0--h5b5514e_2"
description: "shpc-registry automated BioContainers addition for bindash"
config: {"url": "https://biocontainers.pro/tools/bindash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bindash", "latest": {"1.0--h5b5514e_2": "sha256:2c9b9be4093f73188173d1cd22c4518be613c2d75af805aca8497d08edd7d135"}, "tags": {"1.0--h5b5514e_2": "sha256:2c9b9be4093f73188173d1cd22c4518be613c2d75af805aca8497d08edd7d135"}, "docker": "quay.io/biocontainers/bindash", "aliases": {"bindash": "/usr/local/bin/bindash"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bindash.
shpc-registry automated BioContainers addition for bindash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bindash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bindash:1.0--h5b5514e_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bindash/1.0--h5b5514e_2
$ module help quay.io/biocontainers/bindash/1.0--h5b5514e_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bindash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bindash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bindash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bindash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bindash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bindash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bindash

```bash
$ singularity exec <container> /usr/local/bin/bindash
$ podman run --it --rm --entrypoint /usr/local/bin/bindash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bindash   -v ${PWD} -w ${PWD} <container> -c " $@"
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