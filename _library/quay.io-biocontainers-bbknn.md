---
layout: container
name:  "quay.io/biocontainers/bbknn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bbknn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bbknn/container.yaml"
updated_at: "2025-10-10 03:34:52.283041"
latest: "1.6.0--py311h6cce608_5"
container_url: "https://biocontainers.pro/tools/bbknn"
aliases:
 - "numba"
 - "pycc"
 - "f2py3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
versions:
 - "1.5.1--py36h91eb985_2"
 - "1.6.0--py310h4b81fae_0"
 - "1.6.0--py39hf95cd2a_0"
 - "1.5.1--py38hbff2b2d_2"
 - "1.6.0--py310h7c593f9_1"
 - "1.6.0--py312hf67a6ed_3"
 - "1.6.0--py311haab0aaa_4"
 - "1.6.0--py311h6cce608_5"
description: "shpc-registry automated BioContainers addition for bbknn"
config: {"url": "https://biocontainers.pro/tools/bbknn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bbknn", "latest": {"1.6.0--py311h6cce608_5": "sha256:ff7a08c92ad83e1c29720f311b7e12a23038132ddb8189967346d740dffdcff4"}, "tags": {"1.5.1--py36h91eb985_2": "sha256:0c298061db57270d6b11a7447a2beddffda274faf832cc6770b12d0e777711a9", "1.6.0--py310h4b81fae_0": "sha256:ec18b86e37e11528f778d676ab1e01b5bff7c457ff25a45b76b02f86e67520df", "1.6.0--py39hf95cd2a_0": "sha256:009ecf7eb1fc6e83d434fc67f4e54adcae039af3913216ba038eaca0305d514d", "1.5.1--py38hbff2b2d_2": "sha256:ce18e7a16318b870015eae8e3c4ca8208a9683c21df8234d511fee382861831b", "1.6.0--py310h7c593f9_1": "sha256:bda4612f66e9c61330a04718c72d73b8dd282bf50d93ae3d6748b329daf566d1", "1.6.0--py312hf67a6ed_3": "sha256:e1f71465d121c493393b1094ea67c8873a310bd3d3149ea8efd3ddb4be30be86", "1.6.0--py311haab0aaa_4": "sha256:8c9627a46ec9609bc82adda4f48b6c4c2f8da50037d541342f2bb73921d98f73", "1.6.0--py311h6cce608_5": "sha256:ff7a08c92ad83e1c29720f311b7e12a23038132ddb8189967346d740dffdcff4"}, "docker": "quay.io/biocontainers/bbknn", "aliases": {"numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "f2py3.6": "/usr/local/bin/f2py3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bbknn.
shpc-registry automated BioContainers addition for bbknn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bbknn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bbknn:1.6.0--py311h6cce608_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bbknn/1.6.0--py311h6cce608_5
$ module help quay.io/biocontainers/bbknn/1.6.0--py311h6cce608_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bbknn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bbknn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bbknn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bbknn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bbknn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bbknn-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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