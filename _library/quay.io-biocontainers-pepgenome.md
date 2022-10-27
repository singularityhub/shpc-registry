---
layout: container
name:  "quay.io/biocontainers/pepgenome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pepgenome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pepgenome/container.yaml"
updated_at: "2022-10-27 00:59:35.233862"
latest: "1.1.beta--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/pepgenome"
aliases:
 - "pepgenome"
versions:
 - "1.1.beta--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for pepgenome"
config: {"url": "https://biocontainers.pro/tools/pepgenome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pepgenome", "latest": {"1.1.beta--hdfd78af_1": "sha256:48f3c98f473ca9131386aa6b6153ca928aa287cef8f79bd0bfa31f604512ec3d"}, "tags": {"1.1.beta--hdfd78af_1": "sha256:48f3c98f473ca9131386aa6b6153ca928aa287cef8f79bd0bfa31f604512ec3d"}, "docker": "quay.io/biocontainers/pepgenome", "aliases": {"pepgenome": "/usr/local/bin/pepgenome"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pepgenome.
shpc-registry automated BioContainers addition for pepgenome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pepgenome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pepgenome:1.1.beta--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pepgenome/1.1.beta--hdfd78af_1
$ module help quay.io/biocontainers/pepgenome/1.1.beta--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pepgenome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pepgenome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pepgenome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pepgenome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pepgenome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pepgenome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pepgenome

```bash
$ singularity exec <container> /usr/local/bin/pepgenome
$ podman run --it --rm --entrypoint /usr/local/bin/pepgenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pepgenome   -v ${PWD} -w ${PWD} <container> -c " $@"
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