---
layout: container
name:  "quay.io/biocontainers/tadarida-d"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tadarida-d/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/tadarida-d/container.yaml"
updated_at: "2022-10-27 01:04:03.567115"
latest: "1.03--hf71b8e2_6"
container_url: "https://biocontainers.pro/tools/tadarida-d"
aliases:
 - "tadaridaD"
versions:
 - "1.03--hf71b8e2_6"
description: "shpc-registry automated BioContainers addition for tadarida-d"
config: {"url": "https://biocontainers.pro/tools/tadarida-d", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tadarida-d", "latest": {"1.03--hf71b8e2_6": "sha256:eb10379fc1249aed32e297659a5b03ca8d83a32c1d14428c3c1c58e89dfdccbd"}, "tags": {"1.03--hf71b8e2_6": "sha256:eb10379fc1249aed32e297659a5b03ca8d83a32c1d14428c3c1c58e89dfdccbd"}, "docker": "quay.io/biocontainers/tadarida-d", "aliases": {"tadaridaD": "/usr/local/bin/tadaridaD"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tadarida-d.
shpc-registry automated BioContainers addition for tadarida-d
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tadarida-d
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tadarida-d:1.03--hf71b8e2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tadarida-d/1.03--hf71b8e2_6
$ module help quay.io/biocontainers/tadarida-d/1.03--hf71b8e2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tadarida-d-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-d-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tadarida-d-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tadarida-d-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tadarida-d-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tadarida-d-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tadaridaD

```bash
$ singularity exec <container> /usr/local/bin/tadaridaD
$ podman run --it --rm --entrypoint /usr/local/bin/tadaridaD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tadaridaD   -v ${PWD} -w ${PWD} <container> -c " $@"
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