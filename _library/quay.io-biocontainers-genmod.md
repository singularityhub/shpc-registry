---
layout: container
name:  "quay.io/biocontainers/genmod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genmod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genmod/container.yaml"
updated_at: "2024-07-01 03:05:46.261693"
latest: "3.8.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/genmod"
aliases:
 - "genmod"
 - "ped_parser"
 - "py.test"
 - "pytest"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "3.7.4--pyh5e36f6f_0"
 - "3.8.0--pyh7cba7a3_0"
 - "3.8.1--pyh7cba7a3_0"
 - "3.8.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for genmod"
config: {"url": "https://biocontainers.pro/tools/genmod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genmod", "latest": {"3.8.2--pyhdfd78af_0": "sha256:216b9d376b3573013fa6daa3852176296deecc96dbf8ff0182fae84dc3051f23"}, "tags": {"3.7.4--pyh5e36f6f_0": "sha256:6be47a76892f05bcc2754a9c3d25ecda406e2a3b3ac6b4b7fd58ca14402d8ec9", "3.8.0--pyh7cba7a3_0": "sha256:481b1da36c3782afb2c0f6b01f5a403a7856e17c2358e7bad0e54dbfbfb8b540", "3.8.1--pyh7cba7a3_0": "sha256:a22671c4b065627741977e7bbbcc2b6fc87c33aefcb30c8b775b77728541eef2", "3.8.2--pyhdfd78af_0": "sha256:216b9d376b3573013fa6daa3852176296deecc96dbf8ff0182fae84dc3051f23"}, "docker": "quay.io/biocontainers/genmod", "aliases": {"genmod": "/usr/local/bin/genmod", "ped_parser": "/usr/local/bin/ped_parser", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genmod.
shpc-registry automated BioContainers addition for genmod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genmod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genmod:3.8.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genmod/3.8.2--pyhdfd78af_0
$ module help quay.io/biocontainers/genmod/3.8.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genmod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genmod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genmod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genmod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genmod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genmod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genmod

```bash
$ singularity exec <container> /usr/local/bin/genmod
$ podman run --it --rm --entrypoint /usr/local/bin/genmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ped_parser

```bash
$ singularity exec <container> /usr/local/bin/ped_parser
$ podman run --it --rm --entrypoint /usr/local/bin/ped_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ped_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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