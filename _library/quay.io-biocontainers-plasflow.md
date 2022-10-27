---
layout: container
name:  "quay.io/biocontainers/plasflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plasflow/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plasflow/container.yaml"
updated_at: "2022-10-27 00:18:38.834949"
latest: "1.1.0--py35_0"
container_url: "https://biocontainers.pro/tools/plasflow"
aliases:
 - "PlasFlow.py"
versions:
 - "1.1.0--py35_0"
description: "shpc-registry automated BioContainers addition for plasflow"
config: {"url": "https://biocontainers.pro/tools/plasflow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plasflow", "latest": {"1.1.0--py35_0": "sha256:74bb70254dd1a3eafd49050c4845a3657a05ff3466741d9e37d4b205216065e6"}, "tags": {"1.1.0--py35_0": "sha256:74bb70254dd1a3eafd49050c4845a3657a05ff3466741d9e37d4b205216065e6"}, "docker": "quay.io/biocontainers/plasflow", "aliases": {"PlasFlow.py": "/usr/local/bin/PlasFlow.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plasflow.
shpc-registry automated BioContainers addition for plasflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plasflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plasflow:1.1.0--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plasflow/1.1.0--py35_0
$ module help quay.io/biocontainers/plasflow/1.1.0--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PlasFlow.py

```bash
$ singularity exec <container> /usr/local/bin/PlasFlow.py
$ podman run --it --rm --entrypoint /usr/local/bin/PlasFlow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PlasFlow.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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