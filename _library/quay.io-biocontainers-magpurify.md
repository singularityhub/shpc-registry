---
layout: container
name:  "quay.io/biocontainers/magpurify"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magpurify/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/magpurify/container.yaml"
updated_at: "2022-10-27 00:28:54.834979"
latest: "2.1.2--py_1"
container_url: "https://biocontainers.pro/tools/magpurify"
aliases:
 - ".magpurify-post-link.sh"
 - "coverm"
 - "last-split8"
 - "lastal8"
 - "lastdb8"
 - "maf-cut"
 - "magpurify"
 - "remove_minimap2_duplicated_headers"
 - "starcode"
versions:
 - "2.1.2--py_1"
description: "shpc-registry automated BioContainers addition for magpurify"
config: {"url": "https://biocontainers.pro/tools/magpurify", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for magpurify", "latest": {"2.1.2--py_1": "sha256:04aa9ea844627dcad499aa86a37c41e85936527c4f195ff1a4c8726c940546ae"}, "tags": {"2.1.2--py_1": "sha256:04aa9ea844627dcad499aa86a37c41e85936527c4f195ff1a4c8726c940546ae"}, "docker": "quay.io/biocontainers/magpurify", "aliases": {".magpurify-post-link.sh": "/usr/local/bin/.magpurify-post-link.sh", "coverm": "/usr/local/bin/coverm", "last-split8": "/usr/local/bin/last-split8", "lastal8": "/usr/local/bin/lastal8", "lastdb8": "/usr/local/bin/lastdb8", "maf-cut": "/usr/local/bin/maf-cut", "magpurify": "/usr/local/bin/magpurify", "remove_minimap2_duplicated_headers": "/usr/local/bin/remove_minimap2_duplicated_headers", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magpurify.
shpc-registry automated BioContainers addition for magpurify
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magpurify
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magpurify:2.1.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magpurify/2.1.2--py_1
$ module help quay.io/biocontainers/magpurify/2.1.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magpurify-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magpurify-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magpurify-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magpurify-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magpurify-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magpurify-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .magpurify-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.magpurify-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.magpurify-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.magpurify-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverm

```bash
$ singularity exec <container> /usr/local/bin/coverm
$ podman run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### last-split8

```bash
$ singularity exec <container> /usr/local/bin/last-split8
$ podman run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/last-split8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastal8

```bash
$ singularity exec <container> /usr/local/bin/lastal8
$ podman run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastal8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastdb8

```bash
$ singularity exec <container> /usr/local/bin/lastdb8
$ podman run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastdb8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maf-cut

```bash
$ singularity exec <container> /usr/local/bin/maf-cut
$ podman run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maf-cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magpurify

```bash
$ singularity exec <container> /usr/local/bin/magpurify
$ podman run --it --rm --entrypoint /usr/local/bin/magpurify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magpurify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_minimap2_duplicated_headers

```bash
$ singularity exec <container> /usr/local/bin/remove_minimap2_duplicated_headers
$ podman run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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