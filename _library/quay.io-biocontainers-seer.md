---
layout: container
name:  "quay.io/biocontainers/seer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/seer/container.yaml"
updated_at: "2022-10-27 00:57:47.957149"
latest: "1.1.4--hb75bb0b_0"
container_url: "https://biocontainers.pro/tools/seer"
aliases:
 - "combineKmers"
 - "filter_seer"
 - "kmds"
 - "map_back"
 - "seer"
versions:
 - "1.1.4--hb75bb0b_0"
description: "shpc-registry automated BioContainers addition for seer"
config: {"url": "https://biocontainers.pro/tools/seer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seer", "latest": {"1.1.4--hb75bb0b_0": "sha256:26f5c08323c37221c27772484c93363610921f45557206d6a6b81f495f993bbb"}, "tags": {"1.1.4--hb75bb0b_0": "sha256:26f5c08323c37221c27772484c93363610921f45557206d6a6b81f495f993bbb"}, "docker": "quay.io/biocontainers/seer", "aliases": {"combineKmers": "/usr/local/bin/combineKmers", "filter_seer": "/usr/local/bin/filter_seer", "kmds": "/usr/local/bin/kmds", "map_back": "/usr/local/bin/map_back", "seer": "/usr/local/bin/seer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seer.
shpc-registry automated BioContainers addition for seer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seer:1.1.4--hb75bb0b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seer/1.1.4--hb75bb0b_0
$ module help quay.io/biocontainers/seer/1.1.4--hb75bb0b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### combineKmers

```bash
$ singularity exec <container> /usr/local/bin/combineKmers
$ podman run --it --rm --entrypoint /usr/local/bin/combineKmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineKmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_seer

```bash
$ singularity exec <container> /usr/local/bin/filter_seer
$ podman run --it --rm --entrypoint /usr/local/bin/filter_seer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_seer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmds

```bash
$ singularity exec <container> /usr/local/bin/kmds
$ podman run --it --rm --entrypoint /usr/local/bin/kmds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### map_back

```bash
$ singularity exec <container> /usr/local/bin/map_back
$ podman run --it --rm --entrypoint /usr/local/bin/map_back   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/map_back   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seer

```bash
$ singularity exec <container> /usr/local/bin/seer
$ podman run --it --rm --entrypoint /usr/local/bin/seer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seer   -v ${PWD} -w ${PWD} <container> -c " $@"
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