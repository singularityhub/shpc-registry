---
layout: container
name:  "quay.io/biocontainers/libdivsufsort"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libdivsufsort/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libdivsufsort/container.yaml"
updated_at: "2025-03-27 03:47:39.076791"
latest: "2.0.2--h7b50bb2_10"
container_url: "https://biocontainers.pro/tools/libdivsufsort"

versions:
 - "2.0.2--hec16e2b_6"
 - "2.0.2--h031d066_8"
 - "2.0.2--h031d066_9"
 - "2.0.2--h7b50bb2_10"
description: "shpc-registry automated BioContainers addition for libdivsufsort"
config: {"url": "https://biocontainers.pro/tools/libdivsufsort", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libdivsufsort", "latest": {"2.0.2--h7b50bb2_10": "sha256:1d5eeef9e3599c715ac1d257f66b612b4eed969ec9962b2c57e50ff9e8c14322"}, "tags": {"2.0.2--hec16e2b_6": "sha256:d4db8163b70eda62444f834d4ace91cc562a92c045851845b3d7ac7821b2066c", "2.0.2--h031d066_8": "sha256:da5ac54d0795bc69c0fd45c233d65e8cb09cd4454b49eca0d7278bfac2cd41e4", "2.0.2--h031d066_9": "sha256:8f2e658841b7539b227f12895e2ee0308cf4823e1a419c19a12fe65e9dd59f8d", "2.0.2--h7b50bb2_10": "sha256:1d5eeef9e3599c715ac1d257f66b612b4eed969ec9962b2c57e50ff9e8c14322"}, "docker": "quay.io/biocontainers/libdivsufsort"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libdivsufsort.
shpc-registry automated BioContainers addition for libdivsufsort
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libdivsufsort
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libdivsufsort:2.0.2--h7b50bb2_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libdivsufsort/2.0.2--h7b50bb2_10
$ module help quay.io/biocontainers/libdivsufsort/2.0.2--h7b50bb2_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libdivsufsort-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libdivsufsort-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libdivsufsort-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libdivsufsort-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libdivsufsort-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libdivsufsort-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libdivsufsort

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