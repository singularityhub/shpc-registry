---
layout: container
name:  "quay.io/biocontainers/circexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/circexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/circexplorer/container.yaml"
updated_at: "2024-10-19 03:20:05.240760"
latest: "1.1.10--py_4"
container_url: "https://biocontainers.pro/tools/circexplorer"

versions:
 - "1.1.9--py35_0"
 - "1.1.10--py_4"
description: "shpc-registry automated BioContainers addition for circexplorer"
config: {"url": "https://biocontainers.pro/tools/circexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for circexplorer", "latest": {"1.1.10--py_4": "sha256:a8c76cb7df3fc346c144ac7b58a823a9e46a3a3f2858261a07ce55cc783d7ce8"}, "tags": {"1.1.9--py35_0": "sha256:5a9486acf9eae51939d1802e143d686d8a77b8ca56c7b9ee678aca5a7d4e146a", "1.1.10--py_4": "sha256:a8c76cb7df3fc346c144ac7b58a823a9e46a3a3f2858261a07ce55cc783d7ce8"}, "docker": "quay.io/biocontainers/circexplorer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/circexplorer.
shpc-registry automated BioContainers addition for circexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/circexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/circexplorer:1.1.10--py_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/circexplorer/1.1.10--py_4
$ module help quay.io/biocontainers/circexplorer/1.1.10--py_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### circexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### circexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### circexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### circexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### circexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### circexplorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### circexplorer

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