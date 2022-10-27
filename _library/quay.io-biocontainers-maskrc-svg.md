---
layout: container
name:  "quay.io/biocontainers/maskrc-svg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maskrc-svg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/maskrc-svg/container.yaml"
updated_at: "2022-10-27 00:30:19.995686"
latest: "0.5--1"
container_url: "https://biocontainers.pro/tools/maskrc-svg"
aliases:
 - "maskrc-svg.py"
versions:
 - "0.5--1"
description: "shpc-registry automated BioContainers addition for maskrc-svg"
config: {"url": "https://biocontainers.pro/tools/maskrc-svg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for maskrc-svg", "latest": {"0.5--1": "sha256:f14601960406602426bd2a66183e8cdb8a25552c43a7f55349af6b51479c2b00"}, "tags": {"0.5--1": "sha256:f14601960406602426bd2a66183e8cdb8a25552c43a7f55349af6b51479c2b00"}, "docker": "quay.io/biocontainers/maskrc-svg", "aliases": {"maskrc-svg.py": "/usr/local/bin/maskrc-svg.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maskrc-svg.
shpc-registry automated BioContainers addition for maskrc-svg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maskrc-svg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maskrc-svg:0.5--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maskrc-svg/0.5--1
$ module help quay.io/biocontainers/maskrc-svg/0.5--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maskrc-svg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maskrc-svg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maskrc-svg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maskrc-svg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maskrc-svg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maskrc-svg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### maskrc-svg.py

```bash
$ singularity exec <container> /usr/local/bin/maskrc-svg.py
$ podman run --it --rm --entrypoint /usr/local/bin/maskrc-svg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maskrc-svg.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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