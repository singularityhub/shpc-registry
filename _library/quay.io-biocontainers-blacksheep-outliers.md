---
layout: container
name:  "quay.io/biocontainers/blacksheep-outliers"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blacksheep-outliers/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blacksheep-outliers/container.yaml"
updated_at: "2024-01-15 03:00:35.033783"
latest: "0.0.8--py_0"
container_url: "https://biocontainers.pro/tools/blacksheep-outliers"
aliases:
 - "deva"
 - "qhelpconverter"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
 - "qscxmlc"
 - "qtattributionsscanner"
 - "repc"
 - "pylupdate5"
 - "pyrcc5"
versions:
 - "0.0.8--py_0"
description: "shpc-registry automated BioContainers addition for blacksheep-outliers"
config: {"url": "https://biocontainers.pro/tools/blacksheep-outliers", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blacksheep-outliers", "latest": {"0.0.8--py_0": "sha256:1d1ab4a311e06cd02aa9fbb856dc396bd9970fef233e54445e1339c791531618"}, "tags": {"0.0.8--py_0": "sha256:1d1ab4a311e06cd02aa9fbb856dc396bd9970fef233e54445e1339c791531618"}, "docker": "quay.io/biocontainers/blacksheep-outliers", "aliases": {"deva": "/usr/local/bin/deva", "qhelpconverter": "/usr/local/bin/qhelpconverter", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen", "qscxmlc": "/usr/local/bin/qscxmlc", "qtattributionsscanner": "/usr/local/bin/qtattributionsscanner", "repc": "/usr/local/bin/repc", "pylupdate5": "/usr/local/bin/pylupdate5", "pyrcc5": "/usr/local/bin/pyrcc5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blacksheep-outliers.
shpc-registry automated BioContainers addition for blacksheep-outliers
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blacksheep-outliers
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blacksheep-outliers:0.0.8--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blacksheep-outliers/0.0.8--py_0
$ module help quay.io/biocontainers/blacksheep-outliers/0.0.8--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blacksheep-outliers-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blacksheep-outliers-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blacksheep-outliers-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blacksheep-outliers-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blacksheep-outliers-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blacksheep-outliers-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deva

```bash
$ singularity exec <container> /usr/local/bin/deva
$ podman run --it --rm --entrypoint /usr/local/bin/deva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qgltf

```bash
$ singularity exec <container> /usr/local/bin/qgltf
$ podman run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlcachegen

```bash
$ singularity exec <container> /usr/local/bin/qmlcachegen
$ podman run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qscxmlc

```bash
$ singularity exec <container> /usr/local/bin/qscxmlc
$ podman run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtattributionsscanner

```bash
$ singularity exec <container> /usr/local/bin/qtattributionsscanner
$ podman run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtattributionsscanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repc

```bash
$ singularity exec <container> /usr/local/bin/repc
$ podman run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylupdate5

```bash
$ singularity exec <container> /usr/local/bin/pylupdate5
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc5

```bash
$ singularity exec <container> /usr/local/bin/pyrcc5
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc5   -v ${PWD} -w ${PWD} <container> -c " $@"
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