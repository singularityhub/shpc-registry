---
layout: container
name:  "quay.io/biocontainers/postmaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/postmaster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/postmaster/container.yaml"
updated_at: "2025-09-25 07:43:44.588947"
latest: "0.1.0--ha6fb395_1"
container_url: "https://biocontainers.pro/tools/postmaster"
aliases:
 - "postmaster"
versions:
 - "0.1.0--ha6fb395_0"
 - "0.1.0--ha6fb395_1"
description: "singularity registry hpc automated addition for postmaster"
config: {"url": "https://biocontainers.pro/tools/postmaster", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for postmaster", "latest": {"0.1.0--ha6fb395_1": "sha256:78dabf12f500b69656bf6abf39687ba1441f4cdb0e533a73505531d6b3051028"}, "tags": {"0.1.0--ha6fb395_0": "sha256:4d5d721df3f89ff964d9031eb183e443d898d5b1cb02d635b5232660a9aa88b9", "0.1.0--ha6fb395_1": "sha256:78dabf12f500b69656bf6abf39687ba1441f4cdb0e533a73505531d6b3051028"}, "docker": "quay.io/biocontainers/postmaster", "aliases": {"postmaster": "/usr/local/bin/postmaster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/postmaster.
singularity registry hpc automated addition for postmaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/postmaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/postmaster:0.1.0--ha6fb395_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/postmaster/0.1.0--ha6fb395_1
$ module help quay.io/biocontainers/postmaster/0.1.0--ha6fb395_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### postmaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### postmaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### postmaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### postmaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### postmaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### postmaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### postmaster

```bash
$ singularity exec <container> /usr/local/bin/postmaster
$ podman run --it --rm --entrypoint /usr/local/bin/postmaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/postmaster   -v ${PWD} -w ${PWD} <container> -c " $@"
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