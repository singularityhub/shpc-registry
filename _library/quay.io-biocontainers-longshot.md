---
layout: container
name:  "quay.io/biocontainers/longshot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longshot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longshot/container.yaml"
updated_at: "2023-12-20 04:10:45.014650"
latest: "0.4.5--hd175d40_2"
container_url: "https://biocontainers.pro/tools/longshot"
aliases:
 - "longshot"
versions:
 - "v0.3.5--h80880c6_0"
 - "0.4.5--hc4ca7c3_0"
 - "0.4.5--hd175d40_2"
description: "shpc-registry automated BioContainers addition for longshot"
config: {"url": "https://biocontainers.pro/tools/longshot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for longshot", "latest": {"0.4.5--hd175d40_2": "sha256:1bf8278e82945cc7a8ca7eee3a71a84c43dd89f598da5cb64f458ae9cc535af8"}, "tags": {"v0.3.5--h80880c6_0": "sha256:8115bbdc19c0cf173a10bbffe22522ea83a7ae3a1fd0ecb46cf069a45ad1c88e", "0.4.5--hc4ca7c3_0": "sha256:2875eb55c1c48050e3cc7bb218710e2dccd6f5c43b9065b9debb7d8b96490f05", "0.4.5--hd175d40_2": "sha256:1bf8278e82945cc7a8ca7eee3a71a84c43dd89f598da5cb64f458ae9cc535af8"}, "docker": "quay.io/biocontainers/longshot", "aliases": {"longshot": "/usr/local/bin/longshot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longshot.
shpc-registry automated BioContainers addition for longshot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longshot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longshot:0.4.5--hd175d40_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longshot/0.4.5--hd175d40_2
$ module help quay.io/biocontainers/longshot/0.4.5--hd175d40_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longshot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longshot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longshot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longshot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longshot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longshot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### longshot

```bash
$ singularity exec <container> /usr/local/bin/longshot
$ podman run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
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