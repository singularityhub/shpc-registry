---
layout: container
name:  "quay.io/biocontainers/r-cobrar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-cobrar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-cobrar/container.yaml"
updated_at: "2025-12-29 04:14:02.181083"
latest: "0.2.0--r44h9948957_0"
container_url: "https://biocontainers.pro/tools/r-cobrar"
aliases:
 - "glpsol"
 - "hb-info"
 - "tjbench"
versions:
 - "0.1.0--r43h4ac6f70_0"
 - "0.1.1--r43h4ac6f70_1"
 - "0.1.1--r44h9948957_2"
 - "0.1.2--r44h9948957_0"
 - "0.2.0--r44h9948957_0"
description: "singularity registry hpc automated addition for r-cobrar"
config: {"url": "https://biocontainers.pro/tools/r-cobrar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-cobrar", "latest": {"0.2.0--r44h9948957_0": "sha256:0dc97a768ecb926e98644081236c88a9b41cdef6ab3d003c180c62896d0107cd"}, "tags": {"0.1.0--r43h4ac6f70_0": "sha256:a8c6b2e42bb75a7765953b1149182bdbf5adf0a4e559c6caaae094c4d1499e8c", "0.1.1--r43h4ac6f70_1": "sha256:9ae933335ce65381742f7b6db4cbc69db631bbc83cd380b7eec5759225d63446", "0.1.1--r44h9948957_2": "sha256:2c7e5a74d620d338b45960cd189fce1b23a7ed059e7c138f246e696fcfff871a", "0.1.2--r44h9948957_0": "sha256:9ec7ecea09e34e398440860048536f47ca679be504e8351377b8aa726b4060a3", "0.2.0--r44h9948957_0": "sha256:0dc97a768ecb926e98644081236c88a9b41cdef6ab3d003c180c62896d0107cd"}, "docker": "quay.io/biocontainers/r-cobrar", "aliases": {"glpsol": "/usr/local/bin/glpsol", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-cobrar.
singularity registry hpc automated addition for r-cobrar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-cobrar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-cobrar:0.2.0--r44h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-cobrar/0.2.0--r44h9948957_0
$ module help quay.io/biocontainers/r-cobrar/0.2.0--r44h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-cobrar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-cobrar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-cobrar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-cobrar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-cobrar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-cobrar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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