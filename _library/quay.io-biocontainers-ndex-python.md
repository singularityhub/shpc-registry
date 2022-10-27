---
layout: container
name:  "quay.io/biocontainers/ndex-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ndex-python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ndex-python/container.yaml"
updated_at: "2022-10-27 01:00:16.367103"
latest: "3.0.11.23--py_2"
container_url: "https://biocontainers.pro/tools/ndex-python"

versions:
 - "3.0.11.23--py_2"
description: "shpc-registry automated BioContainers addition for ndex-python"
config: {"url": "https://biocontainers.pro/tools/ndex-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ndex-python", "latest": {"3.0.11.23--py_2": "sha256:232e6aae575b9b6638cf2cf794776449e1ddd378738f23f8e9693cb993694740"}, "tags": {"3.0.11.23--py_2": "sha256:232e6aae575b9b6638cf2cf794776449e1ddd378738f23f8e9693cb993694740"}, "docker": "quay.io/biocontainers/ndex-python"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ndex-python.
shpc-registry automated BioContainers addition for ndex-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ndex-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ndex-python:3.0.11.23--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ndex-python/3.0.11.23--py_2
$ module help quay.io/biocontainers/ndex-python/3.0.11.23--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ndex-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ndex-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ndex-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ndex-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ndex-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ndex-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ndex-python

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