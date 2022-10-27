---
layout: container
name:  "quay.io/biocontainers/coverm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coverm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/coverm/container.yaml"
updated_at: "2022-10-27 01:10:40.514101"
latest: "0.6.1--h1535e20_5"
container_url: "https://biocontainers.pro/tools/coverm"
aliases:
 - "coverm"
 - "dashing"
 - "remove_minimap2_duplicated_headers"
 - "starcode"
versions:
 - "0.6.1--h1535e20_5"
description: "shpc-registry automated BioContainers addition for coverm"
config: {"url": "https://biocontainers.pro/tools/coverm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coverm", "latest": {"0.6.1--h1535e20_5": "sha256:852de57f3f00862cd7524eb979fca849e887699d33af53661c4faf72aaef53bb"}, "tags": {"0.6.1--h1535e20_5": "sha256:852de57f3f00862cd7524eb979fca849e887699d33af53661c4faf72aaef53bb"}, "docker": "quay.io/biocontainers/coverm", "aliases": {"coverm": "/usr/local/bin/coverm", "dashing": "/usr/local/bin/dashing", "remove_minimap2_duplicated_headers": "/usr/local/bin/remove_minimap2_duplicated_headers", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coverm.
shpc-registry automated BioContainers addition for coverm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coverm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coverm:0.6.1--h1535e20_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coverm/0.6.1--h1535e20_5
$ module help quay.io/biocontainers/coverm/0.6.1--h1535e20_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coverm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coverm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coverm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coverm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coverm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coverm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coverm

```bash
$ singularity exec <container> /usr/local/bin/coverm
$ podman run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dashing

```bash
$ singularity exec <container> /usr/local/bin/dashing
$ podman run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
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