---
layout: container
name:  "quay.io/biocontainers/burrito-fillings"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/burrito-fillings/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/burrito-fillings/container.yaml"
updated_at: "2024-10-13 10:52:29.535471"
latest: "0.1.1--py_3"
container_url: "https://biocontainers.pro/tools/burrito-fillings"
aliases:
 - "iptest3"
 - "iptest"
 - "ipython3"
 - "ipython"
 - "natsort"
 - "qhelpconverter"
 - "qwebengine_convert_dict"
 - "pygmentize"
 - "canbusutil"
 - "qgltf"
versions:
 - "0.1.1--py_3"
description: "shpc-registry automated BioContainers addition for burrito-fillings"
config: {"url": "https://biocontainers.pro/tools/burrito-fillings", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for burrito-fillings", "latest": {"0.1.1--py_3": "sha256:0dc7e53cdbc2c63e7151343305c7495fed722e85465059413c9c6f8fd422255f"}, "tags": {"0.1.1--py_3": "sha256:0dc7e53cdbc2c63e7151343305c7495fed722e85465059413c9c6f8fd422255f"}, "docker": "quay.io/biocontainers/burrito-fillings", "aliases": {"iptest3": "/usr/local/bin/iptest3", "iptest": "/usr/local/bin/iptest", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "natsort": "/usr/local/bin/natsort", "qhelpconverter": "/usr/local/bin/qhelpconverter", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "pygmentize": "/usr/local/bin/pygmentize", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/burrito-fillings.
shpc-registry automated BioContainers addition for burrito-fillings
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/burrito-fillings
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/burrito-fillings:0.1.1--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/burrito-fillings/0.1.1--py_3
$ module help quay.io/biocontainers/burrito-fillings/0.1.1--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### burrito-fillings-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### burrito-fillings-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### burrito-fillings-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### burrito-fillings-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### burrito-fillings-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### burrito-fillings-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
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