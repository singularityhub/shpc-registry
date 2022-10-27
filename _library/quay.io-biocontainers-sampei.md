---
layout: container
name:  "quay.io/biocontainers/sampei"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sampei/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sampei/container.yaml"
updated_at: "2022-10-27 00:28:45.482812"
latest: "0.0.9--py_0"
container_url: "https://biocontainers.pro/tools/sampei"
aliases:
 - "sampei"
versions:
 - "0.0.9--py_0"
description: "shpc-registry automated BioContainers addition for sampei"
config: {"url": "https://biocontainers.pro/tools/sampei", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sampei", "latest": {"0.0.9--py_0": "sha256:6f251497845abd94b1da93aca8e918f485f367618f4d68502a134dd833003aa3"}, "tags": {"0.0.9--py_0": "sha256:6f251497845abd94b1da93aca8e918f485f367618f4d68502a134dd833003aa3"}, "docker": "quay.io/biocontainers/sampei", "aliases": {"sampei": "/usr/local/bin/sampei"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sampei.
shpc-registry automated BioContainers addition for sampei
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sampei
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sampei:0.0.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sampei/0.0.9--py_0
$ module help quay.io/biocontainers/sampei/0.0.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sampei-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sampei-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sampei-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sampei-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sampei-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sampei-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sampei

```bash
$ singularity exec <container> /usr/local/bin/sampei
$ podman run --it --rm --entrypoint /usr/local/bin/sampei   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sampei   -v ${PWD} -w ${PWD} <container> -c " $@"
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