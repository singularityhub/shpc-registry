---
layout: container
name:  "quay.io/biocontainers/uchime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/uchime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/uchime/container.yaml"
updated_at: "2025-08-18 03:44:00.578284"
latest: "4.2--h9948957_0"
container_url: "https://biocontainers.pro/tools/uchime"
aliases:
 - "uchime"
versions:
 - "4.2--h9948957_0"
description: "singularity registry hpc automated addition for uchime"
config: {"url": "https://biocontainers.pro/tools/uchime", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for uchime", "latest": {"4.2--h9948957_0": "sha256:88adcb20a8d9b120e7f300f789d671016213f1c283996b135d8db6d33cb13cfd"}, "tags": {"4.2--h9948957_0": "sha256:88adcb20a8d9b120e7f300f789d671016213f1c283996b135d8db6d33cb13cfd"}, "docker": "quay.io/biocontainers/uchime", "aliases": {"uchime": "/usr/local/bin/uchime"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/uchime.
singularity registry hpc automated addition for uchime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/uchime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/uchime:4.2--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/uchime/4.2--h9948957_0
$ module help quay.io/biocontainers/uchime/4.2--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### uchime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### uchime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### uchime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### uchime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### uchime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uchime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uchime

```bash
$ singularity exec <container> /usr/local/bin/uchime
$ podman run --it --rm --entrypoint /usr/local/bin/uchime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uchime   -v ${PWD} -w ${PWD} <container> -c " $@"
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