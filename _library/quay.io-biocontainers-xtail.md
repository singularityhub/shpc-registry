---
layout: container
name:  "quay.io/biocontainers/xtail"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xtail/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/xtail/container.yaml"
updated_at: "2022-10-27 00:36:01.097473"
latest: "1.1.5--r40_4"
container_url: "https://biocontainers.pro/tools/xtail"

versions:
 - "1.1.5--r40_4"
description: "shpc-registry automated BioContainers addition for xtail"
config: {"url": "https://biocontainers.pro/tools/xtail", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xtail", "latest": {"1.1.5--r40_4": "sha256:c8cb05fea45208e1645c214d919948a33c803b14aef28533aaacc962d5b12928"}, "tags": {"1.1.5--r40_4": "sha256:c8cb05fea45208e1645c214d919948a33c803b14aef28533aaacc962d5b12928"}, "docker": "quay.io/biocontainers/xtail"}
---

This module is a singularity container wrapper for quay.io/biocontainers/xtail.
shpc-registry automated BioContainers addition for xtail
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xtail
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xtail:1.1.5--r40_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xtail/1.1.5--r40_4
$ module help quay.io/biocontainers/xtail/1.1.5--r40_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xtail-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xtail-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xtail-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xtail-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xtail-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xtail-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### xtail

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