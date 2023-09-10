---
layout: container
name:  "quay.io/biocontainers/sirius-csifingerid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sirius-csifingerid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sirius-csifingerid/container.yaml"
updated_at: "2023-09-10 02:59:43.960295"
latest: "5.8.3--h3bb291f_0"
container_url: "https://biocontainers.pro/tools/sirius-csifingerid"
aliases:
 - "sirius"
 - "sirius-gui"
versions:
 - "4.9.8--hec16e2b_2"
 - "4.9.15--hec16e2b_1"
 - "4.9.15--h031d066_3"
 - "5.8.3--h3bb291f_0"
description: "shpc-registry automated BioContainers addition for sirius-csifingerid"
config: {"url": "https://biocontainers.pro/tools/sirius-csifingerid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sirius-csifingerid", "latest": {"5.8.3--h3bb291f_0": "sha256:b4439de18878f43d4372864aa9acbfd64d6a52cce5fcb5d33837e073661199f9"}, "tags": {"4.9.8--hec16e2b_2": "sha256:745743cc397513f88f5bb20ac0b5e48f9955deedfc071ee3104145146eb141d3", "4.9.15--hec16e2b_1": "sha256:6a8895779bba32e140f5aeda269947a291c4ef52fc5494bce537637925197804", "4.9.15--h031d066_3": "sha256:6515a407e6c8a85e666aae0aa78d2c5060c48dc046c1f3cb6ee2204e6ac76497", "5.8.3--h3bb291f_0": "sha256:b4439de18878f43d4372864aa9acbfd64d6a52cce5fcb5d33837e073661199f9"}, "docker": "quay.io/biocontainers/sirius-csifingerid", "aliases": {"sirius": "/usr/local/bin/sirius", "sirius-gui": "/usr/local/bin/sirius-gui"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sirius-csifingerid.
shpc-registry automated BioContainers addition for sirius-csifingerid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sirius-csifingerid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sirius-csifingerid:5.8.3--h3bb291f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sirius-csifingerid/5.8.3--h3bb291f_0
$ module help quay.io/biocontainers/sirius-csifingerid/5.8.3--h3bb291f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sirius-csifingerid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sirius-csifingerid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sirius-csifingerid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sirius-csifingerid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sirius-csifingerid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sirius-csifingerid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sirius

```bash
$ singularity exec <container> /usr/local/bin/sirius
$ podman run --it --rm --entrypoint /usr/local/bin/sirius   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sirius   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sirius-gui

```bash
$ singularity exec <container> /usr/local/bin/sirius-gui
$ podman run --it --rm --entrypoint /usr/local/bin/sirius-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sirius-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
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