---
layout: container
name:  "quay.io/biocontainers/genie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genie/container.yaml"
updated_at: "2025-07-28 09:54:25.677944"
latest: "0.7.0--h375a9b1_0"
container_url: "https://biocontainers.pro/tools/genie"
aliases:
 - "bolt"
 - "genie"
versions:
 - "0.7.0--h375a9b1_0"
description: "shpc-registry automated BioContainers addition for genie"
config: {"url": "https://biocontainers.pro/tools/genie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genie", "latest": {"0.7.0--h375a9b1_0": "sha256:29015ca494f823d517ea7b6f5aedb9d803761e07a44c83f292f91962c60f29f8"}, "tags": {"0.7.0--h375a9b1_0": "sha256:29015ca494f823d517ea7b6f5aedb9d803761e07a44c83f292f91962c60f29f8"}, "docker": "quay.io/biocontainers/genie", "aliases": {"bolt": "/usr/local/bin/bolt", "genie": "/usr/local/bin/genie"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genie.
shpc-registry automated BioContainers addition for genie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genie:0.7.0--h375a9b1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genie/0.7.0--h375a9b1_0
$ module help quay.io/biocontainers/genie/0.7.0--h375a9b1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bolt

```bash
$ singularity exec <container> /usr/local/bin/bolt
$ podman run --it --rm --entrypoint /usr/local/bin/bolt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bolt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genie

```bash
$ singularity exec <container> /usr/local/bin/genie
$ podman run --it --rm --entrypoint /usr/local/bin/genie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genie   -v ${PWD} -w ${PWD} <container> -c " $@"
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