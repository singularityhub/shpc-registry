---
layout: container
name:  "quay.io/biocontainers/mercat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mercat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mercat/container.yaml"
updated_at: "2024-05-08 02:41:12.148591"
latest: "0.2--py_1"
container_url: "https://biocontainers.pro/tools/mercat"

versions:
 - "0.2--py_1"
description: "shpc-registry automated BioContainers addition for mercat"
config: {"url": "https://biocontainers.pro/tools/mercat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mercat", "latest": {"0.2--py_1": "sha256:bd0e18c7445a9e73f38a855339fccda2946c8a634db6c631b90f9cfaf91f63ae"}, "tags": {"0.2--py_1": "sha256:bd0e18c7445a9e73f38a855339fccda2946c8a634db6c631b90f9cfaf91f63ae"}, "docker": "quay.io/biocontainers/mercat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/mercat.
shpc-registry automated BioContainers addition for mercat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mercat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mercat:0.2--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mercat/0.2--py_1
$ module help quay.io/biocontainers/mercat/0.2--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mercat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mercat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mercat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mercat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mercat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mercat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mercat

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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