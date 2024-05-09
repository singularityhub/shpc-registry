---
layout: container
name:  "quay.io/biocontainers/csblast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/csblast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/csblast/container.yaml"
updated_at: "2024-05-09 03:08:15.483047"
latest: "2.2.3--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/csblast"
aliases:
 - "csblast"
 - "csbuild"
versions:
 - "2.2.3--h9f5acd7_1"
 - "2.2.3--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for csblast"
config: {"url": "https://biocontainers.pro/tools/csblast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for csblast", "latest": {"2.2.3--h4ac6f70_3": "sha256:38d1000ee334556a76be30948f5b60e6a2277a7491b68b2ac49bc7265fff2208"}, "tags": {"2.2.3--h9f5acd7_1": "sha256:14e900025b43dcc8104578bda9a843760f994ced1a1d639ad701397eac508ccd", "2.2.3--h4ac6f70_3": "sha256:38d1000ee334556a76be30948f5b60e6a2277a7491b68b2ac49bc7265fff2208"}, "docker": "quay.io/biocontainers/csblast", "aliases": {"csblast": "/usr/local/bin/csblast", "csbuild": "/usr/local/bin/csbuild"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/csblast.
shpc-registry automated BioContainers addition for csblast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/csblast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/csblast:2.2.3--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/csblast/2.2.3--h4ac6f70_3
$ module help quay.io/biocontainers/csblast/2.2.3--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### csblast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### csblast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### csblast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### csblast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### csblast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### csblast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### csblast

```bash
$ singularity exec <container> /usr/local/bin/csblast
$ podman run --it --rm --entrypoint /usr/local/bin/csblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csbuild

```bash
$ singularity exec <container> /usr/local/bin/csbuild
$ podman run --it --rm --entrypoint /usr/local/bin/csbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
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