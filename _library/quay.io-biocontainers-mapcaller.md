---
layout: container
name:  "quay.io/biocontainers/mapcaller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapcaller/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mapcaller/container.yaml"
updated_at: "2022-10-27 00:19:12.883789"
latest: "0.9.9.7--h9b50bf8_0"
container_url: "https://biocontainers.pro/tools/mapcaller"
aliases:
 - "MapCaller"
 - "bwt_index"
versions:
 - "0.9.9.7--h9b50bf8_0"
description: "shpc-registry automated BioContainers addition for mapcaller"
config: {"url": "https://biocontainers.pro/tools/mapcaller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mapcaller", "latest": {"0.9.9.7--h9b50bf8_0": "sha256:c692fffa51b1ef8d39e6e9ca2da98dd8c8a77d47373fb663c81e5d64f944dbce"}, "tags": {"0.9.9.7--h9b50bf8_0": "sha256:c692fffa51b1ef8d39e6e9ca2da98dd8c8a77d47373fb663c81e5d64f944dbce"}, "docker": "quay.io/biocontainers/mapcaller", "aliases": {"MapCaller": "/usr/local/bin/MapCaller", "bwt_index": "/usr/local/bin/bwt_index"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapcaller.
shpc-registry automated BioContainers addition for mapcaller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapcaller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapcaller:0.9.9.7--h9b50bf8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapcaller/0.9.9.7--h9b50bf8_0
$ module help quay.io/biocontainers/mapcaller/0.9.9.7--h9b50bf8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapcaller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapcaller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapcaller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapcaller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapcaller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapcaller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MapCaller

```bash
$ singularity exec <container> /usr/local/bin/MapCaller
$ podman run --it --rm --entrypoint /usr/local/bin/MapCaller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MapCaller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwt_index

```bash
$ singularity exec <container> /usr/local/bin/bwt_index
$ podman run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
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