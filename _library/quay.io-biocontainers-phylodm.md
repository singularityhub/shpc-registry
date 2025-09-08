---
layout: container
name:  "quay.io/biocontainers/phylodm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phylodm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phylodm/container.yaml"
updated_at: "2025-09-08 04:55:37.062944"
latest: "3.2.0--py310hec43fc7_1"
container_url: "https://biocontainers.pro/tools/phylodm"
aliases:
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "2.1.3--py37he4bd417_1"
 - "2.2.1--py39h6a678da_0"
 - "3.0.0--py311h362c646_1"
 - "2.2.1--py39h6a678da_1"
 - "2.1.3--py310h079770c_1"
 - "3.1.0--py310hec43fc7_0"
 - "3.0.0--py38he1d39cf_2"
 - "3.2.0--py311h5e00ca1_0"
 - "3.2.0--py310hec43fc7_1"
description: "shpc-registry automated BioContainers addition for phylodm"
config: {"url": "https://biocontainers.pro/tools/phylodm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for phylodm", "latest": {"3.2.0--py310hec43fc7_1": "sha256:b4ff0062172f8c7446860ac38b9374481ad8a98cf1409e75f51b9965e30c49db"}, "tags": {"2.1.3--py37he4bd417_1": "sha256:4ea54aa7d2fdd149413efd99132a9942a7f2b935a9d10637425145db3d1b4ad2", "2.2.1--py39h6a678da_0": "sha256:141ab4a7e6995bfbe40415a8eb1442ae3650d7003faec75e078e25d92f5bc10e", "3.0.0--py311h362c646_1": "sha256:9d1e76e00234f11d3332f232d42c1c7f6d60354e90842db15c8a528024b2bb8f", "2.2.1--py39h6a678da_1": "sha256:c460596fed633941b5ee36ee1d508682c6ea742d1cfe1a492989f1a41c4bda0f", "2.1.3--py310h079770c_1": "sha256:e73def279ea1a9db1f369d2767168b01ee67ac20950bbaceb616111b2288d087", "3.1.0--py310hec43fc7_0": "sha256:c8564131f4e6ef567f47d74d4c956a330ba9c1db264a8e64c5cb7cb2e91223d7", "3.0.0--py38he1d39cf_2": "sha256:506a4e91cc930997d33f4bc4d5bf8d364f76e3345cac89a20069058170780d80", "3.2.0--py311h5e00ca1_0": "sha256:5960ee7390606eeea7db7a63fe3f94c6a58ac6fd9722fa03b6e2cac2e3a49c42", "3.2.0--py310hec43fc7_1": "sha256:b4ff0062172f8c7446860ac38b9374481ad8a98cf1409e75f51b9965e30c49db"}, "docker": "quay.io/biocontainers/phylodm", "aliases": {"f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phylodm.
shpc-registry automated BioContainers addition for phylodm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phylodm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phylodm:3.2.0--py310hec43fc7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phylodm/3.2.0--py310hec43fc7_1
$ module help quay.io/biocontainers/phylodm/3.2.0--py310hec43fc7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phylodm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phylodm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phylodm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phylodm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phylodm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phylodm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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