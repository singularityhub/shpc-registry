---
layout: container
name:  "quay.io/biocontainers/broccoli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/broccoli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/broccoli/container.yaml"
updated_at: "2026-10-11 08:58:45.805683"
latest: "2.0.0--hab7d0fd_0"
container_url: "https://biocontainers.pro/tools/broccoli"
aliases:
 - "broccoli"
 - "FastTreeMP"
 - "FastTree"
 - "fasttree"
 - "diamond"
versions:
 - "2.0.0--hab7d0fd_0"
description: "singularity registry hpc automated addition for broccoli"
config: {"url": "https://biocontainers.pro/tools/broccoli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for broccoli", "latest": {"2.0.0--hab7d0fd_0": "sha256:0366cd59a88bc4130942ab976984a88ad73c14b115515bbbfb97d6a41028c657"}, "tags": {"2.0.0--hab7d0fd_0": "sha256:0366cd59a88bc4130942ab976984a88ad73c14b115515bbbfb97d6a41028c657"}, "docker": "quay.io/biocontainers/broccoli", "aliases": {"broccoli": "/usr/local/bin/broccoli", "FastTreeMP": "/usr/local/bin/FastTreeMP", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "diamond": "/usr/local/bin/diamond"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/broccoli.
singularity registry hpc automated addition for broccoli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/broccoli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/broccoli:2.0.0--hab7d0fd_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/broccoli/2.0.0--hab7d0fd_0
$ module help quay.io/biocontainers/broccoli/2.0.0--hab7d0fd_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### broccoli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### broccoli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### broccoli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### broccoli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### broccoli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### broccoli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### broccoli

```bash
$ singularity exec <container> /usr/local/bin/broccoli
$ podman run --it --rm --entrypoint /usr/local/bin/broccoli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/broccoli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
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