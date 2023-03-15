---
layout: container
name:  "quay.io/biocontainers/bedtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bedtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bedtk/container.yaml"
updated_at: "2023-03-15 02:44:39.606829"
latest: "0.0.r25.dirty--h7132678_2"
container_url: "https://biocontainers.pro/tools/bedtk"
aliases:
 - "bedtk"
versions:
 - "0.0.r25.dirty--h7132678_2"
description: "shpc-registry automated BioContainers addition for bedtk"
config: {"url": "https://biocontainers.pro/tools/bedtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bedtk", "latest": {"0.0.r25.dirty--h7132678_2": "sha256:7b6775d5f691908e9cd6cd6e2d70ee8ac7cb43ed5acea2f09d235930f9c3aed5"}, "tags": {"0.0.r25.dirty--h7132678_2": "sha256:7b6775d5f691908e9cd6cd6e2d70ee8ac7cb43ed5acea2f09d235930f9c3aed5"}, "docker": "quay.io/biocontainers/bedtk", "aliases": {"bedtk": "/usr/local/bin/bedtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bedtk.
shpc-registry automated BioContainers addition for bedtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bedtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bedtk:0.0.r25.dirty--h7132678_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bedtk/0.0.r25.dirty--h7132678_2
$ module help quay.io/biocontainers/bedtk/0.0.r25.dirty--h7132678_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bedtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bedtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bedtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bedtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bedtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bedtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedtk

```bash
$ singularity exec <container> /usr/local/bin/bedtk
$ podman run --it --rm --entrypoint /usr/local/bin/bedtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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