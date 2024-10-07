---
layout: container
name:  "quay.io/biocontainers/nlstradamus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nlstradamus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nlstradamus/container.yaml"
updated_at: "2024-10-07 16:10:05.310600"
latest: "1.8--h2d50403_1"
container_url: "https://biocontainers.pro/tools/nlstradamus"
aliases:
 - "NLStradamus"
versions:
 - "1.8--h2d50403_1"
description: "shpc-registry automated BioContainers addition for nlstradamus"
config: {"url": "https://biocontainers.pro/tools/nlstradamus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nlstradamus", "latest": {"1.8--h2d50403_1": "sha256:f612cd558fd8de8df0661873a35cf18a6698a44d266ab410561eb7de594446a8"}, "tags": {"1.8--h2d50403_1": "sha256:f612cd558fd8de8df0661873a35cf18a6698a44d266ab410561eb7de594446a8"}, "docker": "quay.io/biocontainers/nlstradamus", "aliases": {"NLStradamus": "/usr/local/bin/NLStradamus"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nlstradamus.
shpc-registry automated BioContainers addition for nlstradamus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nlstradamus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nlstradamus:1.8--h2d50403_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nlstradamus/1.8--h2d50403_1
$ module help quay.io/biocontainers/nlstradamus/1.8--h2d50403_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nlstradamus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nlstradamus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nlstradamus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nlstradamus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nlstradamus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nlstradamus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NLStradamus

```bash
$ singularity exec <container> /usr/local/bin/NLStradamus
$ podman run --it --rm --entrypoint /usr/local/bin/NLStradamus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NLStradamus   -v ${PWD} -w ${PWD} <container> -c " $@"
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