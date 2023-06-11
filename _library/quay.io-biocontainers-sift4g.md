---
layout: container
name:  "quay.io/biocontainers/sift4g"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sift4g/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sift4g/container.yaml"
updated_at: "2023-06-11 03:46:26.780213"
latest: "2.0.0--hdbdd923_6"
container_url: "https://biocontainers.pro/tools/sift4g"
aliases:
 - "sift4g"
versions:
 - "2.0.0--h87f3376_4"
 - "2.0.0--hdbdd923_6"
description: "shpc-registry automated BioContainers addition for sift4g"
config: {"url": "https://biocontainers.pro/tools/sift4g", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sift4g", "latest": {"2.0.0--hdbdd923_6": "sha256:83a64f2c493a5f9568db706c79f5a907a7baa03072467bb55cf9979e95d07c19"}, "tags": {"2.0.0--h87f3376_4": "sha256:cfa96b310d3bafaa0788eb9cfbcb2d8420f2319d11ea47337f19f15444b8672d", "2.0.0--hdbdd923_6": "sha256:83a64f2c493a5f9568db706c79f5a907a7baa03072467bb55cf9979e95d07c19"}, "docker": "quay.io/biocontainers/sift4g", "aliases": {"sift4g": "/usr/local/bin/sift4g"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sift4g.
shpc-registry automated BioContainers addition for sift4g
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sift4g
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sift4g:2.0.0--hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sift4g/2.0.0--hdbdd923_6
$ module help quay.io/biocontainers/sift4g/2.0.0--hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sift4g-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sift4g-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sift4g-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sift4g-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sift4g-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sift4g-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sift4g

```bash
$ singularity exec <container> /usr/local/bin/sift4g
$ podman run --it --rm --entrypoint /usr/local/bin/sift4g   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sift4g   -v ${PWD} -w ${PWD} <container> -c " $@"
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