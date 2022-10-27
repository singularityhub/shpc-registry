---
layout: container
name:  "quay.io/biocontainers/forceatlas2-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/forceatlas2-python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/forceatlas2-python/container.yaml"
updated_at: "2022-10-27 01:03:12.657163"
latest: "1.1--py_1"
container_url: "https://biocontainers.pro/tools/forceatlas2-python"

versions:
 - "1.1--py_1"
description: "shpc-registry automated BioContainers addition for forceatlas2-python"
config: {"url": "https://biocontainers.pro/tools/forceatlas2-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for forceatlas2-python", "latest": {"1.1--py_1": "sha256:f37e1832ac2e3e3bb99d12f1e9090c1253a2359294e69b25940107ed9c4e7e3e"}, "tags": {"1.1--py_1": "sha256:f37e1832ac2e3e3bb99d12f1e9090c1253a2359294e69b25940107ed9c4e7e3e"}, "docker": "quay.io/biocontainers/forceatlas2-python"}
---

This module is a singularity container wrapper for quay.io/biocontainers/forceatlas2-python.
shpc-registry automated BioContainers addition for forceatlas2-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/forceatlas2-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/forceatlas2-python:1.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/forceatlas2-python/1.1--py_1
$ module help quay.io/biocontainers/forceatlas2-python/1.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### forceatlas2-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### forceatlas2-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### forceatlas2-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### forceatlas2-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### forceatlas2-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### forceatlas2-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### forceatlas2-python

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