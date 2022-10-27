---
layout: container
name:  "quay.io/biocontainers/stamp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/stamp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/stamp/container.yaml"
updated_at: "2022-10-27 00:26:15.885112"
latest: "2.1.3--py_2"
container_url: "https://biocontainers.pro/tools/stamp"
aliases:
 - "STAMP"
 - "checkHierarchy.py"
versions:
 - "2.1.3--py_2"
description: "shpc-registry automated BioContainers addition for stamp"
config: {"url": "https://biocontainers.pro/tools/stamp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for stamp", "latest": {"2.1.3--py_2": "sha256:5d810f59eb45a000171bf6894c84774982ddce8f84e094aff1a47c7ab1dc7453"}, "tags": {"2.1.3--py_2": "sha256:5d810f59eb45a000171bf6894c84774982ddce8f84e094aff1a47c7ab1dc7453"}, "docker": "quay.io/biocontainers/stamp", "aliases": {"STAMP": "/usr/local/bin/STAMP", "checkHierarchy.py": "/usr/local/bin/checkHierarchy.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/stamp.
shpc-registry automated BioContainers addition for stamp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/stamp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/stamp:2.1.3--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/stamp/2.1.3--py_2
$ module help quay.io/biocontainers/stamp/2.1.3--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stamp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stamp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stamp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stamp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stamp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stamp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STAMP

```bash
$ singularity exec <container> /usr/local/bin/STAMP
$ podman run --it --rm --entrypoint /usr/local/bin/STAMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkHierarchy.py

```bash
$ singularity exec <container> /usr/local/bin/checkHierarchy.py
$ podman run --it --rm --entrypoint /usr/local/bin/checkHierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkHierarchy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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