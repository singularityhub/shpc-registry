---
layout: container
name:  "quay.io/biocontainers/prosic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prosic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prosic/container.yaml"
updated_at: "2025-10-02 04:21:01.404999"
latest: "2.1.2--hc7800f0_1"
container_url: "https://biocontainers.pro/tools/prosic"
aliases:
 - "prosic"
versions:
 - "2.1.2--hc7800f0_1"
description: "shpc-registry automated BioContainers addition for prosic"
config: {"url": "https://biocontainers.pro/tools/prosic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prosic", "latest": {"2.1.2--hc7800f0_1": "sha256:6c4b941f61905dd7215149a3baf091eee27933cb00a2792a78d71ebc812d30ad"}, "tags": {"2.1.2--hc7800f0_1": "sha256:6c4b941f61905dd7215149a3baf091eee27933cb00a2792a78d71ebc812d30ad"}, "docker": "quay.io/biocontainers/prosic", "aliases": {"prosic": "/usr/local/bin/prosic"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prosic.
shpc-registry automated BioContainers addition for prosic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prosic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prosic:2.1.2--hc7800f0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prosic/2.1.2--hc7800f0_1
$ module help quay.io/biocontainers/prosic/2.1.2--hc7800f0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prosic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prosic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prosic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prosic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prosic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prosic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prosic

```bash
$ singularity exec <container> /usr/local/bin/prosic
$ podman run --it --rm --entrypoint /usr/local/bin/prosic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prosic   -v ${PWD} -w ${PWD} <container> -c " $@"
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