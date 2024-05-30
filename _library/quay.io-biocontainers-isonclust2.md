---
layout: container
name:  "quay.io/biocontainers/isonclust2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/isonclust2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/isonclust2/container.yaml"
updated_at: "2024-05-30 02:34:33.798022"
latest: "2.3--hc9558a2_0"
container_url: "https://biocontainers.pro/tools/isonclust2"
aliases:
 - "isONclust2"
versions:
 - "2.3--hc9558a2_0"
description: "shpc-registry automated BioContainers addition for isonclust2"
config: {"url": "https://biocontainers.pro/tools/isonclust2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for isonclust2", "latest": {"2.3--hc9558a2_0": "sha256:3203cea99d751b157686860c8a68ddfd4238e1ae8a59a039a6f13a91d17cf4eb"}, "tags": {"2.3--hc9558a2_0": "sha256:3203cea99d751b157686860c8a68ddfd4238e1ae8a59a039a6f13a91d17cf4eb"}, "docker": "quay.io/biocontainers/isonclust2", "aliases": {"isONclust2": "/usr/local/bin/isONclust2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/isonclust2.
shpc-registry automated BioContainers addition for isonclust2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/isonclust2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/isonclust2:2.3--hc9558a2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/isonclust2/2.3--hc9558a2_0
$ module help quay.io/biocontainers/isonclust2/2.3--hc9558a2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### isonclust2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### isonclust2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### isonclust2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### isonclust2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### isonclust2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### isonclust2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isONclust2

```bash
$ singularity exec <container> /usr/local/bin/isONclust2
$ podman run --it --rm --entrypoint /usr/local/bin/isONclust2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isONclust2   -v ${PWD} -w ${PWD} <container> -c " $@"
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