---
layout: container
name:  "quay.io/biocontainers/peakachu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/peakachu/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/peakachu/container.yaml"
updated_at: "2022-10-27 01:12:19.336239"
latest: "0.2.0--py36h91eb985_2"
container_url: "https://biocontainers.pro/tools/peakachu"
aliases:
 - "blockbuster.x"
 - "peakachu"
versions:
 - "0.2.0--py36h91eb985_2"
description: "shpc-registry automated BioContainers addition for peakachu"
config: {"url": "https://biocontainers.pro/tools/peakachu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for peakachu", "latest": {"0.2.0--py36h91eb985_2": "sha256:0858e75e0b0eacff2ccabd49349bc0168aa05ff7879fbabe2f95c1c9c3ae63d4"}, "tags": {"0.2.0--py36h91eb985_2": "sha256:0858e75e0b0eacff2ccabd49349bc0168aa05ff7879fbabe2f95c1c9c3ae63d4"}, "docker": "quay.io/biocontainers/peakachu", "aliases": {"blockbuster.x": "/usr/local/bin/blockbuster.x", "peakachu": "/usr/local/bin/peakachu"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/peakachu.
shpc-registry automated BioContainers addition for peakachu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/peakachu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/peakachu:0.2.0--py36h91eb985_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/peakachu/0.2.0--py36h91eb985_2
$ module help quay.io/biocontainers/peakachu/0.2.0--py36h91eb985_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### peakachu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### peakachu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### peakachu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### peakachu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### peakachu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### peakachu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blockbuster.x

```bash
$ singularity exec <container> /usr/local/bin/blockbuster.x
$ podman run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockbuster.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### peakachu

```bash
$ singularity exec <container> /usr/local/bin/peakachu
$ podman run --it --rm --entrypoint /usr/local/bin/peakachu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/peakachu   -v ${PWD} -w ${PWD} <container> -c " $@"
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