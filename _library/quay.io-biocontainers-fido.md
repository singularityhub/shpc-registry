---
layout: container
name:  "quay.io/biocontainers/fido"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fido/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fido/container.yaml"
updated_at: "2023-11-11 03:09:00.440236"
latest: "1.0--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/fido"
aliases:
 - "Fido"
 - "FidoChooseParameters"
versions:
 - "1.0--h9f5acd7_4"
 - "1.0--h9f5acd7_5"
 - "1.0--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for fido"
config: {"url": "https://biocontainers.pro/tools/fido", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fido", "latest": {"1.0--h4ac6f70_6": "sha256:6c85b1c93d40937ab34e7f2062bfd03c7a77548a0498960cbf4bd07679eda248"}, "tags": {"1.0--h9f5acd7_4": "sha256:fb93081e2598407c1b8f1867f1defa44ad54d274dfd7b00b1adaf680f6d3434f", "1.0--h9f5acd7_5": "sha256:f73a6450c9886e0e1c999ebae44b4fec4621206cfdda5d79777f5451cc93bba9", "1.0--h4ac6f70_6": "sha256:6c85b1c93d40937ab34e7f2062bfd03c7a77548a0498960cbf4bd07679eda248"}, "docker": "quay.io/biocontainers/fido", "aliases": {"Fido": "/usr/local/bin/Fido", "FidoChooseParameters": "/usr/local/bin/FidoChooseParameters"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fido.
shpc-registry automated BioContainers addition for fido
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fido
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fido:1.0--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fido/1.0--h4ac6f70_6
$ module help quay.io/biocontainers/fido/1.0--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fido-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fido-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fido-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fido-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fido-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fido-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Fido

```bash
$ singularity exec <container> /usr/local/bin/Fido
$ podman run --it --rm --entrypoint /usr/local/bin/Fido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FidoChooseParameters

```bash
$ singularity exec <container> /usr/local/bin/FidoChooseParameters
$ podman run --it --rm --entrypoint /usr/local/bin/FidoChooseParameters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FidoChooseParameters   -v ${PWD} -w ${PWD} <container> -c " $@"
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