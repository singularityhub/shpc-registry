---
layout: container
name:  "quay.io/biocontainers/mykrobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mykrobe/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mykrobe/container.yaml"
updated_at: "2022-10-27 00:28:08.411270"
latest: "0.9.0--py38h8e3bb3f_3"
container_url: "https://biocontainers.pro/tools/mykrobe"
aliases:
 - "install_compass"
 - "mongo"
 - "mongod"
 - "mongos"
 - "mykrobe"
versions:
 - "0.9.0--py38h8e3bb3f_3"
description: "shpc-registry automated BioContainers addition for mykrobe"
config: {"url": "https://biocontainers.pro/tools/mykrobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mykrobe", "latest": {"0.9.0--py38h8e3bb3f_3": "sha256:cad54cf1570ba39df553217c2589f294560ccf692f0c6d5682844b92e95e7a02"}, "tags": {"0.9.0--py38h8e3bb3f_3": "sha256:cad54cf1570ba39df553217c2589f294560ccf692f0c6d5682844b92e95e7a02"}, "docker": "quay.io/biocontainers/mykrobe", "aliases": {"install_compass": "/usr/local/bin/install_compass", "mongo": "/usr/local/bin/mongo", "mongod": "/usr/local/bin/mongod", "mongos": "/usr/local/bin/mongos", "mykrobe": "/usr/local/bin/mykrobe"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mykrobe.
shpc-registry automated BioContainers addition for mykrobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mykrobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mykrobe:0.9.0--py38h8e3bb3f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mykrobe/0.9.0--py38h8e3bb3f_3
$ module help quay.io/biocontainers/mykrobe/0.9.0--py38h8e3bb3f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mykrobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mykrobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mykrobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mykrobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mykrobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mykrobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### install_compass

```bash
$ singularity exec <container> /usr/local/bin/install_compass
$ podman run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongo

```bash
$ singularity exec <container> /usr/local/bin/mongo
$ podman run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod

```bash
$ singularity exec <container> /usr/local/bin/mongod
$ podman run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos

```bash
$ singularity exec <container> /usr/local/bin/mongos
$ podman run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mykrobe

```bash
$ singularity exec <container> /usr/local/bin/mykrobe
$ podman run --it --rm --entrypoint /usr/local/bin/mykrobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mykrobe   -v ${PWD} -w ${PWD} <container> -c " $@"
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