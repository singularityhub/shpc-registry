---
layout: container
name:  "quay.io/biocontainers/concoord"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/concoord/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/concoord/container.yaml"
updated_at: "2024-05-12 03:04:35.014483"
latest: "2.1.2--h9ee0642_4"
container_url: "https://biocontainers.pro/tools/concoord"
aliases:
 - "dist"
 - "dist.exe"
 - "disco"
versions:
 - "2.1.2--h9ee0642_3"
 - "2.1.2--h9ee0642_4"
description: "singularity registry hpc automated addition for concoord"
config: {"url": "https://biocontainers.pro/tools/concoord", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for concoord", "latest": {"2.1.2--h9ee0642_4": "sha256:7c1f093c3ea5c96dfa844153e5534366bf12dd83962e4c0bb03c1ce9a0f1d2d5"}, "tags": {"2.1.2--h9ee0642_3": "sha256:4a2f2e71bdc3535d5baa44fcedbae196c7cdcc7f96656fe444767ab542c47ab5", "2.1.2--h9ee0642_4": "sha256:7c1f093c3ea5c96dfa844153e5534366bf12dd83962e4c0bb03c1ce9a0f1d2d5"}, "docker": "quay.io/biocontainers/concoord", "aliases": {"dist": "/usr/local/bin/dist", "dist.exe": "/usr/local/bin/dist.exe", "disco": "/usr/local/bin/disco"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/concoord.
singularity registry hpc automated addition for concoord
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/concoord
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/concoord:2.1.2--h9ee0642_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/concoord/2.1.2--h9ee0642_4
$ module help quay.io/biocontainers/concoord/2.1.2--h9ee0642_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### concoord-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### concoord-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### concoord-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### concoord-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### concoord-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### concoord-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dist

```bash
$ singularity exec <container> /usr/local/bin/dist
$ podman run --it --rm --entrypoint /usr/local/bin/dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dist.exe

```bash
$ singularity exec <container> /usr/local/bin/dist.exe
$ podman run --it --rm --entrypoint /usr/local/bin/dist.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dist.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disco

```bash
$ singularity exec <container> /usr/local/bin/disco
$ podman run --it --rm --entrypoint /usr/local/bin/disco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disco   -v ${PWD} -w ${PWD} <container> -c " $@"
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