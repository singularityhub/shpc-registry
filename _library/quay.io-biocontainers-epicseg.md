---
layout: container
name:  "quay.io/biocontainers/epicseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/epicseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/epicseg/container.yaml"
updated_at: "2025-10-21 03:22:01.357670"
latest: "1.0--r42h031d066_8"
container_url: "https://biocontainers.pro/tools/epicseg"

versions:
 - "1.0--r41hec16e2b_6"
 - "1.0--r42hec16e2b_7"
 - "1.0--r42h031d066_8"
description: "shpc-registry automated BioContainers addition for epicseg"
config: {"url": "https://biocontainers.pro/tools/epicseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for epicseg", "latest": {"1.0--r42h031d066_8": "sha256:a8578385a51fa552ae37ff0c99a48dd8f0fd45626561f647d3164360d172bfc9"}, "tags": {"1.0--r41hec16e2b_6": "sha256:d6afb897a583b37026ba13bfa6bf145beaf4dfec19402c743f44e30fdf42fd46", "1.0--r42hec16e2b_7": "sha256:d3fc201f7c306175e50b6de941793bde2bd312766002153415e5d372c77d5687", "1.0--r42h031d066_8": "sha256:a8578385a51fa552ae37ff0c99a48dd8f0fd45626561f647d3164360d172bfc9"}, "docker": "quay.io/biocontainers/epicseg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/epicseg.
shpc-registry automated BioContainers addition for epicseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/epicseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/epicseg:1.0--r42h031d066_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/epicseg/1.0--r42h031d066_8
$ module help quay.io/biocontainers/epicseg/1.0--r42h031d066_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### epicseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### epicseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### epicseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### epicseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### epicseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### epicseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### epicseg

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