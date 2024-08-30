---
layout: container
name:  "quay.io/biocontainers/openslide"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/openslide/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/openslide/container.yaml"
updated_at: "2024-08-30 03:15:44.676991"
latest: "3.4.1--2"
container_url: "https://biocontainers.pro/tools/openslide"

versions:
 - "3.4.1--2"
description: "shpc-registry automated BioContainers addition for openslide"
config: {"url": "https://biocontainers.pro/tools/openslide", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for openslide", "latest": {"3.4.1--2": "sha256:3ac32a87d874eb4c003b6b87a54b94a20979defd53b97d9445625d9105f55db3"}, "tags": {"3.4.1--2": "sha256:3ac32a87d874eb4c003b6b87a54b94a20979defd53b97d9445625d9105f55db3"}, "docker": "quay.io/biocontainers/openslide"}
---

This module is a singularity container wrapper for quay.io/biocontainers/openslide.
shpc-registry automated BioContainers addition for openslide
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/openslide
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/openslide:3.4.1--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/openslide/3.4.1--2
$ module help quay.io/biocontainers/openslide/3.4.1--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openslide-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openslide-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openslide-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openslide-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openslide-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openslide-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openslide

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