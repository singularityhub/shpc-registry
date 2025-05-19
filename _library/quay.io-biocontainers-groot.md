---
layout: container
name:  "quay.io/biocontainers/groot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/groot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/groot/container.yaml"
updated_at: "2025-05-19 03:42:01.409518"
latest: "1.1.2--h047eeb3_6"
container_url: "https://biocontainers.pro/tools/groot"
aliases:
 - "groot"
versions:
 - "1.1.2--hef68116_1"
 - "1.1.2--heaae5f8_3"
 - "1.1.2--heaae5f8_4"
 - "1.1.2--5"
 - "1.1.2--h047eeb3_6"
description: "shpc-registry automated BioContainers addition for groot"
config: {"url": "https://biocontainers.pro/tools/groot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for groot", "latest": {"1.1.2--h047eeb3_6": "sha256:a38dcc027a727ca12ebcd909363b952ff2d76d734f7d2f0cd8a9a522142b5d04"}, "tags": {"1.1.2--hef68116_1": "sha256:0f6fafab0423019c06fe8dafb8b8760de1ca254e1ac89a2bbffb072add276a20", "1.1.2--heaae5f8_3": "sha256:e52404e318ee76e3d6cb379858dfca15a67d1f911c64c415d71c8292bda6959e", "1.1.2--heaae5f8_4": "sha256:9638081be8f9dd8aa9ba9876f9dbf444811b863f84d51c775dcedb2c1ce9ce2a", "1.1.2--5": "sha256:8f6e7925415300dddde496679e2bd1ffd617724a7524245ed3093b82bc0e2c98", "1.1.2--h047eeb3_6": "sha256:a38dcc027a727ca12ebcd909363b952ff2d76d734f7d2f0cd8a9a522142b5d04"}, "docker": "quay.io/biocontainers/groot", "aliases": {"groot": "/usr/local/bin/groot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/groot.
shpc-registry automated BioContainers addition for groot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/groot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/groot:1.1.2--h047eeb3_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/groot/1.1.2--h047eeb3_6
$ module help quay.io/biocontainers/groot/1.1.2--h047eeb3_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### groot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### groot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### groot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### groot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### groot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### groot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### groot

```bash
$ singularity exec <container> /usr/local/bin/groot
$ podman run --it --rm --entrypoint /usr/local/bin/groot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groot   -v ${PWD} -w ${PWD} <container> -c " $@"
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