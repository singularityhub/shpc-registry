---
layout: container
name:  "quay.io/biocontainers/anise_basil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/anise_basil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/anise_basil/container.yaml"
updated_at: "2024-09-05 03:05:04.733500"
latest: "1.2.0--py312hc60241a_8"
container_url: "https://biocontainers.pro/tools/anise_basil"
aliases:
 - "anise"
 - "basil"
 - "filter_basil.py"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "pyvenv"
versions:
 - "1.2.0--py36hcb2eddc_3"
 - "1.2.0--py39h1442aad_6"
 - "1.2.0--py38h529b8a6_6"
 - "1.2.0--py310h9da9059_7"
 - "1.2.0--py312hc60241a_8"
description: "shpc-registry automated BioContainers addition for anise_basil"
config: {"url": "https://biocontainers.pro/tools/anise_basil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for anise_basil", "latest": {"1.2.0--py312hc60241a_8": "sha256:e6141624c4f5843d660e53fec439eb7dbc95fd2f8b5fed8362fcc0eb38237fc5"}, "tags": {"1.2.0--py36hcb2eddc_3": "sha256:fba04d9b4155ce0cad72e78602e1f9d08e84cd3ae4765da8c264b640727dde12", "1.2.0--py39h1442aad_6": "sha256:a2bffd2574d4c3160ebfc15ace4c600079383b8b8499b3ead00d50c810cabde7", "1.2.0--py38h529b8a6_6": "sha256:20effeb6391a1d1b7faecfd4d091dcc95170607a60b4b1b650fcac37725d292b", "1.2.0--py310h9da9059_7": "sha256:be72c835025b2170c36b2c06a5edf196137ce9fad38c1eb4a6fb01c631220188", "1.2.0--py312hc60241a_8": "sha256:e6141624c4f5843d660e53fec439eb7dbc95fd2f8b5fed8362fcc0eb38237fc5"}, "docker": "quay.io/biocontainers/anise_basil", "aliases": {"anise": "/usr/local/bin/anise", "basil": "/usr/local/bin/basil", "filter_basil.py": "/usr/local/bin/filter_basil.py", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/anise_basil.
shpc-registry automated BioContainers addition for anise_basil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/anise_basil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/anise_basil:1.2.0--py312hc60241a_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/anise_basil/1.2.0--py312hc60241a_8
$ module help quay.io/biocontainers/anise_basil/1.2.0--py312hc60241a_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### anise_basil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### anise_basil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### anise_basil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### anise_basil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### anise_basil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### anise_basil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anise

```bash
$ singularity exec <container> /usr/local/bin/anise
$ podman run --it --rm --entrypoint /usr/local/bin/anise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basil

```bash
$ singularity exec <container> /usr/local/bin/basil
$ podman run --it --rm --entrypoint /usr/local/bin/basil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_basil.py

```bash
$ singularity exec <container> /usr/local/bin/filter_basil.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_basil.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_basil.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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