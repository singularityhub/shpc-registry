---
layout: container
name:  "quay.io/biocontainers/deepaclive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepaclive/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepaclive/container.yaml"
updated_at: "2022-10-27 00:58:16.743887"
latest: "0.3.2--py_0"
container_url: "https://biocontainers.pro/tools/deepaclive"
aliases:
 - "deepac"
 - "deepac-live"
versions:
 - "0.3.2--py_0"
description: "shpc-registry automated BioContainers addition for deepaclive"
config: {"url": "https://biocontainers.pro/tools/deepaclive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepaclive", "latest": {"0.3.2--py_0": "sha256:184e4f7cf2b3ef73b3d5b492f4eed715c0e1ac2e579c9a8b2f4fd8ac2050a257"}, "tags": {"0.3.2--py_0": "sha256:184e4f7cf2b3ef73b3d5b492f4eed715c0e1ac2e579c9a8b2f4fd8ac2050a257"}, "docker": "quay.io/biocontainers/deepaclive", "aliases": {"deepac": "/usr/local/bin/deepac", "deepac-live": "/usr/local/bin/deepac-live"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepaclive.
shpc-registry automated BioContainers addition for deepaclive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepaclive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepaclive:0.3.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepaclive/0.3.2--py_0
$ module help quay.io/biocontainers/deepaclive/0.3.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepaclive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepaclive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepaclive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepaclive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepaclive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepaclive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepac

```bash
$ singularity exec <container> /usr/local/bin/deepac
$ podman run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepac-live

```bash
$ singularity exec <container> /usr/local/bin/deepac-live
$ podman run --it --rm --entrypoint /usr/local/bin/deepac-live   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac-live   -v ${PWD} -w ${PWD} <container> -c " $@"
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