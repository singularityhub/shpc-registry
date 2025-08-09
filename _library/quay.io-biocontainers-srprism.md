---
layout: container
name:  "quay.io/biocontainers/srprism"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/srprism/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/srprism/container.yaml"
updated_at: "2025-08-09 03:54:14.220763"
latest: "2.4.24--hd6d6fdc_6"
container_url: "https://biocontainers.pro/tools/srprism"
aliases:
 - "srprism"
versions:
 - "2.4.24--h96824bc_3"
 - "2.4.24--h6a68c12_5"
 - "2.4.24--hd6d6fdc_6"
description: "shpc-registry automated BioContainers addition for srprism"
config: {"url": "https://biocontainers.pro/tools/srprism", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for srprism", "latest": {"2.4.24--hd6d6fdc_6": "sha256:9c0c37176c11835f9fdfd9e9420f2063204f3dcc695706e4c619aa10d520625e"}, "tags": {"2.4.24--h96824bc_3": "sha256:8606a5b78cc3c35a4e940caa1e26c96b717d4298fd15278c911fb15b43881e90", "2.4.24--h6a68c12_5": "sha256:33356e5ed80af2fd0b47a37466b6857edb6fabf07962949d3850052533e8135e", "2.4.24--hd6d6fdc_6": "sha256:9c0c37176c11835f9fdfd9e9420f2063204f3dcc695706e4c619aa10d520625e"}, "docker": "quay.io/biocontainers/srprism", "aliases": {"srprism": "/usr/local/bin/srprism"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/srprism.
shpc-registry automated BioContainers addition for srprism
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/srprism
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/srprism:2.4.24--hd6d6fdc_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/srprism/2.4.24--hd6d6fdc_6
$ module help quay.io/biocontainers/srprism/2.4.24--hd6d6fdc_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### srprism-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### srprism-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### srprism-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### srprism-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### srprism-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### srprism-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### srprism

```bash
$ singularity exec <container> /usr/local/bin/srprism
$ podman run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srprism   -v ${PWD} -w ${PWD} <container> -c " $@"
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