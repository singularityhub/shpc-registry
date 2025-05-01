---
layout: container
name:  "quay.io/biocontainers/peer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/peer/container.yaml"
updated_at: "2025-05-01 03:33:34.257011"
latest: "1.3--h503566f_1"
container_url: "https://biocontainers.pro/tools/peer"
aliases:
 - "peertool"
versions:
 - "1.3--hdbdd923_0"
 - "1.3--h503566f_1"
description: "singularity registry hpc automated addition for peer"
config: {"url": "https://biocontainers.pro/tools/peer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for peer", "latest": {"1.3--h503566f_1": "sha256:d58645effa4443de0a2bef18832f9aaafabfbdb54cc3825389798719525656c4"}, "tags": {"1.3--hdbdd923_0": "sha256:607e2cf162f874b50469508c1b6b5fc4aba154cb309b47765fd59e61648cb4a8", "1.3--h503566f_1": "sha256:d58645effa4443de0a2bef18832f9aaafabfbdb54cc3825389798719525656c4"}, "docker": "quay.io/biocontainers/peer", "aliases": {"peertool": "/usr/local/bin/peertool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peer.
singularity registry hpc automated addition for peer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peer:1.3--h503566f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peer/1.3--h503566f_1
$ module help quay.io/biocontainers/peer/1.3--h503566f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### peertool

```bash
$ singularity exec <container> /usr/local/bin/peertool
$ podman run --it --rm --entrypoint /usr/local/bin/peertool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peertool   -v ${PWD} -w ${PWD} <container> -c " $@"
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