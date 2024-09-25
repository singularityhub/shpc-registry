---
layout: container
name:  "quay.io/biocontainers/sketchy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sketchy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sketchy/container.yaml"
updated_at: "2024-09-25 03:37:14.605910"
latest: "0.6.0--h031d066_2"
container_url: "https://biocontainers.pro/tools/sketchy"
aliases:
 - "sketchy"
versions:
 - "0.6.0--hec16e2b_0"
 - "0.6.0--h031d066_2"
description: "shpc-registry automated BioContainers addition for sketchy"
config: {"url": "https://biocontainers.pro/tools/sketchy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sketchy", "latest": {"0.6.0--h031d066_2": "sha256:e7605987cec317c7421407bf321f2425152fb050d06f409fadff83923906fbbf"}, "tags": {"0.6.0--hec16e2b_0": "sha256:12541264d0ee2ca34315d9b675dee49a35ef3c74306fac2f4d78c28349d959e8", "0.6.0--h031d066_2": "sha256:e7605987cec317c7421407bf321f2425152fb050d06f409fadff83923906fbbf"}, "docker": "quay.io/biocontainers/sketchy", "aliases": {"sketchy": "/usr/local/bin/sketchy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sketchy.
shpc-registry automated BioContainers addition for sketchy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sketchy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sketchy:0.6.0--h031d066_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sketchy/0.6.0--h031d066_2
$ module help quay.io/biocontainers/sketchy/0.6.0--h031d066_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sketchy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sketchy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sketchy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sketchy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sketchy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sketchy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sketchy

```bash
$ singularity exec <container> /usr/local/bin/sketchy
$ podman run --it --rm --entrypoint /usr/local/bin/sketchy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchy   -v ${PWD} -w ${PWD} <container> -c " $@"
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