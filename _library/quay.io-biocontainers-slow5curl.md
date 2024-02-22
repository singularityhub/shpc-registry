---
layout: container
name:  "quay.io/biocontainers/slow5curl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slow5curl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slow5curl/container.yaml"
updated_at: "2024-02-22 04:49:34.336622"
latest: "0.2.0--h9bb4366_0"
container_url: "https://biocontainers.pro/tools/slow5curl"
aliases:
 - "slow5curl"
versions:
 - "0.2.0--h9bb4366_0"
description: "singularity registry hpc automated addition for slow5curl"
config: {"url": "https://biocontainers.pro/tools/slow5curl", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for slow5curl", "latest": {"0.2.0--h9bb4366_0": "sha256:591438316c6fa7ffd31bea7f30450160206d8fadc4ea639aaa192b44a1a67426"}, "tags": {"0.2.0--h9bb4366_0": "sha256:591438316c6fa7ffd31bea7f30450160206d8fadc4ea639aaa192b44a1a67426"}, "docker": "quay.io/biocontainers/slow5curl", "aliases": {"slow5curl": "/usr/local/bin/slow5curl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slow5curl.
singularity registry hpc automated addition for slow5curl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slow5curl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slow5curl:0.2.0--h9bb4366_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slow5curl/0.2.0--h9bb4366_0
$ module help quay.io/biocontainers/slow5curl/0.2.0--h9bb4366_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slow5curl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slow5curl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slow5curl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slow5curl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slow5curl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slow5curl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### slow5curl

```bash
$ singularity exec <container> /usr/local/bin/slow5curl
$ podman run --it --rm --entrypoint /usr/local/bin/slow5curl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slow5curl   -v ${PWD} -w ${PWD} <container> -c " $@"
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