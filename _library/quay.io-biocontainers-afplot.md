---
layout: container
name:  "quay.io/biocontainers/afplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/afplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/afplot/container.yaml"
updated_at: "2025-03-03 03:01:50.021543"
latest: "0.2.1--py_2"
container_url: "https://biocontainers.pro/tools/afplot"

versions:
 - "0.2.1--py_2"
description: "shpc-registry automated BioContainers addition for afplot"
config: {"url": "https://biocontainers.pro/tools/afplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for afplot", "latest": {"0.2.1--py_2": "sha256:e9b22ea859f3ced98ab8fc7e1e8e9c1883fd7551f8f3999b16e828080203488b"}, "tags": {"0.2.1--py_2": "sha256:e9b22ea859f3ced98ab8fc7e1e8e9c1883fd7551f8f3999b16e828080203488b"}, "docker": "quay.io/biocontainers/afplot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/afplot.
shpc-registry automated BioContainers addition for afplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/afplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/afplot:0.2.1--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/afplot/0.2.1--py_2
$ module help quay.io/biocontainers/afplot/0.2.1--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### afplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### afplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### afplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### afplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### afplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### afplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### afplot

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