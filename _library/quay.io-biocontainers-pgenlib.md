---
layout: container
name:  "quay.io/biocontainers/pgenlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgenlib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgenlib/container.yaml"
updated_at: "2025-08-20 03:22:38.868427"
latest: "0.93.0--py39h475c85d_0"
container_url: "https://biocontainers.pro/tools/pgenlib"
aliases:
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.90.1--py310h551a815_0"
 - "0.90.2--py38h6c5ba02_0"
 - "0.90.2--py310h551a815_0"
 - "0.90.2--py312hf0ab922_1"
 - "0.91.0--py311hc849397_0"
 - "0.91.0--py312h5e9d817_1"
 - "0.92.1--py312h5e9d817_0"
 - "0.93.0--py39h475c85d_0"
description: "singularity registry hpc automated addition for pgenlib"
config: {"url": "https://biocontainers.pro/tools/pgenlib", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pgenlib", "latest": {"0.93.0--py39h475c85d_0": "sha256:dddd942f4eb6a451cc51af7a288ac58637f372d981a24ee63b8d236d41790513"}, "tags": {"0.90.1--py310h551a815_0": "sha256:60c573c7917153c77b62cc494a5ac014e62bf5ced1ed5b3a1078f7064f99daaf", "0.90.2--py38h6c5ba02_0": "sha256:283eb1252e8192c79ba70ddcb5806766f7b398652139eb42a8150072426693ee", "0.90.2--py310h551a815_0": "sha256:5acf608d0063b3b93e9100ad7160061893b7d2090f227455f974263be6083e75", "0.90.2--py312hf0ab922_1": "sha256:fc2175128f86c70b3de6808e3cda315a66e1ae3c7c57c1d22915b1f76ae2adf1", "0.91.0--py311hc849397_0": "sha256:c3aef8dffe8fd97edf443646e85909f8b2e443607abd164bef29a23b7d764967", "0.91.0--py312h5e9d817_1": "sha256:79fe60a52413a06bd0ba8e6f34005ced6008b7e29170d010b17e7bc30d7cf64c", "0.92.1--py312h5e9d817_0": "sha256:7e8c6ea83217debe9bfc4b0ad58eee04d3f5245190bcc22ed423c19ae3c9522d", "0.93.0--py39h475c85d_0": "sha256:dddd942f4eb6a451cc51af7a288ac58637f372d981a24ee63b8d236d41790513"}, "docker": "quay.io/biocontainers/pgenlib", "aliases": {"f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgenlib.
singularity registry hpc automated addition for pgenlib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgenlib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgenlib:0.93.0--py39h475c85d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgenlib/0.93.0--py39h475c85d_0
$ module help quay.io/biocontainers/pgenlib/0.93.0--py39h475c85d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgenlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgenlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgenlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgenlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgenlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgenlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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