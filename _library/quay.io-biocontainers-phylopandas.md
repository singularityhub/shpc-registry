---
layout: container
name:  "quay.io/biocontainers/phylopandas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylopandas/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/phylopandas/container.yaml"
updated_at: "2022-10-27 00:43:31.286266"
latest: "0.8.0--py_0"
container_url: "https://biocontainers.pro/tools/phylopandas"

versions:
 - "0.8.0--py_0"
description: "shpc-registry automated BioContainers addition for phylopandas"
config: {"url": "https://biocontainers.pro/tools/phylopandas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylopandas", "latest": {"0.8.0--py_0": "sha256:b363e1ee18806db6cb229572576840850ccc801b5ced8bb33c40d666d8c0a4d1"}, "tags": {"0.8.0--py_0": "sha256:b363e1ee18806db6cb229572576840850ccc801b5ced8bb33c40d666d8c0a4d1"}, "docker": "quay.io/biocontainers/phylopandas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylopandas.
shpc-registry automated BioContainers addition for phylopandas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylopandas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylopandas:0.8.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylopandas/0.8.0--py_0
$ module help quay.io/biocontainers/phylopandas/0.8.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylopandas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylopandas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylopandas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylopandas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylopandas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylopandas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### phylopandas

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