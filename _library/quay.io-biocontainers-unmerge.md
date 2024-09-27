---
layout: container
name:  "quay.io/biocontainers/unmerge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unmerge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unmerge/container.yaml"
updated_at: "2024-09-27 03:08:58.109326"
latest: "1.0--hdbdd923_4"
container_url: "https://biocontainers.pro/tools/unmerge"
aliases:
 - "unmerge"
versions:
 - "1.0--h87f3376_2"
 - "1.0--hdbdd923_4"
description: "shpc-registry automated BioContainers addition for unmerge"
config: {"url": "https://biocontainers.pro/tools/unmerge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unmerge", "latest": {"1.0--hdbdd923_4": "sha256:e1341f4ff986f996d38d1d7f5d28f932cc81bb4867f7234e0779e6b83d3773c5"}, "tags": {"1.0--h87f3376_2": "sha256:46c2f61eb4dd82219959240b6f3b61692a5d57b1e28ec717e0cafd09dfa421e7", "1.0--hdbdd923_4": "sha256:e1341f4ff986f996d38d1d7f5d28f932cc81bb4867f7234e0779e6b83d3773c5"}, "docker": "quay.io/biocontainers/unmerge", "aliases": {"unmerge": "/usr/local/bin/unmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unmerge.
shpc-registry automated BioContainers addition for unmerge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unmerge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unmerge:1.0--hdbdd923_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unmerge/1.0--hdbdd923_4
$ module help quay.io/biocontainers/unmerge/1.0--hdbdd923_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unmerge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unmerge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unmerge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unmerge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unmerge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unmerge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unmerge

```bash
$ singularity exec <container> /usr/local/bin/unmerge
$ podman run --it --rm --entrypoint /usr/local/bin/unmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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