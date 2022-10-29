---
layout: container
name:  "quay.io/biocontainers/metaquantome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaquantome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metaquantome/container.yaml"
updated_at: "2022-10-29 05:38:17.620155"
latest: "2.0.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metaquantome"
aliases:
 - "metaquantome"
 - "write_hierarchy.py"
 - "2to3-3.6"
 - "acyclic"
 - "assistant"
 - "bcomps"
 - "c89"
 - "c99"
 - "canbusutil"
 - "ccomps"
 - "circo"
 - "cluster"
versions:
 - "2.0.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metaquantome"
config: {"url": "https://biocontainers.pro/tools/metaquantome", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaquantome", "latest": {"2.0.2--pyhdfd78af_0": "sha256:63ecc9b2be8ab451aae2092d47d03e5f6e2d9217fa920e7bf488b1a6f1cb4f9e"}, "tags": {"2.0.2--pyhdfd78af_0": "sha256:63ecc9b2be8ab451aae2092d47d03e5f6e2d9217fa920e7bf488b1a6f1cb4f9e"}, "docker": "quay.io/biocontainers/metaquantome", "aliases": {"metaquantome": "/usr/local/bin/metaquantome", "write_hierarchy.py": "/usr/local/bin/write_hierarchy.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "acyclic": "/usr/local/bin/acyclic", "assistant": "/usr/local/bin/assistant", "bcomps": "/usr/local/bin/bcomps", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99", "canbusutil": "/usr/local/bin/canbusutil", "ccomps": "/usr/local/bin/ccomps", "circo": "/usr/local/bin/circo", "cluster": "/usr/local/bin/cluster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaquantome.
shpc-registry automated BioContainers addition for metaquantome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaquantome
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaquantome:2.0.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaquantome/2.0.2--pyhdfd78af_0
$ module help quay.io/biocontainers/metaquantome/2.0.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaquantome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaquantome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaquantome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaquantome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaquantome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaquantome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaquantome

```bash
$ singularity exec <container> /usr/local/bin/metaquantome
$ podman run --it --rm --entrypoint /usr/local/bin/metaquantome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaquantome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### write_hierarchy.py

```bash
$ singularity exec <container> /usr/local/bin/write_hierarchy.py
$ podman run --it --rm --entrypoint /usr/local/bin/write_hierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/write_hierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccomps

```bash
$ singularity exec <container> /usr/local/bin/ccomps
$ podman run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### circo

```bash
$ singularity exec <container> /usr/local/bin/circo
$ podman run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/circo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
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