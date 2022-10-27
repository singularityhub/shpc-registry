---
layout: container
name:  "quay.io/biocontainers/deeplc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deeplc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deeplc/container.yaml"
updated_at: "2022-10-27 00:32:03.889915"
latest: "1.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/deeplc"
aliases:
 - "deeplc"
 - "deeplc-gui"
versions:
 - "1.1.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for deeplc"
config: {"url": "https://biocontainers.pro/tools/deeplc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deeplc", "latest": {"1.1.2--pyhdfd78af_0": "sha256:ffd2beadc46a1f104fffcfd45a9be1ef8806f4a4b1189bad8da42a66820e3524"}, "tags": {"1.1.2--pyhdfd78af_0": "sha256:ffd2beadc46a1f104fffcfd45a9be1ef8806f4a4b1189bad8da42a66820e3524"}, "docker": "quay.io/biocontainers/deeplc", "aliases": {"deeplc": "/usr/local/bin/deeplc", "deeplc-gui": "/usr/local/bin/deeplc-gui"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deeplc.
shpc-registry automated BioContainers addition for deeplc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deeplc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deeplc:1.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deeplc/1.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/deeplc/1.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deeplc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deeplc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deeplc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deeplc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deeplc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deeplc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deeplc

```bash
$ singularity exec <container> /usr/local/bin/deeplc
$ podman run --it --rm --entrypoint /usr/local/bin/deeplc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeplc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deeplc-gui

```bash
$ singularity exec <container> /usr/local/bin/deeplc-gui
$ podman run --it --rm --entrypoint /usr/local/bin/deeplc-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deeplc-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
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