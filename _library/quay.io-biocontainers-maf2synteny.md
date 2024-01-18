---
layout: container
name:  "quay.io/biocontainers/maf2synteny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/maf2synteny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/maf2synteny/container.yaml"
updated_at: "2024-01-18 02:47:01.589427"
latest: "1.2--hdbdd923_3"
container_url: "https://biocontainers.pro/tools/maf2synteny"
aliases:
 - "maf2synteny"
versions:
 - "1.2--h87f3376_1"
 - "1.2--hdbdd923_3"
description: "shpc-registry automated BioContainers addition for maf2synteny"
config: {"url": "https://biocontainers.pro/tools/maf2synteny", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for maf2synteny", "latest": {"1.2--hdbdd923_3": "sha256:0eaf4538351340e292663a9516639793ad6fb2818d64ff8f531a559bd3ebdb17"}, "tags": {"1.2--h87f3376_1": "sha256:e689496243bbcc4a7b0960e91ab59c6a580e1c0d65b20033236c9cd8c083a5b2", "1.2--hdbdd923_3": "sha256:0eaf4538351340e292663a9516639793ad6fb2818d64ff8f531a559bd3ebdb17"}, "docker": "quay.io/biocontainers/maf2synteny", "aliases": {"maf2synteny": "/usr/local/bin/maf2synteny"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/maf2synteny.
shpc-registry automated BioContainers addition for maf2synteny
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maf2synteny
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maf2synteny:1.2--hdbdd923_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maf2synteny/1.2--hdbdd923_3
$ module help quay.io/biocontainers/maf2synteny/1.2--hdbdd923_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maf2synteny-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maf2synteny-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maf2synteny-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maf2synteny-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maf2synteny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maf2synteny-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### maf2synteny

```bash
$ singularity exec <container> /usr/local/bin/maf2synteny
$ podman run --it --rm --entrypoint /usr/local/bin/maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf2synteny   -v ${PWD} -w ${PWD} <container> -c " $@"
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