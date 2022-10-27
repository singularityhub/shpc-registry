---
layout: container
name:  "quay.io/biocontainers/metaquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaquant/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metaquant/container.yaml"
updated_at: "2022-10-27 00:52:57.466004"
latest: "0.1.2--py_1"
container_url: "https://biocontainers.pro/tools/metaquant"
aliases:
 - "metaquant"
versions:
 - "0.1.2--py_1"
description: "shpc-registry automated BioContainers addition for metaquant"
config: {"url": "https://biocontainers.pro/tools/metaquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaquant", "latest": {"0.1.2--py_1": "sha256:dd422c77cc00a9d2a8094699e8e062cb0a7aa5bbbffd69d1aebed8bc90b71451"}, "tags": {"0.1.2--py_1": "sha256:dd422c77cc00a9d2a8094699e8e062cb0a7aa5bbbffd69d1aebed8bc90b71451"}, "docker": "quay.io/biocontainers/metaquant", "aliases": {"metaquant": "/usr/local/bin/metaquant"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaquant.
shpc-registry automated BioContainers addition for metaquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaquant:0.1.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaquant/0.1.2--py_1
$ module help quay.io/biocontainers/metaquant/0.1.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaquant

```bash
$ singularity exec <container> /usr/local/bin/metaquant
$ podman run --it --rm --entrypoint /usr/local/bin/metaquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquant   -v ${PWD} -w ${PWD} <container> -c " $@"
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