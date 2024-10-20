---
layout: container
name:  "quay.io/biocontainers/orfanage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orfanage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orfanage/container.yaml"
updated_at: "2024-10-20 03:38:08.684487"
latest: "1.1.0--ha666654_0"
container_url: "https://biocontainers.pro/tools/orfanage"
aliases:
 - "orfanage"
versions:
 - "1.0.4--ha666654_0"
 - "1.1.0--ha666654_0"
description: "singularity registry hpc automated addition for orfanage"
config: {"url": "https://biocontainers.pro/tools/orfanage", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for orfanage", "latest": {"1.1.0--ha666654_0": "sha256:2ab928831e643e24e3919c12e034b9f18c0f9a2c29fe90a525073bd58683586d"}, "tags": {"1.0.4--ha666654_0": "sha256:e758da6b14f6b1338585cea0c9e1482bd9e6a78901fa5f148d34bb23a4ece3e3", "1.1.0--ha666654_0": "sha256:2ab928831e643e24e3919c12e034b9f18c0f9a2c29fe90a525073bd58683586d"}, "docker": "quay.io/biocontainers/orfanage", "aliases": {"orfanage": "/usr/local/bin/orfanage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orfanage.
singularity registry hpc automated addition for orfanage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orfanage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orfanage:1.1.0--ha666654_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orfanage/1.1.0--ha666654_0
$ module help quay.io/biocontainers/orfanage/1.1.0--ha666654_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orfanage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orfanage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orfanage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orfanage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orfanage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orfanage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### orfanage

```bash
$ singularity exec <container> /usr/local/bin/orfanage
$ podman run --it --rm --entrypoint /usr/local/bin/orfanage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orfanage   -v ${PWD} -w ${PWD} <container> -c " $@"
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