---
layout: container
name:  "quay.io/biocontainers/drive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/drive/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/drive/container.yaml"
updated_at: "2025-03-08 03:05:23.578106"
latest: "0.3.9--h9ee0642_2"
container_url: "https://biocontainers.pro/tools/drive"
aliases:
 - "drive"
versions:
 - "0.3.9--h9ee0642_2"
description: "shpc-registry automated BioContainers addition for drive"
config: {"url": "https://biocontainers.pro/tools/drive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for drive", "latest": {"0.3.9--h9ee0642_2": "sha256:16f496d1fcc8a85e71336211f1505819346af31fd5c353a6357b1ff7ea8e9128"}, "tags": {"0.3.9--h9ee0642_2": "sha256:16f496d1fcc8a85e71336211f1505819346af31fd5c353a6357b1ff7ea8e9128"}, "docker": "quay.io/biocontainers/drive", "aliases": {"drive": "/usr/local/bin/drive"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/drive.
shpc-registry automated BioContainers addition for drive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/drive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/drive:0.3.9--h9ee0642_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/drive/0.3.9--h9ee0642_2
$ module help quay.io/biocontainers/drive/0.3.9--h9ee0642_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### drive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### drive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### drive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### drive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### drive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### drive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### drive

```bash
$ singularity exec <container> /usr/local/bin/drive
$ podman run --it --rm --entrypoint /usr/local/bin/drive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/drive   -v ${PWD} -w ${PWD} <container> -c " $@"
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