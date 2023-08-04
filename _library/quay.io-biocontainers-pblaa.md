---
layout: container
name:  "quay.io/biocontainers/pblaa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pblaa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pblaa/container.yaml"
updated_at: "2023-08-04 03:06:20.454544"
latest: "2.4.2--2"
container_url: "https://biocontainers.pro/tools/pblaa"
aliases:
 - "laa"
 - "laagc"
versions:
 - "2.4.2--2"
description: "shpc-registry automated BioContainers addition for pblaa"
config: {"url": "https://biocontainers.pro/tools/pblaa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pblaa", "latest": {"2.4.2--2": "sha256:91ad9abe4418e268d6dee7ac2c70eebc7d927d1c4537ba37fd464d1fe9242893"}, "tags": {"2.4.2--2": "sha256:91ad9abe4418e268d6dee7ac2c70eebc7d927d1c4537ba37fd464d1fe9242893"}, "docker": "quay.io/biocontainers/pblaa", "aliases": {"laa": "/usr/local/bin/laa", "laagc": "/usr/local/bin/laagc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pblaa.
shpc-registry automated BioContainers addition for pblaa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pblaa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pblaa:2.4.2--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pblaa/2.4.2--2
$ module help quay.io/biocontainers/pblaa/2.4.2--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pblaa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pblaa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pblaa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pblaa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pblaa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pblaa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### laa

```bash
$ singularity exec <container> /usr/local/bin/laa
$ podman run --it --rm --entrypoint /usr/local/bin/laa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/laa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### laagc

```bash
$ singularity exec <container> /usr/local/bin/laagc
$ podman run --it --rm --entrypoint /usr/local/bin/laagc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/laagc   -v ${PWD} -w ${PWD} <container> -c " $@"
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