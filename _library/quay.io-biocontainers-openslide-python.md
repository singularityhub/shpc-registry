---
layout: container
name:  "quay.io/biocontainers/openslide-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/openslide-python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/openslide-python/container.yaml"
updated_at: "2022-10-27 01:10:42.240749"
latest: "1.1.1--py36h470a237_0"
container_url: "https://biocontainers.pro/tools/openslide-python"
aliases:
 - "openslide-quickhash1sum"
 - "openslide-show-properties"
 - "openslide-write-png"
versions:
 - "1.1.1--py36h470a237_0"
description: "shpc-registry automated BioContainers addition for openslide-python"
config: {"url": "https://biocontainers.pro/tools/openslide-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for openslide-python", "latest": {"1.1.1--py36h470a237_0": "sha256:8e07e05e15b3d41e524af0a43121a98523c351b27c822e20dcfc106301f397a3"}, "tags": {"1.1.1--py36h470a237_0": "sha256:8e07e05e15b3d41e524af0a43121a98523c351b27c822e20dcfc106301f397a3"}, "docker": "quay.io/biocontainers/openslide-python", "aliases": {"openslide-quickhash1sum": "/usr/local/bin/openslide-quickhash1sum", "openslide-show-properties": "/usr/local/bin/openslide-show-properties", "openslide-write-png": "/usr/local/bin/openslide-write-png"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/openslide-python.
shpc-registry automated BioContainers addition for openslide-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/openslide-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/openslide-python:1.1.1--py36h470a237_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/openslide-python/1.1.1--py36h470a237_0
$ module help quay.io/biocontainers/openslide-python/1.1.1--py36h470a237_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openslide-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openslide-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openslide-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openslide-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openslide-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openslide-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### openslide-quickhash1sum

```bash
$ singularity exec <container> /usr/local/bin/openslide-quickhash1sum
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-quickhash1sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-quickhash1sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openslide-show-properties

```bash
$ singularity exec <container> /usr/local/bin/openslide-show-properties
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-show-properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-show-properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### openslide-write-png

```bash
$ singularity exec <container> /usr/local/bin/openslide-write-png
$ podman run --it --rm --entrypoint /usr/local/bin/openslide-write-png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/openslide-write-png   -v ${PWD} -w ${PWD} <container> -c " $@"
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