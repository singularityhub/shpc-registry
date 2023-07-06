---
layout: container
name:  "quay.io/biocontainers/gb_taxonomy_tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gb_taxonomy_tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gb_taxonomy_tools/container.yaml"
updated_at: "2023-07-06 07:23:11.102979"
latest: "1.0.1--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/gb_taxonomy_tools"
aliases:
 - "gid-taxid"
 - "taxonomy-reader"
 - "taxonomy2tree"
 - "tree2ps"
versions:
 - "1.0.1--h87f3376_3"
 - "1.0.1--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for gb_taxonomy_tools"
config: {"url": "https://biocontainers.pro/tools/gb_taxonomy_tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gb_taxonomy_tools", "latest": {"1.0.1--hdbdd923_5": "sha256:8639e375f6934327f2943cdfe95390b20c982034956b43d6dc4db28a824635eb"}, "tags": {"1.0.1--h87f3376_3": "sha256:d8b7b6baa53f8e88b62be2ab8b21b9299d812606c6827852f08c04b2f0d05b62", "1.0.1--hdbdd923_5": "sha256:8639e375f6934327f2943cdfe95390b20c982034956b43d6dc4db28a824635eb"}, "docker": "quay.io/biocontainers/gb_taxonomy_tools", "aliases": {"gid-taxid": "/usr/local/bin/gid-taxid", "taxonomy-reader": "/usr/local/bin/taxonomy-reader", "taxonomy2tree": "/usr/local/bin/taxonomy2tree", "tree2ps": "/usr/local/bin/tree2ps"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gb_taxonomy_tools.
shpc-registry automated BioContainers addition for gb_taxonomy_tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gb_taxonomy_tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gb_taxonomy_tools:1.0.1--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gb_taxonomy_tools/1.0.1--hdbdd923_5
$ module help quay.io/biocontainers/gb_taxonomy_tools/1.0.1--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gb_taxonomy_tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gb_taxonomy_tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gb_taxonomy_tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gb_taxonomy_tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gb_taxonomy_tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gb_taxonomy_tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gid-taxid

```bash
$ singularity exec <container> /usr/local/bin/gid-taxid
$ podman run --it --rm --entrypoint /usr/local/bin/gid-taxid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gid-taxid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonomy-reader

```bash
$ singularity exec <container> /usr/local/bin/taxonomy-reader
$ podman run --it --rm --entrypoint /usr/local/bin/taxonomy-reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonomy-reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonomy2tree

```bash
$ singularity exec <container> /usr/local/bin/taxonomy2tree
$ podman run --it --rm --entrypoint /usr/local/bin/taxonomy2tree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonomy2tree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tree2ps

```bash
$ singularity exec <container> /usr/local/bin/tree2ps
$ podman run --it --rm --entrypoint /usr/local/bin/tree2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree2ps   -v ${PWD} -w ${PWD} <container> -c " $@"
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