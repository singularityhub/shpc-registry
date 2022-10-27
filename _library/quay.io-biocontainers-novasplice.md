---
layout: container
name:  "quay.io/biocontainers/novasplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/novasplice/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/novasplice/container.yaml"
updated_at: "2022-10-27 00:56:23.098725"
latest: "0.0.4--py_0"
container_url: "https://biocontainers.pro/tools/novasplice"
aliases:
 - "novasplice"
versions:
 - "0.0.4--py_0"
description: "shpc-registry automated BioContainers addition for novasplice"
config: {"url": "https://biocontainers.pro/tools/novasplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for novasplice", "latest": {"0.0.4--py_0": "sha256:80524cbb0bb1604c85a37d855fb10a5005d378f4a3323c9c25a7f78fc1824222"}, "tags": {"0.0.4--py_0": "sha256:80524cbb0bb1604c85a37d855fb10a5005d378f4a3323c9c25a7f78fc1824222"}, "docker": "quay.io/biocontainers/novasplice", "aliases": {"novasplice": "/usr/local/bin/novasplice"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/novasplice.
shpc-registry automated BioContainers addition for novasplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/novasplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/novasplice:0.0.4--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/novasplice/0.0.4--py_0
$ module help quay.io/biocontainers/novasplice/0.0.4--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### novasplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### novasplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### novasplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### novasplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### novasplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### novasplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### novasplice

```bash
$ singularity exec <container> /usr/local/bin/novasplice
$ podman run --it --rm --entrypoint /usr/local/bin/novasplice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novasplice   -v ${PWD} -w ${PWD} <container> -c " $@"
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