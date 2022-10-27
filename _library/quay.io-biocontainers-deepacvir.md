---
layout: container
name:  "quay.io/biocontainers/deepacvir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepacvir/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepacvir/container.yaml"
updated_at: "2022-10-27 01:05:18.495770"
latest: "0.2.2--py_0"
container_url: "https://biocontainers.pro/tools/deepacvir"
aliases:
 - "deepac"
 - "deepac-vir"
 - "pyjwt"
versions:
 - "0.2.2--py_0"
description: "shpc-registry automated BioContainers addition for deepacvir"
config: {"url": "https://biocontainers.pro/tools/deepacvir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepacvir", "latest": {"0.2.2--py_0": "sha256:474f42f649a26f97f315c89fe64f9a85e13564a9cec844d4cc30e9e5e6691dc7"}, "tags": {"0.2.2--py_0": "sha256:474f42f649a26f97f315c89fe64f9a85e13564a9cec844d4cc30e9e5e6691dc7"}, "docker": "quay.io/biocontainers/deepacvir", "aliases": {"deepac": "/usr/local/bin/deepac", "deepac-vir": "/usr/local/bin/deepac-vir", "pyjwt": "/usr/local/bin/pyjwt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepacvir.
shpc-registry automated BioContainers addition for deepacvir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepacvir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepacvir:0.2.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepacvir/0.2.2--py_0
$ module help quay.io/biocontainers/deepacvir/0.2.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepacvir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepacvir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepacvir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepacvir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepacvir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepacvir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepac

```bash
$ singularity exec <container> /usr/local/bin/deepac
$ podman run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepac-vir

```bash
$ singularity exec <container> /usr/local/bin/deepac-vir
$ podman run --it --rm --entrypoint /usr/local/bin/deepac-vir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac-vir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjwt

```bash
$ singularity exec <container> /usr/local/bin/pyjwt
$ podman run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
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