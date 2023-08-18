---
layout: container
name:  "quay.io/biocontainers/platypus-conquistador"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/platypus-conquistador/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/platypus-conquistador/container.yaml"
updated_at: "2023-08-18 02:52:13.994059"
latest: "0.9.0--py_3"
container_url: "https://biocontainers.pro/tools/platypus-conquistador"
aliases:
 - "iptest2"
 - "ipython2"
 - "platypus"
 - "iptest"
 - "ipython"
 - "natsort"
 - "qhelpconverter"
 - "f2py2"
 - "f2py2.7"
 - "qwebengine_convert_dict"
 - "pygmentize"
 - "canbusutil"
 - "qgltf"
versions:
 - "0.9.0--py_3"
description: "shpc-registry automated BioContainers addition for platypus-conquistador"
config: {"url": "https://biocontainers.pro/tools/platypus-conquistador", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for platypus-conquistador", "latest": {"0.9.0--py_3": "sha256:f42b19b89a5148a24001db71c20333a2dd6e7283e7c9e1d99d06a6d55a6ebed0"}, "tags": {"0.9.0--py_3": "sha256:f42b19b89a5148a24001db71c20333a2dd6e7283e7c9e1d99d06a6d55a6ebed0"}, "docker": "quay.io/biocontainers/platypus-conquistador", "aliases": {"iptest2": "/usr/local/bin/iptest2", "ipython2": "/usr/local/bin/ipython2", "platypus": "/usr/local/bin/platypus", "iptest": "/usr/local/bin/iptest", "ipython": "/usr/local/bin/ipython", "natsort": "/usr/local/bin/natsort", "qhelpconverter": "/usr/local/bin/qhelpconverter", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "pygmentize": "/usr/local/bin/pygmentize", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/platypus-conquistador.
shpc-registry automated BioContainers addition for platypus-conquistador
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/platypus-conquistador
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/platypus-conquistador:0.9.0--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/platypus-conquistador/0.9.0--py_3
$ module help quay.io/biocontainers/platypus-conquistador/0.9.0--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### platypus-conquistador-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### platypus-conquistador-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### platypus-conquistador-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### platypus-conquistador-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### platypus-conquistador-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### platypus-conquistador-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iptest2

```bash
$ singularity exec <container> /usr/local/bin/iptest2
$ podman run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython2

```bash
$ singularity exec <container> /usr/local/bin/ipython2
$ podman run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### platypus

```bash
$ singularity exec <container> /usr/local/bin/platypus
$ podman run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
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