---
layout: container
name:  "quay.io/biocontainers/appspam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/appspam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/appspam/container.yaml"
updated_at: "2023-09-27 03:02:37.874101"
latest: "1.03--h9f5acd7_3"
container_url: "https://biocontainers.pro/tools/appspam"
aliases:
 - "appspam"
versions:
 - "1.03--h9f5acd7_2"
 - "1.03--h9f5acd7_3"
description: "shpc-registry automated BioContainers addition for appspam"
config: {"url": "https://biocontainers.pro/tools/appspam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for appspam", "latest": {"1.03--h9f5acd7_3": "sha256:13df04dd778259d4096e73443e97bcb7995aa6b50e0e67a5151fa42c9c616d69"}, "tags": {"1.03--h9f5acd7_2": "sha256:73dafecacd7cc3b654f3cdfb5e0b70f9f4150f17f15e343e0584559b63b7db88", "1.03--h9f5acd7_3": "sha256:13df04dd778259d4096e73443e97bcb7995aa6b50e0e67a5151fa42c9c616d69"}, "docker": "quay.io/biocontainers/appspam", "aliases": {"appspam": "/usr/local/bin/appspam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/appspam.
shpc-registry automated BioContainers addition for appspam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/appspam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/appspam:1.03--h9f5acd7_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/appspam/1.03--h9f5acd7_3
$ module help quay.io/biocontainers/appspam/1.03--h9f5acd7_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### appspam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### appspam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### appspam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### appspam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### appspam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### appspam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### appspam

```bash
$ singularity exec <container> /usr/local/bin/appspam
$ podman run --it --rm --entrypoint /usr/local/bin/appspam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appspam   -v ${PWD} -w ${PWD} <container> -c " $@"
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