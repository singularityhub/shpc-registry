---
layout: container
name:  "quay.io/biocontainers/socru"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/socru/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/socru/container.yaml"
updated_at: "2022-10-27 00:25:37.281086"
latest: "2.2.4--py_1"
container_url: "https://biocontainers.pro/tools/socru"
aliases:
 - "socru"
 - "socru_create"
 - "socru_rebuild_profile"
 - "socru_shrink_database"
 - "socru_species"
 - "socru_update_profile"
versions:
 - "2.2.4--py_1"
description: "shpc-registry automated BioContainers addition for socru"
config: {"url": "https://biocontainers.pro/tools/socru", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for socru", "latest": {"2.2.4--py_1": "sha256:7b75eac862334deac9d56ce38d1c3f49d7e878b0fa5930f17611f09774d3b6d8"}, "tags": {"2.2.4--py_1": "sha256:7b75eac862334deac9d56ce38d1c3f49d7e878b0fa5930f17611f09774d3b6d8"}, "docker": "quay.io/biocontainers/socru", "aliases": {"socru": "/usr/local/bin/socru", "socru_create": "/usr/local/bin/socru_create", "socru_rebuild_profile": "/usr/local/bin/socru_rebuild_profile", "socru_shrink_database": "/usr/local/bin/socru_shrink_database", "socru_species": "/usr/local/bin/socru_species", "socru_update_profile": "/usr/local/bin/socru_update_profile"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/socru.
shpc-registry automated BioContainers addition for socru
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/socru
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/socru:2.2.4--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/socru/2.2.4--py_1
$ module help quay.io/biocontainers/socru/2.2.4--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### socru-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### socru-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### socru-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### socru-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### socru-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### socru-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### socru

```bash
$ singularity exec <container> /usr/local/bin/socru
$ podman run --it --rm --entrypoint /usr/local/bin/socru   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### socru_create

```bash
$ singularity exec <container> /usr/local/bin/socru_create
$ podman run --it --rm --entrypoint /usr/local/bin/socru_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### socru_rebuild_profile

```bash
$ singularity exec <container> /usr/local/bin/socru_rebuild_profile
$ podman run --it --rm --entrypoint /usr/local/bin/socru_rebuild_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru_rebuild_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### socru_shrink_database

```bash
$ singularity exec <container> /usr/local/bin/socru_shrink_database
$ podman run --it --rm --entrypoint /usr/local/bin/socru_shrink_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru_shrink_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### socru_species

```bash
$ singularity exec <container> /usr/local/bin/socru_species
$ podman run --it --rm --entrypoint /usr/local/bin/socru_species   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru_species   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### socru_update_profile

```bash
$ singularity exec <container> /usr/local/bin/socru_update_profile
$ podman run --it --rm --entrypoint /usr/local/bin/socru_update_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/socru_update_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
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