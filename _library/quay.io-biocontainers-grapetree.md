---
layout: container
name:  "quay.io/biocontainers/grapetree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grapetree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grapetree/container.yaml"
updated_at: "2025-10-12 03:05:47.673919"
latest: "2.1--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/grapetree"
aliases:
 - "grapetree"
 - "unidecode"
 - "ete3"
 - "flask"
 - "numba"
 - "pycc"
 - "qhelpconverter"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
versions:
 - "2.1--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for grapetree"
config: {"url": "https://biocontainers.pro/tools/grapetree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for grapetree", "latest": {"2.1--pyh3252c3a_0": "sha256:fa040abbeb646bb2576536ccaec8b88683509c4e45842f81b954e27ac91e4a83"}, "tags": {"2.1--pyh3252c3a_0": "sha256:fa040abbeb646bb2576536ccaec8b88683509c4e45842f81b954e27ac91e4a83"}, "docker": "quay.io/biocontainers/grapetree", "aliases": {"grapetree": "/usr/local/bin/grapetree", "unidecode": "/usr/local/bin/unidecode", "ete3": "/usr/local/bin/ete3", "flask": "/usr/local/bin/flask", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "qhelpconverter": "/usr/local/bin/qhelpconverter", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grapetree.
shpc-registry automated BioContainers addition for grapetree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grapetree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grapetree:2.1--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grapetree/2.1--pyh3252c3a_0
$ module help quay.io/biocontainers/grapetree/2.1--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grapetree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grapetree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grapetree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grapetree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grapetree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grapetree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grapetree

```bash
$ singularity exec <container> /usr/local/bin/grapetree
$ podman run --it --rm --entrypoint /usr/local/bin/grapetree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grapetree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
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