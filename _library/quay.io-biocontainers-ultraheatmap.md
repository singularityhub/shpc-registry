---
layout: container
name:  "quay.io/biocontainers/ultraheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ultraheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ultraheatmap/container.yaml"
updated_at: "2022-10-27 01:13:36.886315"
latest: "1.3.1--py_1"
container_url: "https://biocontainers.pro/tools/ultraheatmap"
aliases:
 - "addFeatureToMatrix"
 - "computeOrderedMatrix"
 - "ultraheatmap"
versions:
 - "1.3.1--py_1"
description: "shpc-registry automated BioContainers addition for ultraheatmap"
config: {"url": "https://biocontainers.pro/tools/ultraheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ultraheatmap", "latest": {"1.3.1--py_1": "sha256:cedbdbafd98c62e90b0fe5c865259ccbc9b4f4582318a71303613b675415f83e"}, "tags": {"1.3.1--py_1": "sha256:cedbdbafd98c62e90b0fe5c865259ccbc9b4f4582318a71303613b675415f83e"}, "docker": "quay.io/biocontainers/ultraheatmap", "aliases": {"addFeatureToMatrix": "/usr/local/bin/addFeatureToMatrix", "computeOrderedMatrix": "/usr/local/bin/computeOrderedMatrix", "ultraheatmap": "/usr/local/bin/ultraheatmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ultraheatmap.
shpc-registry automated BioContainers addition for ultraheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ultraheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ultraheatmap:1.3.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ultraheatmap/1.3.1--py_1
$ module help quay.io/biocontainers/ultraheatmap/1.3.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ultraheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ultraheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ultraheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ultraheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ultraheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ultraheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addFeatureToMatrix

```bash
$ singularity exec <container> /usr/local/bin/addFeatureToMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/addFeatureToMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addFeatureToMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### computeOrderedMatrix

```bash
$ singularity exec <container> /usr/local/bin/computeOrderedMatrix
$ podman run --it --rm --entrypoint /usr/local/bin/computeOrderedMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/computeOrderedMatrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ultraheatmap

```bash
$ singularity exec <container> /usr/local/bin/ultraheatmap
$ podman run --it --rm --entrypoint /usr/local/bin/ultraheatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ultraheatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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