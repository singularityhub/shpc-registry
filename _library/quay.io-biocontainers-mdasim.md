---
layout: container
name:  "quay.io/biocontainers/mdasim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mdasim/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mdasim/container.yaml"
updated_at: "2022-10-27 00:45:20.918264"
latest: "2.1.1--h5c6ebe3_3"
container_url: "https://biocontainers.pro/tools/mdasim"
aliases:
 - "mdasim"
versions:
 - "2.1.1--h5c6ebe3_3"
description: "shpc-registry automated BioContainers addition for mdasim"
config: {"url": "https://biocontainers.pro/tools/mdasim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mdasim", "latest": {"2.1.1--h5c6ebe3_3": "sha256:aa32932a2ab0050383992ba6bfa92af1f66b2ac94d94d447a075216f4879955c"}, "tags": {"2.1.1--h5c6ebe3_3": "sha256:aa32932a2ab0050383992ba6bfa92af1f66b2ac94d94d447a075216f4879955c"}, "docker": "quay.io/biocontainers/mdasim", "aliases": {"mdasim": "/usr/local/bin/mdasim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mdasim.
shpc-registry automated BioContainers addition for mdasim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mdasim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mdasim:2.1.1--h5c6ebe3_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mdasim/2.1.1--h5c6ebe3_3
$ module help quay.io/biocontainers/mdasim/2.1.1--h5c6ebe3_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mdasim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mdasim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mdasim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mdasim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mdasim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mdasim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mdasim

```bash
$ singularity exec <container> /usr/local/bin/mdasim
$ podman run --it --rm --entrypoint /usr/local/bin/mdasim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mdasim   -v ${PWD} -w ${PWD} <container> -c " $@"
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