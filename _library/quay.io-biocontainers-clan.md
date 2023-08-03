---
layout: container
name:  "quay.io/biocontainers/clan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clan/container.yaml"
updated_at: "2023-08-03 02:46:37.608777"
latest: "0.05--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/clan"
aliases:
 - "clan_annotate"
 - "clan_index"
 - "clan_output"
 - "clan_search"
versions:
 - "0.05--h9f5acd7_2"
 - "0.05--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for clan"
config: {"url": "https://biocontainers.pro/tools/clan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clan", "latest": {"0.05--h4ac6f70_4": "sha256:1c13b1248732bb57e41352e987514c0d11fd3a0da9f0b912a60d20e159dc462e"}, "tags": {"0.05--h9f5acd7_2": "sha256:c21ca23fea4efb0f2fdd1153236ae4e763e4c75e37f048182f296e6de1da4370", "0.05--h4ac6f70_4": "sha256:1c13b1248732bb57e41352e987514c0d11fd3a0da9f0b912a60d20e159dc462e"}, "docker": "quay.io/biocontainers/clan", "aliases": {"clan_annotate": "/usr/local/bin/clan_annotate", "clan_index": "/usr/local/bin/clan_index", "clan_output": "/usr/local/bin/clan_output", "clan_search": "/usr/local/bin/clan_search"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clan.
shpc-registry automated BioContainers addition for clan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clan:0.05--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clan/0.05--h4ac6f70_4
$ module help quay.io/biocontainers/clan/0.05--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clan_annotate

```bash
$ singularity exec <container> /usr/local/bin/clan_annotate
$ podman run --it --rm --entrypoint /usr/local/bin/clan_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_index

```bash
$ singularity exec <container> /usr/local/bin/clan_index
$ podman run --it --rm --entrypoint /usr/local/bin/clan_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_output

```bash
$ singularity exec <container> /usr/local/bin/clan_output
$ podman run --it --rm --entrypoint /usr/local/bin/clan_output   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_output   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clan_search

```bash
$ singularity exec <container> /usr/local/bin/clan_search
$ podman run --it --rm --entrypoint /usr/local/bin/clan_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clan_search   -v ${PWD} -w ${PWD} <container> -c " $@"
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