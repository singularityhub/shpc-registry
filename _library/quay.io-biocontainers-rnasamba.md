---
layout: container
name:  "quay.io/biocontainers/rnasamba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rnasamba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rnasamba/container.yaml"
updated_at: "2022-10-27 00:54:30.251989"
latest: "0.2.5--py37h8902056_1"
container_url: "https://biocontainers.pro/tools/rnasamba"
aliases:
 - "rnasamba"
versions:
 - "0.2.5--py37h8902056_1"
description: "shpc-registry automated BioContainers addition for rnasamba"
config: {"url": "https://biocontainers.pro/tools/rnasamba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rnasamba", "latest": {"0.2.5--py37h8902056_1": "sha256:4b46eb4487718024405060e5e72655d68fe7308c5a90fcc5b2b9a0f27d604cfd"}, "tags": {"0.2.5--py37h8902056_1": "sha256:4b46eb4487718024405060e5e72655d68fe7308c5a90fcc5b2b9a0f27d604cfd"}, "docker": "quay.io/biocontainers/rnasamba", "aliases": {"rnasamba": "/usr/local/bin/rnasamba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rnasamba.
shpc-registry automated BioContainers addition for rnasamba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rnasamba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rnasamba:0.2.5--py37h8902056_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rnasamba/0.2.5--py37h8902056_1
$ module help quay.io/biocontainers/rnasamba/0.2.5--py37h8902056_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rnasamba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rnasamba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rnasamba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rnasamba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rnasamba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rnasamba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rnasamba

```bash
$ singularity exec <container> /usr/local/bin/rnasamba
$ podman run --it --rm --entrypoint /usr/local/bin/rnasamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnasamba   -v ${PWD} -w ${PWD} <container> -c " $@"
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